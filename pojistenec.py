class Pojistenec:

    # metoda pro iniciaci pojištěnce
    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    # metoda pro výpis pojištěnce
    def __str__(self):
        return f"{self.jmeno}\t{self.prijmeni}\t{self.vek}\t\t{self.tel_cislo}"

