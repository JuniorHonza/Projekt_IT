import databaze

MENU = """
-----------------------------
EVIDENCE POJIŠTĚNÝCH KLIENTŮ
-----------------------------
Vyberte činnost, kterou chcete udělat:
1 - Přidat nového klienta
2 - Vypsat všechny pojištěné klienty
3 - Vyhledat pojištěnce
4 - Vymazat pojištěnce
5 - Ukončení aplikace

Zadejte číslo akce:"""


def menu():
    connection = databaze.connect()
    databaze.vytvoreni_tabulky(connection)

    while (user_input := input(MENU)) != "5":
        if user_input == "1":
            Jmeno = input("Zadejte jméno pojištěného:\n")
            Prijmeni = input("Zadejte příjmení pojištěného:\n")
            Vek = int(input("Zadejte věk pojištěného:\n"))
            Telefoni_cislo = int(input("Zadejte telefonní číslo:\n +420"))

            databaze.pridani_noveho_pojisteneho(connection, Jmeno, Prijmeni, Vek, Telefoni_cislo)

            input("Data byla uložena, pokračujte libovolnou klavesou...")
            continue

        elif user_input == "2":
            pojisteni = databaze.vypsani_seznamu_pojistenych(connection)

            for pojisteny in pojisteni:
                print(f"{pojisteny[0]} {pojisteny[1]} {pojisteny[2]} {pojisteny[3]} {pojisteny[4]}")

            input(
                "Zde vidíte výpis pojištěných. Pokud se žádná data nevypsala, žádný pojištěný zde není. Pokračujte libovolnou klavesou...")
            continue


        elif user_input == "3":
            Jmeno = input("Zadej jméno pojištěného:\n")
            Prijmeni = input("Zadej příjmení pojištěného:\n")
            pojisteni = databaze.vyhledani_pojisteneho_podle_jmena_a_prijimeni(connection, Jmeno, Prijmeni)

            pojisteny = False
            for pojisteny in pojisteni:
                if pojisteny in pojisteni:
                    pojisteni = True
            if pojisteni:
                print(f"{pojisteny[0]} {pojisteny[1]} {pojisteny[2]} {pojisteny[3]} {pojisteny[4]}")
                input("Pojištěný nalezen, pokračujte libovolnou klavesou...")
            else:
                input("Pojištěný nenalezen! Pokračujte libovolnou klavesou...")
                continue

        elif user_input == "4":
            Jmeno = input("Zadej jméno pojištěného:\n")
            Prijmeni = input("Zadej příjmení pojištěného:\n")
            pojisteni = databaze.vymazani_pojisteneho_podle_jmena_a_prijimeni(connection, Jmeno, Prijmeni)

            pojisteny = False
            for pojisteny in pojisteni:
                if pojisteny in pojisteni:
                    pojisteni = True

            input(
                "Pojištěný byl z databáze vymazán! Pokračujte libovolnou klavesou...")
            continue

        elif user_input == "5":
            pass

        else:
            input("Zadáno špatné číslo, zkuste to znovu, prosím! Pokračujte libovolnou klávesou...")
        continue


menu()