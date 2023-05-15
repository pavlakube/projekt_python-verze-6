from unittest import TestCase
from insurance_administration import InsuranceAdministration, Record

class TestInsuranceAdministration(TestCase):
    def test_create_record(self):
        insurance_administration = InsuranceAdministration()

        # Testování vytvoření záznamu
        insurance_administration.create_record()

        # Ověření, zda byl záznam přidán do evidence
        self.assertEqual(len(insurance_administration.records), 1)
        self.assertIsInstance(insurance_administration.records[0], Record)

    def test_find_record(self):
        insurance_administration = InsuranceAdministration()

        # Přidáme záznam pro testování
        record = Record("John", "Doe", 30, "123456789")
        insurance_administration.records.append(record)
        insurance_administration.connection.execute(
            "INSERT INTO insured_persons (name, surname, age, phone_number) VALUES (?, ?, ?, ?)",
            (record._name, record._surname, record._age, record._phone)
        )
        insurance_administration.connection.commit()

        # Vyhledáme existující záznam
        insurance_administration.find_record()
        # Otestujeme výstup
        expected_output = f"Hledaný pojištěnec: {record}\n\n"
        self.assertEqual(expected_output, self.stdout.getvalue())

        # Vyhledáme neexistující záznam
        insurance_administration.find_record()
        # Otestujeme výstup
        expected_output = "Hledaný pojištěnec nebyl nalezen.\n\n"
        self.assertEqual(expected_output, self.stdout.getvalue())