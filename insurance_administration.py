from record import Record
import sqlite3
# třída pro Správu pojišťovny
class InsuranceAdministration:

    def __init__(self):
        self.records = []

        # propojení do databáze
        try:
           self.connection = sqlite3.connect("insurance_records.db")
        except Exception as e:
            print("Chyba při otevírání databáze", e)
        self.cursor = self.connection.cursor()
        self.connection.commit()

    # metoda pro vytvoření záznamu pojištěnce
    def create_record(self):
        while True:
            name = input("Zadejte jméno: ").strip()
            # vrací True, pokud abeced. znaky a pokud neprázdné
            if name.isalpha() and name:
                break
            print("Jméno může obsahovat pouze písmena.")
        while True:
            surname = input("Zadejte příjmení: ").strip()
            if surname.isalpha() and surname:
                break
            print("Příjmení může obsahovat pouze písmena.")
        while True:
            age = input("Zadejte věk: ")
            try:
                age = int(age)
                if 0 <= age <= 150:
                    break
                else:
                    print("Věk pro naše pojištěnce musí být max 150 let.")
            except ValueError:
                print("Věk musí být číslo, zkuste zadat znovu.")
        while True:
            phone = input("Zadejte telefonní číslo: ")
            if phone.isdigit() and len(phone) == 9:
                break
            else:
                print("Číslo musí obsahovat 9 číslic.")
        new_record = Record(name, surname, age, phone)
        self.records.append(new_record)
        self.connection.execute("INSERT INTO insured_persons"
                                "(name, surname, age, phone_number) "
                                "VALUES (?, ?, ?, ?)",
                                (name, surname, age, phone))
        self.connection.commit()
        print(f"Nový záznam byl přidán do evidence.\n")

    # pro výpis všech pojištěnců
    def get_all_records(self):
        print("Výpis všech pojištěnců:")
        self.cursor.execute("SELECT *"
                                " FROM insured_persons")
        rows = self.cursor.fetchall()
        # pro aktualizaci seznamu records před operací výpis
        self.records = []
        for row in rows:
            user_id, name, surname, age, phone = row
            record = Record(name, surname, age, phone)
            self.records.append(record)
            print(record)
        print()

    def find_record(self):
        while True:
            name_and_surname = input("Zadejte jméno a příjmení pojištěnce:")
            if " " in name_and_surname:
                name, surname = name_and_surname.split(" ")
                if name.isalpha() and surname.isalpha():
                    break
                else:
                    print("Jméno a příjmení mohou obsahovat pouze písmena.")
            print("Jméno a příjmení musí být odděleny mezerou.")
        self.cursor.execute("SELECT * FROM insured_persons WHERE name=? "
                            "AND surname=?", (name, surname))
        row = self.cursor.fetchone()
        # kontroluje, zda se nevrátil prázdný záznam
        if row:
            # rozbalí hodnoty z řádku databáze do proměnných
            user_id, name, surname, age, phone = row
            # vytvoří nový objekt -> hledaného pojištěnce
            record = Record(name, surname, age, phone)
            print("Hledaný pojištěnec: ", record, "\n")
        else:
            print("Hledaný pojištěnec nebyl nalezen.\n")
        print()
