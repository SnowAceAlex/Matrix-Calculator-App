import tkinter as tk
from tkinter import messagebox
import numpy as np


class FlatButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            bg="#95a5a6",
            fg="white",
            relief="flat",
            padx=15,
            pady=8,
            font=("Helvetica", 10),
            activebackground="#7f8c8d"
        )
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = "#7f8c8d"

    def on_leave(self, e):
        self['background'] = "#95a5a6"


class FlatEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief="flat",
            bg="#ecf0f1",
            fg="#2c3e50",
            font=("Helvetica", 10),
            insertbackground="#2c3e50"
        )


class MatrixCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")
        self.root.configure(bg="#e8f3f1")

        # Colors
        self.colors = {
            "bg": "#e8f3f1",
            "frame": "#d5e8e3",
            "label_bg": "#c1dfd7"
        }

        # Matrix dimensions
        self.rows = 2
        self.cols = 2

        # Add padding around the window
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Create title
        title = tk.Label(
            self.root,
            text="Matrix Calculator",
            font=("Helvetica", 16, "bold"),
            bg=self.colors["bg"],
            fg="#2c3e50",
            pady=15
        )
        title.pack()

        self.create_matrix_frames()
        self.create_operation_buttons()

    def create_matrix_frames(self):
        frame_style = {
            "bg": self.colors["frame"],
            "relief": "flat",
            "padx": 15,
            "pady": 10
        }

        # Matrix A
        self.matrix_a_frame = tk.LabelFrame(
            self.root,
            text="Matrix A",
            font=("Helvetica", 10, "bold"),
            **frame_style
        )
        self.matrix_a_frame.pack(padx=20, pady=5)
        self.matrix_a_entries = self.create_matrix_entries(self.matrix_a_frame)

        # Matrix B
        self.matrix_b_frame = tk.LabelFrame(
            self.root,
            text="Matrix B",
            font=("Helvetica", 10, "bold"),
            **frame_style
        )
        self.matrix_b_frame.pack(padx=20, pady=5)
        self.matrix_b_entries = self.create_matrix_entries(self.matrix_b_frame)

        # Result Matrix
        self.result_frame = tk.LabelFrame(
            self.root,
            text="Result",
            font=("Helvetica", 10, "bold"),
            **frame_style
        )
        self.result_frame.pack(padx=20, pady=5)
        self.result_labels = self.create_result_labels(self.result_frame)

    def create_matrix_entries(self, frame):
        entries = []
        for i in range(self.rows):
            row_entries = []
            for j in range(self.cols):
                entry = FlatEntry(frame, width=8)
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry.insert(0, "0")
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def create_result_labels(self, frame):
        labels = []
        for i in range(self.rows):
            row_labels = []
            for j in range(self.cols):
                label = tk.Label(
                    frame,
                    width=8,
                    bg=self.colors["label_bg"],
                    relief="flat",
                    font=("Helvetica", 10),
                    pady=5
                )
                label.grid(row=i, column=j, padx=5, pady=5)
                label.config(text="0")
                row_labels.append(label)
            labels.append(row_labels)
        return labels

    def create_operation_buttons(self):
        button_frame = tk.Frame(self.root, bg=self.colors["bg"])
        button_frame.pack(pady=15)

        operations = [
            ("Add", self.add_matrices, "#3498db"),
            ("Subtract", self.subtract_matrices, "#e74c3c"),
            ("Multiply", self.multiply_matrices, "#2ecc71"),
            ("Clear", self.clear_matrices, "#95a5a6")
        ]

        for text, command, color in operations:
            btn = FlatButton(
                button_frame,
                text=text,
                command=command,
                bg=color,
                width=8
            )
            btn.pack(side=tk.LEFT, padx=5)

    def get_matrix_values(self, entries):
        try:
            return [[float(entry.get()) for entry in row] for row in entries]
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numbers only.")
            return None

    def display_result(self, result):
        for i in range(self.rows):
            for j in range(self.cols):
                self.result_labels[i][j].config(text=f"{result[i][j]:.2f}")

    def add_matrices(self):
        a = self.get_matrix_values(self.matrix_a_entries)
        b = self.get_matrix_values(self.matrix_b_entries)
        if a and b:
            result = np.add(a, b)
            self.display_result(result)

    def subtract_matrices(self):
        a = self.get_matrix_values(self.matrix_a_entries)
        b = self.get_matrix_values(self.matrix_b_entries)
        if a and b:
            result = np.subtract(a, b)
            self.display_result(result)

    def multiply_matrices(self):
        a = self.get_matrix_values(self.matrix_a_entries)
        b = self.get_matrix_values(self.matrix_b_entries)
        if a and b:
            result = np.matmul(a, b)
            self.display_result(result)

    def clear_matrices(self):
        for entries in [self.matrix_a_entries, self.matrix_b_entries]:
            for row in entries:
                for entry in row:
                    entry.delete(0, tk.END)
                    entry.insert(0, "0")
        for row in self.result_labels:
            for label in row:
                label.config(text="0")


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculator(root)
    root.mainloop()