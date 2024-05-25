import random   //Importam functia random pentru a genera numere aleatoare zarului
import tkinter as tk   // Aceasta linie importa biblioteca tkinter si o denumeste tk pentru interfata grafica
from tkinter import messagebox   // importam messagebox pentru a avea o fereastra ca si interfata grafica unde ne sunt afisate rezultatele

# se introduc bibliotecile necesare

def aruncare_zaruri():  //functia pentru zaruri
    return [random.randint(1, 6) for _ in range(6)] //rezultatul functie pentru zaruri cu rezultate aleatoare

# definirea functiei pentru aruncarea zarurilor care returneaza 6 numere aleatorii unul pt fiecare zar

def calculeaza_punctaj(zaruri, formatie):  //functie pentru calcularea punctajului
    if formatie in ["1", "2", "3", "4", "5", "6"]:   // verificam continutul formatiei(daca acesta se afla in lista data)
        return sum(d for d in zaruri if d == int(formatie)) // se returneaza suma anumitor elemente, daca acestea formeaza
        # verifica valoarea zarului in intervalul 1-6 si da suma valorilor din zaruri
    elif formatie == "mici": // verificam daca este o formatie de numere mici
        return sum(d for d in zaruri if d <= 3) // calculeaza suma anumitor elemente din lista zaruri, mai exact a elementelor mai mici decat 3
        # suma doar pt cele mai mici decat 3 
    elif formatie == "mari": // verificam daca este o formatie de numere mari
        return sum(d for d in zaruri if d >= 4)
        # suma mai mari decat 4
    elif formatie == "pare":  // verificam daca este o formatie de numere pare
        return sum(d for d in zaruri if d % 2 == 0)
        #pt pare
    elif formatie == "impare":  // verificam daca este o formatie de numere impare
        return sum(d for d in zaruri if d % 2 != 0)
        #pt impare
    elif formatie == "duble":  // verificam daca este o formatie de numere impare
        for i in range(1, 7):
            if zaruri.count(i) >= 2:
                return 3 * i
        return 0
        #varifica daca un nr apare de 2 ori in interval si ii retuneaza valoare triplata
    elif formatie == "triple":
        for i in range(1, 7):
            if zaruri.count(i) >= 3:
                return 2 * 3 * i
        return 0
        # same dar aici verifica daca apare de 3 ori
    elif formatie == "suita":
        if sorted(zaruri) == [1, 2, 3, 4, 5, 6]:
            return 20
        return 0
        #daca cele 6 zaruri pot forma numerele de la 1 la 6 si automat ofera participantului 20 de puncte, daca nu se formeaza o suita completa se ofera 0 puncte
    elif formatie == "care":
        if zaruri.count(6) >= 4:
            return sum(zaruri)
        return 0
        #daca 6 apare de min 4 ori retuneaza suma acelor zaruri, daca nu se returneaza 0 puncte
    elif formatie == "cameron":
        if zaruri == [4, 6, 4, 6, 4, 6]:
            return 36
        return 0
        #doar daca sunt in aceasta formatie se returneaza 36 de puncte, in caz contrar 0 puncte

def arunca_zaruri_si_calculeaza():
    global punctaj_total  //parametru global
    global formatii_realizate  //parametru global
    zaruri = aruncare_zaruri()  // variabila zaruri apeleaza functia aruncare zaruri
    messagebox.showinfo("Zaruri aruncate", f"Zarurile aruncate sunt: {zaruri}")  // se afiseaza in fereastra creeata un mesaj cu zarurile aruncate
    formatie_aleasa = input_box.get().lower()  // se tasteaza formatia aleasa si se converteste in litere mici 
    if formatie_aleasa == "renunță":  // Daca jucatorul a ales sa renunte
        messagebox.showinfo("Renunțare", "Ați renunțat la această formație.")  // se va afisa in fereastra mesajul din interiorul printului
        punctaj_total -= 3  // se scad 3 puncte din punctajul total
    elif formatie_aleasa in formatii_disponibile:  // daca formatia aleasa se afla in lista de formatii disponibile
        punctaj_formatie = calculeaza_punctaj(zaruri, formatie_aleasa)  // se calculeaza punctajul formatiei care primeste ca parametrii lista de zaruri si formatia
        messagebox.showinfo("Punctaj", f"Punctajul pentru formația {formatie_aleasa} este: {punctaj_formatie}")  // se afiseaza punctajul obtinut pentru formatia aleasa
        punctaj_total += punctaj_formatie  // se adauga acest punctaj la punctajul total al jucatorului
        formatii_realizate.append(formatie_aleasa)  // adauga formatia aleasa de jucator in lista de formatii realizate
        formatii_disponibile.remove(formatie_aleasa)  // se sterge automat din lista de formatii disponibile formatia aleasa de jucator
    else:
        messagebox.showinfo("Formație invalidă", "Formație invalidă!")
    input_box.delete(0, tk.END)
    if len(formatii_realizate) == 15:  // daca jucatorul a realizat toate cele 15 formatii
        punctaj_total += 20  // se mai adauga 20 de puncte la punctajul total
        messagebox.showinfo("Felicitări!", "Ați completat toate formațiile și ați primit un bonus de 20 de puncte!")//se afiseaza urmatorul mesaj in consola daca este indeplinita conditia
    punctaj_label.config(text=f"Punctaj total: {punctaj_total}")  //actualizeaza textul etichetei pentru a afisa noul punctaj total
    formatii_label.config(text=f"Formații realizate: {', '.join(formatii_realizate)}")

def start_game():
    global punctaj_total
    global formatii_realizate
    global formatii_disponibile
    global input_box
    global punctaj_label
    global formatii_label

    //declararea unor parametrii ca fiind globali pentru a putea fi folostiti in alte functii
    
    punctaj_total = 0  // parametru pentru punctajul total initializat cu 0
    formatii_realizate = []  // o lista goala in care se stocheaza formatiile realizate de jucatori
    formatii_disponibile = ["1", "2", "3", "4", "5", "6", "mici", "mari", "pare", "impare", "duble", "triple", "suita", "care", "cameron"]  //lista cu formatiile

    root = tk.Tk()  
    root.title("Cameroon")  //modificarea titlului la Cameroon

    # Stilizare și configurare
    root.geometry("500x400")
    root.configure(bg="#fff176")  # Fundal galben

    # Stiluri
    title_font = ("Helvetica", 18, "bold")
    label_font = ("Helvetica", 12)
    button_font = ("Helvetica", 12, "bold")

    # Culori
    title_color = "#283593"
    bg_color = "#fff176"  # Fundal galben
    input_bg_color = "#fff9c4"
    button_bg_color = "#f57f17"
    button_fg_color = "white"
    label_bg_color = bg_color

    title_label = tk.Label(root, text="Cameroon", font=title_font, fg=title_color, bg=bg_color)
    title_label.pack(pady=20)

    input_frame = tk.Frame(root, bg=bg_color)
    input_frame.pack(pady=10)

    input_label = tk.Label(input_frame, text="Alegeți o formă disponibilă sau renunțați:", font=label_font, bg=label_bg_color)
    input_label.pack(side=tk.LEFT, padx=5)

    input_box = tk.Entry(input_frame, bg=input_bg_color)
    input_box.pack(side=tk.LEFT)

    arunca_button = tk.Button(root, text="Aruncă zarurile și calculează", command=arunca_zaruri_si_calculeaza, bg=button_bg_color, fg=button_fg_color, font=button_font)
    arunca_button.pack(pady=10)

    punctaj_label = tk.Label(root, text=f"Punctaj total: {punctaj_total}", font=label_font, bg=label_bg_color)
    punctaj_label.pack(pady=5)

    formatii_label = tk.Label(root, text="Formații realizate: ", font=label_font, bg=label_bg_color)
    formatii_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":  //verifica daca fisierul este rulat direct
    start_game()   //apeleaza functia start_game care contine interfata grafica si variabilele globale
