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