#!/bin/bash

declare -A readme_contents=(
  ["tictactoe"]="TicTacToe
Game optimized for performance, where the computer plays itself using random choices (no strategy). Logs include: who played first, was it a draw, who won, did the first player win, first move position, full move sequence, number of moves, and win method (e.g., row_1, diag_anti) saved to a CSV file. Develop multiple computer agents with different strategies. Backtracking can be used to simulate future game states and evaluate optimal moves (e.g., using minimax). Dynamic programming can cache board evaluations to avoid redundant computation during simulations."
  
  ["sequence"]="Sequence
Build an accurate version of the Sequence game. Implement board logic, card handling, and rules. Support two or three players or teams. Optimize for performance and allow AI agents with a mix of strategy and randomness. Backtracking can simulate token placements and analyze optimal sequences. Dynamic programming helps detect sequences efficiently on the grid by caching token alignments."
  
  ["dasher"]="Dasher
Simulate a delivery game where an agent navigates a city represented as a graph to complete delivery tasks. Player: Accepts, cancels (before pickup), picks up, and delivers orders while managing a limited budget (distance/time). City Map: Modeled as a weighted graph (nodes = locations, edges = roads with distance/time). Orders: Randomly generated with pickup/drop-off points, payouts, and time windows. Agent Strategies: Greedy: Accept highest-paying nearby order. Shortest Path: Choose orders along the most efficient route. Backtracking explores different sequences of order fulfillment for maximum efficiency. Dynamic programming helps solve route optimization and delivery selection problems Heaps are used to manage order priority (highest payout, nearest expiration) and for shortest-path algorithms like Dijkstra’s. Trees and decision trees can model planning decisions across delivery sequences."
  
  ["webcrawler"]="WebCrawler
Crawl a Wikipedia page and recursively explore links, generating a report that includes: All discovered links Tree structure of the site Depth of each page Dead or unreachable links Graphs represent the hyperlink structure of the site. Backtracking handles recursive exploration with rollback on dead ends. Dynamic programming caches visited URLs to avoid redundant work."
  
  ["webscraper"]="WebScraper (TMDB)
Scrape The Movie Database (TMDB) to find the top N trending movies and sort/filter them based on ratings, genres, popularity, and other metadata. Heaps are used to maintain top-N rated/trending movies efficiently. Tries (optional) can enable fast autocomplete or search indexing for actor/movie names. Use trees to parse and represent category or genre hierarchies."
  
  ["explorer"]="Explorer
A file explorer for creating, reading, updating, and deleting files/folders starting from a root directory. Includes user/owner permissions and role-based access. Command history and undo supported via a stack. Autocorrect for commands and paths using edit distance + dynamic programming. Trie stores valid commands and paths for fast prefix search and autocorrect. The filesystem is structured as a tree, and symbolic links (if supported) can introduce a DAG structure. Backtracking enables undo/redo of file operations. Heaps can identify top-N largest or most recent files."
  
  ["echo"]="Echo Music Player
Terminal-based music player that allows users to: Add and manage music from the device Search artists/songs Queue, play, pause, resume, stop tracks Reverse or reorder queue sections View top/least played or searched songs Manage playlists and remove songs from the library Autocorrect for searches using edit distance + dynamic programming Trie stores artist and song names for fast prefix-based search and autocorrect Heaps maintain top/least played and searched track lists"
  
  ["automod"]="AutoMod
A bot that continuously monitors and redacts personally identifiable information (PII) such as emails, phone numbers, and SSNs from incoming content streams (e.g., from https://jsonplaceholder.typicode.com/). Use tries to store and match common sensitive patterns (e.g., name parts, domains). Model complex PII patterns using finite automata (state machines as trees or graphs). Dynamic programming helps in pattern recognition and error-tolerant matching (e.g., misformatted PII). Heaps can rank detected PII by severity or confidence score (optional)."
)

for folder in "${!readme_contents[@]}"; do
  echo "Updating README.md in $folder..."
  echo -e "${readme_contents[$folder]}" > "$folder/README.md"
done

echo "All README.md files updated."
