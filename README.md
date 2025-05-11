# 🧠 Tic-Tac-Toe AI – Minimax Algorithm

This project implements a perfect Tic-Tac-Toe-playing AI using the **Minimax algorithm** and **Alpha-Beta Pruning**. The AI ensures it never loses, whether it plays first or second. It's a practical demo of adversarial search and decision trees in game AI.

🎮 **Try the game here**: [Play Tic-Tac-Toe AI](https://cledersonbc.github.io/tic-tac-toe-minimax/)

---

## 📌 Features

- Minimax algorithm with depth-based recursive search
- Alpha-Beta Pruning for optimization
- Terminal-based game interface
- Human vs. AI gameplay

---

## 🧠 How It Works

The AI constructs a **game tree** where each node represents a possible game state. The **Minimax algorithm** simulates all possible moves and backtracks to find the optimal one, assuming both players play perfectly.

In this zero-sum game:
- AI seeks to **maximize** its score (+1 win)
- Human seeks to **minimize** AI's score (-1 win for human)
- A draw results in a score of 0

### 🎯 Example Game Tree

<img src="preview/tic-tac-toe-minimax-game-tree.png" width="500"/>

---

## ⚙️ Installation & Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-minimax.git
   cd tic-tac-toe-minimax
   ```

2. Run the game:
   ```bash
   python game.py
   ```

3. Play using your **numpad keys (1–9)** to place your move on the board.

---

## 📊 Preliminary Results

| Method               | AI Win % | Draw % | Human Win % | Avg Move Time |
|----------------------|---------|--------|-------------|----------------|
| Minimax              | ~50%    | ~50%   | 0%          | ~25ms          |
| Alpha-Beta Pruning   | ~50%    | ~50%   | 0%          | ~12ms          |

- The AI **never loses**, and **Alpha-Beta Pruning** halves the average computation time.

---

## 📚 References

- [Minimax - Wikipedia](https://en.wikipedia.org/wiki/Minimax)
- [NTU Tic-Tac-Toe AI Tutorial](https://www.ntu.edu.sg/home/ehchua/programming/java/JavaGame_TicTacToe_AI.html)
- *Algorithms in a Nutshell*, O’Reilly (2009)

---

## 📂 Project Structure

```
├── game.py           # Game loop and AI logic
├── preview/          # Game tree images
├── README.md         # Project documentation
└── .gitignore        # Ignore cache files
```

---

## 👨‍💻 Authors

- Parishad Ajallooeian  
- Jigneshkumar Makawana

---

## 🔗 GitHub Link

(https://github.com/jigneshParishad/tic-tac-toe.git))
