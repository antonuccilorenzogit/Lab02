def carica_da_file(file_path,biblioteca,libri):
    """Carica i libri dal file"""
    try:
        infile= open(file_path,'r')
        n= infile.readline().strip()
        for line in infile:
            libro= line.split(',')
            libri.append(libro)

        for n_sez in range(1,int(n)+1):
            if n_sez not in biblioteca.keys():
                biblioteca[n_sez]=[]
            for libro in libri:
                if int(libro[-1]) ==n_sez:
                    biblioteca[n_sez].append(libro)
        infile.close()
        return biblioteca

    except FileNotFoundError:
        return None


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""

    try:
        if sezione in biblioteca.keys():
            for libro in biblioteca[sezione]:
                if titolo == libro[0]:
                    return None
            biblioteca[sezione].append([titolo,autore,anno,pagine,sezione])
            infile= open(file_path,'a')
            infile.write(f'{titolo},{autore},{anno},{pagine},{sezione}\n')
            infile.close()
            return True
        else:
            return None
    except FileNotFoundError:
            return None


def cerca_libro(biblioteca, titolo,):
    Trovato= False
    for chiave in biblioteca.keys().list():
        for n in range(len(biblioteca[chiave])):
            if titolo == biblioteca[chiave][n][0]:
                return [biblioteca[chiave][n][0],biblioteca[chiave][n][1],biblioteca[chiave][n][2],biblioteca[chiave][n][3], chiave]
                Trovato= True
                break

    if not Trovato:
        return None


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    if sezione not in biblioteca.keys():
        return None
    else:
        return sorted(biblioteca[sezione],key=lambda x: x[0])

def main():

    file_path = "biblioteca.csv"

    biblioteca = {}
    libri = []

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path,biblioteca,libri)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

