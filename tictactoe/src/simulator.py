# simulator.py

import argparse
import random
import os
from .game import Game
from .logger import log_game, init_log, reset_log, LOG_PATH
from .agents import RandomAgent, RulesAgent, MinimaxAgent #ForkAgent

# Register available agent types
AGENT_TYPES = {
    "random": RandomAgent,
    "rules": RulesAgent,
    #"fork": ForkAgent,
    "minimax": MinimaxAgent,
}

def pick_random_agents():
    agent_classes = list(AGENT_TYPES.values())
    agent1 = random.choice(agent_classes)()
    agent2 = random.choice(agent_classes)()
    return agent1, agent2
def run_simulation(n_games: int):
    # Reset log if it already exists
    if os.path.exists(LOG_PATH):
        reset_log()
    else:
        init_log()

    for game_id in range(1, n_games + 1):
        agent1, agent2 = pick_random_agents()

        # 🔀 Randomize who goes first
        if random.choice([True, False]):
            x_agent, o_agent = agent1, agent2
        else:
            x_agent, o_agent = agent2, agent1

        game = Game(x_agent, o_agent, game_id)
        result = game.run()
        log_game(result)

        if game_id % 100 == 0 or game_id == n_games:
            print(f"[INFO] Completed {game_id} games.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run TicTacToe AI simulations.")
    parser.add_argument("n", type=int, help="Number of games to simulate")
    args = parser.parse_args()

    run_simulation(args.n)
