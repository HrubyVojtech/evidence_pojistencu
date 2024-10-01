class Databaze:

    # list do kterého se ukládají přidaní pojištěnci
    def __init__(self):
        self._seznam_pojistenych = []

    # metoda pro přidání pojištěnce
    def pridej_pojistence(self, pojistenec):
        #print(f"insert into pojistenci ({pojistenec.jmeno}, {pojistenec.prijmeni}, {pojistenec.vek}, {pojistenec.tel_cislo})")
        self._seznam_pojistenych.append(pojistenec)

    # metoda pro výpis seznamu pojištěnců
    def get_seznam_pojistenych(self):
        return self._seznam_pojistenych

    # metoda pro výpis konkrétního pojištěnce podle jména a příjmení
    def najdi_pojistence(self, jmeno, prijmeni):
        for pojistenec in self._seznam_pojistenych:
            if jmeno == pojistenec.jmeno and prijmeni == pojistenec.prijmeni:
                return (pojistenec)
            return None