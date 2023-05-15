from insurance_administration import InsuranceAdministration

insurance_administration = InsuranceAdministration()

print("\n-------------------------------")
print("Evidence pojištěných osob")
print("-------------------------------\n")

start_menu = True
while start_menu:
    print("1 - Přidat nového pojištěnce")
    print("2 - Vypsat všechny pojištěnce")
    print("3 - Vyhledat pojištěnce")
    print("4 - Konec")

    # výběr z menu
    menu_selection = input("Kterou možnost chcete zvolit? Zadejte číslo: ")
    if menu_selection == "1":
        print("\nZvolil jste možnost přidat záznam.")
        insurance_administration.create_record()
    elif menu_selection == "2":
        print("\nZvolil jsi možnost vypsat všechny pojištěnce.")
        insurance_administration.get_all_records()
    elif menu_selection == "3":
        print("\nZvolil jsi možnost vyhledat pojištěnce")
        insurance_administration.find_record()
    elif menu_selection == "4":
        print("\nDěkuji a nashledanou!")
        input("")
        start_menu = False
    else:
        print("Neplatná volba, zadejte číslo dle nabídky.\n")
        start_menu = True
pass
