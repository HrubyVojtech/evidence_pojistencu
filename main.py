from pojistenec import Pojistenec
from databaze import Databaze

#funkce pro bezchybné zadání jména
def validace_jmena(jmeno):
    if not jmeno.isalpha():
        raise ValueError("Chyba!, Jméno musí obsahovat pouze písmena.")

#funkce pro bezchybné zadání věku
def validace_veku(vek):
    if not vek.isdigit():
        raise ValueError("Chyba! Věk musí být číslo.")
    if int(vek) <= 0 or int(vek) >= 130:
        raise ValueError("Chyba! Věk musí být v rozmezí 0 až 130 let.")

#funkce pro bezchybné zadání telefonního čísla
def validace_tel_cisla(tel_cislo):
    tel_cislo_bez_mezer = tel_cislo.replace(" ", "")
    if not tel_cislo_bez_mezer.replace("+", "").isdigit():
        raise ValueError("Chyba! Telefonní číslo musí obsahovat pouze čísla a znak '+'.")

data = Databaze() # instance pro vytvoření databáze


while True:     # Dokud se program neukončí, zobrazí se vždy tento výpis
    print("_____________________________\nEvidence pojištěných\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    volba = int(input("Vyberte si akci:\n"
                "1 - Přidat nového pojištěného\n"
                "2 - Vypsat všechny pojištěné\n"
                "3 - Vyhledat pojištěného\n"
                "4 - Konec\n"))
    if volba == 1:      # Pokud je volba uživatele 1, je vyzván k zadání jména, příjmení, věku a telefonního čísla
        while True:
            jmeno = input("Zadejte jméno pojištěného: ").strip().capitalize()
            try:
                validace_jmena(jmeno)
                break
            except ValueError as e:
                print(e)

        while True:
            prijmeni = input("Zadejte příjmení: ").strip().capitalize()
            try:
                validace_jmena(prijmeni)
                break
            except ValueError as e:
                print(e)

        while True:
            vek = input("Zadejte věk: ").strip()
            try:
                validace_veku(vek)
                break
            except ValueError as e:
                print(e)

        while True:
            tel_cislo = input("Zadejte telefonní číslo: ").strip()
            try:
                validace_tel_cisla(tel_cislo)
                break
            except ValueError as e:
                print(e)

        pojistenec = Pojistenec(jmeno, prijmeni, int(vek), tel_cislo)   # instance pojištěnce
        data.pridej_pojistence(pojistenec)      # volání instance data pro pridání pojištěnce do databáze
        print("\nPojištěnec přidán")        # výpis po úspěšném zadání nového pojištěnce
        input("Stiskněte libovolnou klávesu pro pokračování...")


    elif volba == 2:    # Pokud je volba uživatele 2, program navrátí výpis všech pojištěnců
        for pojistenec in data.get_seznam_pojistenych():
            print(str(pojistenec))
        input("Stiskněte libovolnou klávesu pro pokračování...")


    elif volba == 3:    # Pokud je volba uživatele 3, je vyzván k zadání jména a příjmení pro vyhledání konkrétního pojištěnce
        jmeno = input("Zadejte jméno pojisteného: ").strip().capitalize()
        prijmeni = input("Zadejte příjmení: ").strip().capitalize()
        pojistenec = data.najdi_pojistence(jmeno, prijmeni)
        if pojistenec == None:
            print("Nenalezeno")
        else:
            print(str(pojistenec))
        input("Stiskněte libovolnou klávesu pro pokračování...")


    elif volba == 4:    # Volba 4 ukončí program
        break

    else:
        print("Chyba! Zadej znovu.")    # Pokud je volba jiná než 1-4, uživatel je vyzván o opakování volby
