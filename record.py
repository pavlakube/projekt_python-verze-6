# třída reprezentuje jednotlivé záznamy pojištěnce
class Record:

    def __init__(self, name, surname, age, phone):
        self._name = name
        self._surname = surname
        self._age = age
        self._phone = phone
        self._record = [self._name, self._surname, self._age, self._phone]

    #metoda pro výpis záznamu
    def __str__(self):
        return f"Pojištěnec: {self._name} {self._surname}, věk: {self._age}, telefoní číslo: {self._phone}"