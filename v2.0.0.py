import random  # Importam functia random pentru a genera numere aleatoare zarului
import tkinter as tk  # Aceasta linie importa biblioteca tkinter si o denumeste tk pentru interfata grafica
from tkinter import \
    messagebox  # importam messagebox pentru a avea o fereastra ca si interfata grafica unde ne sunt afisate rezultatele


def aruncare_zaruri(): # functia pentru zaruri
    return [random.randint(1, 6) for _ in range(6)] #rezultatul functie pentru zaruri cu rezultate aleatoare


def calculeaza_punctaj(zaruri, formatie): # functie pentru calcularea punctajului
    if formatie in ["1", "2", "3", "4", "5", "6"]: #verificam continutul formatiei(daca acesta se afla in lista data)
        return sum(d for d in zaruri if d == int(formatie)) # verifica valoarea zarului in intervalul 1-6 si da suma valorilor din zaruri
    elif formatie == "mici": # verificam daca este o formatie de numere mici
        return sum(d for d in zaruri if d <= 3)
    elif formatie == "mari": # verificam daca este o formatie de numere mari
        return sum(d for d in zaruri if d >= 4)
    elif formatie == "pare": # verificam daca este o formatie de numere pare
        return sum(d for d in zaruri if d % 2 == 0)
    elif formatie == "impare": # verificam daca este o formatie de numere impare
        return sum(d for d in zaruri if d % 2 != 0)
    elif formatie == "duble":
        for i in range(1, 7):
            if zaruri.count(i) >= 2:
                return 3 * i
        return 0
    # verifica daca un nr apare de 2 ori in interval si ii returneaza valoarea triplata
    elif formatie == "triple":
        for i in range(1, 7):
            if zaruri.count(i) >= 3:
                return 2 * 3 * i
        return 0
    # verifica daca un nr apare de 3 ori in interval si ii returneaza de 6 ori valoarea
    elif formatie == "suita":
        if sorted(zaruri) == [1, 2, 3, 4, 5, 6]:
            return 20
        return 0
    # daca cele 6 zaruri sunt numere de la 1 la 6, automat jucatorul primeste 20 de puncte, daca nu este suita completa primeste 0
    elif formatie == "care":
        if zaruri.count(6) >= 4:
            return sum(zaruri)
        return 0
    # daca 6 apare de min 4 ori retuneaza suma acelor zaruri, daca nu se returneaza 0 puncte
    elif formatie == "cameron":
        if zaruri == [4, 6, 4, 6, 4, 6]:
            return 36
        return 0
    # doar daca sunt in aceasta formatie se returneaza 36 de puncte, in caz contrar 0 puncte

def arunca_zaruri_si_calculeaza():
    global punctaj_total_jucator1
    global punctaj_total_jucator2
    global formatii_realizate_jucator1
    global formatii_realizate_jucator2
    global formatii_disponibile
    global jucator_curent
    # parametrii globali pentru a putea fi utilizati si in alte functii

    zaruri = aruncare_zaruri() # variabila zaruri apeleaza functia aruncare zaruri
    messagebox.showinfo("Zaruri aruncate", f"Zarurile aruncate sunt: {zaruri}")
    formatie_aleasa = input_box.get().lower() # se tasteaza formatia aleasa si se converteste in litere mici

    if formatie_aleasa == "renunta": # Daca jucatorul a ales sa renunte prin tastarea mesajului "renunta"
        messagebox.showinfo("Renunțare", "Ați renunțat la această formație.") #se va afisa mesajul acesta
        if jucator_curent == 1: #verifica daca jucatorul curent este primul
            punctaj_total_jucator1 -= 3 #daca da ii scade acestuia din punctaj 3 puncte
        else:
            punctaj_total_jucator2 -= 3 #in caz contrar ii scade celui de al doilea jucator
    elif formatie_aleasa in formatii_disponibile: #verifica daca formatia aleasa este in formatiile disponibile
        punctaj_formatie = calculeaza_punctaj(zaruri, formatie_aleasa) #se calculeaza punctajul formatiei care primeste ca parametrii lista de zaruri si formatia
        messagebox.showinfo("Punctaj", f"Punctajul pentru formația {formatie_aleasa} este: {punctaj_formatie}")
        # se afiseaza punctajul pentru formatia respectiva
        if jucator_curent == 1: #verifica daca jucatorul curent este primul
            punctaj_total_jucator1 += punctaj_formatie #daca da ii adauga punctajul acumulat la punctajul total
            formatii_realizate_jucator1.append(formatie_aleasa) #ii adauga si formatia la formatii realizate
        else:
            punctaj_total_jucator2 += punctaj_formatie #daca nu adauga la cel de al doilea jucator
            formatii_realizate_jucator2.append(formatie_aleasa)

        formatii_disponibile.remove(formatie_aleasa) # se sterge automat din lista de formatii disponibile formatia aleasa de jucator
    else:
        messagebox.showinfo("Formație invalidă", "Formație invalidă!")
    # Daca formatia nu este valida se afiseaza mesajul de mai sus

    input_box.delete(0, tk.END) #sterge textul introdus in caseta pentru a putea introduce din nou altul

    if len(formatii_realizate_jucator1) + len(formatii_realizate_jucator2) == 15: #verifica daca totalul formatiilor realizate de jucatori este 15
        if jucator_curent == 1:  #verifica daca este primul jucator
            punctaj_total_jucator1 += 20 #daca da acesta primeste automat 20 de puncte pentru aceasta realizare
            messagebox.showinfo("Felicitări!",
                                f"{nume_jucator1}, ați completat toate formațiile și ați primit un bonus de 20 de puncte!")
            # se afiseaza mesajul la realizarea tuturor formatiilor
        else:
            punctaj_total_jucator2 += 20 #altfel ii ofera 20 de puncte celui de al doilea jucator
            messagebox.showinfo("Felicitări!",
                                f"{nume_jucator2}, ați completat toate formațiile și ați primit un bonus de 20 de puncte!")

    punctaj_label.config(
        text=f"Punctaj {nume_jucator1}: {punctaj_total_jucator1}    Punctaj {nume_jucator2}: {punctaj_total_jucator2}")
    formatii_label.config(
        text=f"Formații realizate: {nume_jucator1}: {', '.join(formatii_realizate_jucator1)} | {nume_jucator2}: {', '.join(formatii_realizate_jucator2)}")
    # actualizarea punctajelor pentru ambii jucatori in interfata grafica

    jucator_curent = 2 if jucator_curent == 1 else 1  # Schimbă jucătorul curent
    player_turn_label.config(text=f"Este rândul lui {nume_jucator1 if jucator_curent == 1 else nume_jucator2}")
    # actualizeaza interfata grafica pentru a afisa mereu al cui este randul


def start_game():
    global punctaj_total_jucator1
    global punctaj_total_jucator2
    global formatii_realizate_jucator1
    global formatii_realizate_jucator2
    global formatii_disponibile
    global input_box
    global punctaj_label
    global formatii_label
    global player_turn_label
    global jucator_curent
    # parametrii globali pentru usurinta folosirii in mai multe functii

    punctaj_total_jucator1 = 0 #parametru pentru punctajul total initializat cu 0
    punctaj_total_jucator2 = 0
    formatii_realizate_jucator1 = []
    formatii_realizate_jucator2 = [] #liste goale pentru ambii jucatori care ajuta la memorarea formatiilor realizate
    formatii_disponibile = ["1", "2", "3", "4", "5", "6", "mici", "mari", "pare", "impare", "duble", "triple", "suita",
                            "care", "cameron"]
    # formatiile disponibile pentru acestia
    jucator_curent = 1 #primul jucator incepe jocul

    global root  #variabila globala pentru a putea fi folosita in toate functiile
    root = tk.Tk()
    root.title("Cameroon")

    root.geometry("500x400")
    root.configure(bg="#fff176")

    title_font = ("Helvetica", 18, "bold")
    label_font = ("Helvetica", 12)
    button_font = ("Helvetica", 12, "bold")

    title_color = "#283593"
    bg_color = "#fff176"
    input_bg_color = "#fff9c4"
    button_bg_color = "#f57f17"
    button_fg_color = "white"
    label_bg_color = bg_color

    title_label = tk.Label(root, text="Cameroon", font=title_font, fg=title_color, bg=bg_color)
    title_label.pack(pady=20)

    input_frame = tk.Frame(root, bg=bg_color)
    input_frame.pack(pady=10)

    input_label = tk.Label(input_frame, text="Alegeți o formă disponibilă sau renunțați:", font=label_font,
                           bg=label_bg_color)
    input_label.pack(side=tk.LEFT, padx=5)

    input_box = tk.Entry(input_frame, bg=input_bg_color)
    input_box.pack(side=tk.LEFT)

    arunca_button = tk.Button(root, text="Aruncă zarurile și calculează", command=arunca_zaruri_si_calculeaza,
                              bg=button_bg_color, fg=button_fg_color, font=button_font)
    arunca_button.pack(pady=10)

    punctaj_label = tk.Label(root,
                             text=f"Punctaj {nume_jucator1}: {punctaj_total_jucator1}    Punctaj {nume_jucator2}: {punctaj_total_jucator2}",
                             font=label_font, bg=label_bg_color)
    punctaj_label.pack(pady=5)

    formatii_label = tk.Label(root,
                              text=f"Formații realizate: {nume_jucator1}: {', '.join(formatii_realizate_jucator1)} | {nume_jucator2}: {', '.join(formatii_realizate_jucator2)}",
                              font=label_font, bg=label_bg_color)
    formatii_label.pack(pady=5)

    player_turn_label = tk.Label(root, text=f"Este rândul lui {nume_jucator1}", font=label_font, bg=label_bg_color)
    player_turn_label.pack(pady=10)

    root.mainloop()


def main_menu(): #facem aceasta functie pentru a avea acees la doua campuri de introducere a jucatorilor
    global root  #variabila globala pentru usurinta de a fi folosita in alte functii
    root = tk.Tk() #creeaza fereastra interfetei cu ajutorul Tkinter
    root.title("Cameroon - Start") #seteaza titlul ferestrei de interfata

    root.geometry("500x400") #seteaza dimensiunea ferestrei
    root.configure(bg="#fff176") #seteaza culoarea ferestrei

    title_font = ("Helvetica", 18, "bold") #se defineste fontul, dimensiunea si stilul titlului
    label_font = ("Helvetica", 12) #defineste fontul si dimensiunea etichetelor
    button_font = ("Helvetica", 12, "bold") #defineste fontul,dimensiunea si stilul titlului

    title_color = "#283593"
    bg_color = "#fff176"
    input_bg_color = "#fff9c4"
    button_bg_color = "#f57f17"
    button_fg_color = "white"
    # se definesc culorile titlului, butonului,etichetelor

    title_label = tk.Label(root, text="Cameroon", font=title_font, fg=title_color, bg=bg_color)
    title_label.pack(pady=20)
    # creeaza eticheta Cameroon cu specificatiile oferite mai sus

    name_label1 = tk.Label(root, text="Introduceți numele jucătorului 1:", font=label_font, bg=bg_color)
    name_label1.pack(pady=10)
    # creeaza eticheta de introducere a primului jucator

    global name_entry1 #defineste parametrul name_entry1 ca sa poata fi accesat si in alte functii
    name_entry1 = tk.Entry(root, font=label_font, bg=input_bg_color)
    name_entry1.pack(pady=5)
    # creeaza caseta pentru a introduce numele primul jucator

    name_label2 = tk.Label(root, text="Introduceți numele jucătorului 2:", font=label_font, bg=bg_color)
    name_label2.pack(pady=10)
    # creeaza eticheta de introducere a celui de al doilea jucator

    global name_entry2
    name_entry2 = tk.Entry(root, font=label_font, bg=input_bg_color)
    name_entry2.pack(pady=5)
    # creeaza caseta pentru a introduce numele celui de al doilea jucator

    start_button = tk.Button(root, text="Start joc", command=interfata_principala, bg=button_bg_color, fg=button_fg_color,
                             font=button_font)
    start_button.pack(pady=20)#creem un buton care atunci cand este apasat va apela functia pentru introducere numelor celor doi jucatori

    root.mainloop()#bucla interfetei care permite interactiunea si afisarea continutului acesteia


def interfata_principala():#definirea functie care este apelata atunci cand utilizatorul apasa butonul
    global nume_jucator1
    global nume_jucator2
    nume_jucator1 = name_entry1.get() #se apeleaza parametrii globali din functia de mai sus si se paseaza numele
    nume_jucator2 = name_entry2.get()
    if nume_jucator1 and nume_jucator2: #daca numele sunt valide atunci meniul principal din interfata dispare si se va incepe jocul
        root.destroy()
        start_game()
    else:
        messagebox.showinfo("Eroare", "Vă rugăm să introduceți numele ambilor jucători.")
#altfel interfata va pasa automat un text de eroare si solicitarea unui nume valid

main_menu() #se afiseaza interfata grafica principala la rularea codului
