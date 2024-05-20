import random
import tkinter as tk
from tkinter import messagebox
def aruncare_zaruri():
    return [random.randint(1, 6) for _ in range(6)]

def calculeaza_punctaj(zaruri, formatie):
    if formatie in ["1", "2", "3", "4", "5", "6"]:
        return sum(d for d in zaruri if d == int(formatie))
    elif formatie == "mici":
        return sum(d for d in zaruri if d <= 3)
    elif formatie == "mari":
        return sum(d for d in zaruri if d >= 4)
    elif formatie == "pare":
        return sum(d for d in zaruri if d % 2 == 0)
    elif formatie == "impare":
        return sum(d for d in zaruri if d % 2 != 0)
    elif formatie == "duble":
        for i in range(1, 7):
            if zaruri.count(i) >= 2:
                return 3 * i
        return 0
    elif formatie == "triple":
        for i in range(1, 7):
            if zaruri.count(i) >= 3:
                return 2 * 3 * i
        return 0
    elif formatie == "suita":
        if sorted(zaruri) == [1, 2, 3, 4, 5, 6]:
            return 20
        return 0
    elif formatie == "care":
        if zaruri.count(6) >= 4:
            return sum(zaruri)
        return 0
    elif formatie == "cameron":
        if zaruri == [4, 6, 4, 6, 4, 6]:
            return 36
        return 0

def main():
    nume_jucator = input("Introduceți numele jucatorului: ")
    formatii_disponibile = ["1", "2", "3", "4", "5", "6", "mici", "mari", "pare", "impare", "duble", "triple", "suita", "care", "cameron"]
    formatii_realizate = []
    punctaj_total = 0

    for _ in range(15):
        input("Apasați ENTER pentru a arunca zarurile...")
        zaruri = aruncare_zaruri()
        print("Zarurile aruncate sunt:", zaruri)
        formatie_aleasa = input("Alegeți o formație disponibila sau renunțați (scrieți 'renunță'): ").lower()
        if formatie_aleasa == "renunță":
            print("Ați renunțat la această formație.")
            punctaj_total -= 3
        elif formatie_aleasa in formatii_disponibile:
            punctaj_formatie = calculeaza_punctaj(zaruri, formatie_aleasa)
            print(f"Punctajul pentru formația {formatie_aleasa} este: {punctaj_formatie}")
            punctaj_total += punctaj_formatie
            formatii_realizate.append(formatie_aleasa)
            formatii_disponibile.remove(formatie_aleasa)
        else:
            print("Formație invalidă!")
    if len(formatii_realizate) == 15:
        punctaj_total += 20
        print("Felicitări, ați completat toate formațiile și ați primit un bonus de 20 de puncte!")

    print("Jocul s-a încheiat. Punctaj total:", punctaj_total)

def arunca_zaruri_si_calculeaza():
    global punctaj_total
    zaruri = aruncare_zaruri()
    messagebox.showinfo("Zaruri aruncate", f"Zarurile aruncate sunt: {zaruri}")
    formatie_aleasa = input_box.get().lower()
    if formatie_aleasa == "renunță":
        messagebox.showinfo("Renunțare", "Ați renunțat la această formație.")
        punctaj_total -= 3
    elif formatie_aleasa in formatii_disponibile:
        punctaj_formatie = calculeaza_punctaj(zaruri, formatie_aleasa)
        messagebox.showinfo("Punctaj", f"Punctajul pentru formația {formatie_aleasa} este: {punctaj_formatie}")
        punctaj_total += punctaj_formatie
        formatii_realizate.append(formatie_aleasa)
        formatii_disponibile.remove(formatie_aleasa)
    else:
        messagebox.showinfo("Formație invalidă", "Formație invalidă!")
    input_box.delete(0, tk.END)
    if len(formatii_realizate) == 15:
        punctaj_total += 20
        messagebox.showinfo("Felicitări!", "Ați completat toate formațiile și ați primit un bonus de 20 de puncte!")
    punctaj_label.config(text=f"Punctaj total: {punctaj_total}")

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
