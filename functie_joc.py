import random
import tkinter as tk
from tkinter import messagebox

def start_game():
    global punctaj_total
    global formatii_realizate
    global formatii_disponibile
    punctaj_total = 0
    formatii_realizate = []
    formatii_disponibile = ["1", "2", "3", "4", "5", "6", "mici", "mari", "pare", "impare", "duble", "triple", "suită", "caré", "cameron"]

    root = tk.Tk()
    root.title("Joc cu zaruri")

    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    input_label = tk.Label(input_frame, text="Alegeți o formă disponibilă sau renunțați:")
    input_label.pack(side=tk.LEFT)

    global input_box
    input_box = tk.Entry(input_frame)
    input_box.pack(side=tk.LEFT)

    arunca_button = tk.Button(root, text="Aruncă zarurile și calculează", command=arunca_zaruri_si_calculeaza)
    arunca_button.pack(pady=5)

    global punctaj_label
    punctaj_label = tk.Label(root, text=f"Punctaj total: {punctaj_total}")
    punctaj_label.pack()
    root.mainloop()

if __name__ == "__main__":
    start_game()