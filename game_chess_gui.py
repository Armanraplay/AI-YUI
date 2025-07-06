# game_chess_gui.py

import tkinter as tk
from tkinter import messagebox
import chess
import random
import json
import os

LOG_PATH = "chess_log.json"
SQUARE_SIZE = 64
COLORS = ["#F0D9B5", "#B58863"]  # Putih & coklat

class ChessGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Catur Yui")
        self.canvas = tk.Canvas(master, width=8*SQUARE_SIZE, height=8*SQUARE_SIZE)
        self.canvas.pack()

        self.board = chess.Board()
        self.selected_square = None
        self.move_history = []

        self.canvas.bind("<Button-1>", self.click)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(8):
            for col in range(8):
                x1 = col * SQUARE_SIZE
                y1 = row * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE
                color = COLORS[(row + col) % 2]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                col = chess.square_file(square)
                row = 7 - chess.square_rank(square)
                x = col * SQUARE_SIZE + SQUARE_SIZE // 2
                y = row * SQUARE_SIZE + SQUARE_SIZE // 2
                self.canvas.create_text(x, y, text=self.piece_unicode(piece), font=("Arial", 32))

    def piece_unicode(self, piece):
        symbol = piece.symbol()
        table = {
            'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
            'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚',
        }
        return table[symbol]

    def click(self, event):
        col = event.x // SQUARE_SIZE
        row = 7 - (event.y // SQUARE_SIZE)
        square = chess.square(col, row)

        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == chess.WHITE:
                self.selected_square = square
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.move_history.append(move.uci())
                self.draw_board()
                self.selected_square = None

                if not self.board.is_game_over():
                    self.master.after(500, self.yui_move)
                else:
                    self.end_game()
            else:
                self.selected_square = None

    def yui_move(self):
        legal_moves = list(self.board.legal_moves)
        if legal_moves:
            move = random.choice(legal_moves)
            self.board.push(move)
            self.move_history.append(move.uci())
            self.draw_board()

            if self.board.is_game_over():
                self.end_game()

    def end_game(self):
        result = self.board.result()
        winner = "Draw"
        if result == "1-0":
            winner = "User"
        elif result == "0-1":
            winner = "Yui"

        self.save_game_log(winner)
        messagebox.showinfo("Game Selesai", f"🏁 {winner} menang!" if winner != "Draw" else "🏁 Seri!")
        self.master.destroy()

    def save_game_log(self, winner):
        log = []
        if os.path.exists(LOG_PATH):
            with open(LOG_PATH, "r", encoding="utf-8") as f:
                try:
                    log = json.load(f)
                except json.JSONDecodeError:
                    log = []

        log.append({
            "winner": winner,
            "moves": self.move_history
        })

        with open(LOG_PATH, "w", encoding="utf-8") as f:
            json.dump(log, f, indent=2)

def play_chess_gui():
    root = tk.Tk()
    app = ChessGUI(root)
    root.mainloop()
