# 🧩 8-Puzzle Solver (A* & BFS)

An interactive Python application that solves the classic 8-Puzzle (Taquin) using Artificial Intelligence search algorithms. The project features a graphical interface built with Tkinter and supports both manual gameplay and automatic puzzle solving.

## 🚀 Features

- Interactive Tkinter-based graphical interface
- A* search algorithm with Manhattan distance heuristic
- BFS (Best-First Search) solver implementation
- Randomized and custom board configurations
- Animated step-by-step solution visualization
- Performance comparison through iteration statistics

## 🛠️ Technologies Used

- Python 3
- Tkinter
- PriorityQueue
- heapq
- random

## 🧠 Implemented Algorithms

### A* Search
Uses the evaluation function:

f(n) = g(n) + h(n)

Where:
- `g(n)` = cost from the initial state
- `h(n)` = Manhattan distance heuristic

Provides optimal solutions while minimizing the number of moves.

### Best-First Search (BFS)
Explores states according to their heuristic value and prioritizes the most promising nodes first.

## 📊 Heuristic Function

The project uses the **Manhattan Distance** heuristic:

- Sum of the distances between each tile's current position and its target position.
- Efficient and widely used for sliding puzzle problems.

## 🎮 Usage

### Run the application

```bash
python main.py
```

### Available Actions

- Generate a random puzzle configuration
- Enter a custom puzzle state manually
- Solve using A*
- Solve using BFS
- Visualize the solution through animated tile movements


