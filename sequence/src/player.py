class Player:
    def __init__(self, player_id, name, is_cpu=False):
        self.player_id = player_id
        self.name = name
        self.is_cpu = is_cpu
        self.tokens = 0  # Track tokens placed or other stats as needed

    def __str__(self):
        return f"Player {self.name} (ID: {self.player_id})"
