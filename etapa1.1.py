def main():
    nume_jucator = input("Introduceți numele jucătorului: ")
    formatii_disponibile = ["1", "2", "3", "4", "5", "6", "mici", "mari", "pare", "impare", "duble", "triple", "suită", "caré", "cameron"]
    formatii_realizate = []
    punctaj_total = 0

    for _ in range(15):
        input("Apăsați ENTER pentru a arunca zarurile...")
        zaruri = aruncare_zaruri()
        print("Zarurile aruncate sunt:", zaruri)

        formatie_aleasa = input("Alegeți o formație disponibilă sau renunțați (scrieți 'renunta'): ").lower()

        if formatie_aleasa == "renunta":
            print("Ai renunțat la această formație.")
            punctaj_total -= 3
        elif formatie_aleasa in formatii_disponibile:
            punctaj_formatie = calculeaza_punctaj(zaruri, formatie_aleasa)
            print("Punctajul pentru formația", formatie_aleasa, "este:", punctaj_formatie)
            punctaj_total += punctaj_formatie
            formatii_realizate.append(formatie_aleasa)
            formatii_disponibile.remove(formatie_aleasa)
        else:
            print("Formație invalidă!")

    if len(formatii_realizate) == 15:
        punctaj_total += 20
        print("Felicitări, ai completat toate formațiile și ai primit un bonus de 20 de puncte!")

    print("Jocul s-a încheiat. Punctaj total:", punctaj_total)

if __name__ == "__main__":
    main()