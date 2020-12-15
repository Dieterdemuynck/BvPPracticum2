__author__ = "Dieter Demuynck" + " & " + "Rayan Verheecke"
"""
Practicum 2 voor Beginselen van Programmeren
"""


class Magazijn:
    def __init__(self):
        self._in_stock = {}  # dictionary voor producttypes in stock, gelinkt met hun aantal
        self._verkocht = {}  # dictionary voor producttypes, gelinkt met het verkochte aantal producten per type
        self._klantenlijst = []  # lijst van klanten

    def getProducttypes(self):
        return tuple(self._in_stock.keys())

    # ================================================================================================================
    # Initialisatie Methodes
    # ================================================================================================================

    def nieuwProducttype(self, naam, aankoopprijs, verkoopprijs):
        producttype = ProductType(naam, aankoopprijs, verkoopprijs)
        self._in_stock[producttype] = 0
        self._verkocht[producttype] = 0

        return producttype

    def nieuwKlant(self, naam):
        klant = Klant(naam)
        self._klantenlijst.append(klant)

        return klant

    def nieuwBestelling(self, klant, producttype, aantal):
        bestelling = klant.maak_bestelling(producttype, aantal)

        return bestelling

    # ----------------------------------------------------------------------------------------------------------------

    # Producten van bepaald type toevoegen
    def addProducten(self, producttype, aantal):
        self._in_stock[producttype] += aantal

    # Bestelling van een klant verwerken
    def verwerkBestelling(self, klant, bestelling):
        product_type = bestelling.get_producttype()
        bestel_aantal = bestelling.get_aantal()
        stock_aantal = self._in_stock[product_type]

        # Bestelling kan zonder problemen doorgaan, er is genoeg in voorraad
        if bestel_aantal <= stock_aantal:
            self._in_stock[product_type] -= bestel_aantal
            self._verkocht[product_type] += bestel_aantal
            klant.verwerkBestelling(bestelling)

        # Als besteld aantal groter dan aantal in voorraad:
        # -- OPTIE 1 --
        # Stop de bestelling
        else:
            print(f"Besteld aantal ({bestel_aantal}) is groter dan aantal in voorraad ({stock_aantal})")

        # -- OPTIE 2 --
        # Trek van de bestelling het aantal in voorraad af, stock wordt 0
        #
        # else:
        #     bestelling.set_aantal(bestel_aantal - stock_aantal)
        #     self._producttypes[product_type] = 0
        #     self._verkocht[product_type] += bestel_aantal - stock_aantal

    # ================================================================================================================
    # Aankoop- en verkoopwaarde Methodes
    # ================================================================================================================

    def _verkoopwaarde_product(self, producttype):
        return self._in_stock[producttype] * producttype.getverkoopPrijs()

    def _aankoopwaarde_product(self, producttype):
        return self._in_stock[producttype] * producttype.getaankoopPrijs()

    def _verkoopwaarde_stock(self):
        totale_prijs = 0
        for product, aantal in self._in_stock.items():
            totale_prijs += aantal * product.getverkoopPrijs()
        return totale_prijs

    def _aankoopwaarde_stock(self):  # interne functie voor winst te bepalen
        totale_prijs = 0
        for product, aantal in self._in_stock.items():
            totale_prijs += aantal * product.getaankoopPrijs()
        return totale_prijs

    def verkoopwaarde(self, producttype=None):
        if producttype is None:
            return self._verkoopwaarde_stock()
        return self._verkoopwaarde_product(producttype)

    def _aankoopwaarde(self, producttype=None):
        if producttype is None:
            return self._aankoopwaarde_stock()
        return self._aankoopwaarde_product(producttype)

    # ================================================================================================================
    # Winst Methodes
    # ================================================================================================================

    def _winst_product(self, producttype):
        return self._verkocht[producttype] * (producttype.getverkoopPrijs() - producttype.getaankoopPrijs())

    def _winst_stock(self):
        totale_winst = 0
        for producttype, aantal in self._verkocht.items():
            totale_winst += aantal * (producttype.getverkoopPrijs() - producttype.getaankoopPrijs())

        return totale_winst

    def winst(self, producttype=None):
        """
        Berekent de winst van een bepaald producttype als deze is opgegeven.
        Als het producttype niet werd opgegeven (is None), berekent de functie de winst van alle producten in voorraad.
        :param producttype: het producttype waarvan de opgebrachte winst wordt berekend
        :return: de opgebrachte winst van alle producten (van het opgegeven producttype)
        """
        if producttype is None:
            return self._winst_stock()
        return self._winst_product(producttype)

    # ================================================================================================================
    # Informatie Methodes
    # ================================================================================================================

    def _info_product(self, producttype):
        # initialise message var
        message = ""

        # add info
        message += f"Producttype: {producttype.getNaam():>20}\n"
        message += '-' * 33  # separator
        message += f"Aankoopprijs: {producttype.getaankoopPrijs():>17.2f} €\n"
        message += f"Verkoopprijs: {producttype.getverkoopPrijs():>17.2f} €\n"
        message += f"Aantal in stock: {self._in_stock[producttype]:>16d}\n"
        message += f"Verkoopwaarde stock: {self._verkoopwaarde_product(producttype):>9.2f} €"
        message += f"Aantal verkocht: {self._verkocht[producttype]:>16d}\n"
        message += f"Gemaakte winst: {self._winst_product(producttype):>15.2f} €"

        print(message)

    def _info_stock(self):
        # Uitleg tabel
        line_1 = f"{'Producttype':<20} | aankoopprijs | verkoopprijs | aantal"
        line_1 += " | verkoopwaarde stock | totale winst"
        seperator = "\n" + "-" * len(line_1)
        print(line_1 + seperator)

        # Werkelijke info, gebruik de __str__ functie van ProductType
        for producttype, aantal in self._in_stock.items():
            line = f"{str(producttype)} | {aantal:>6d} | {self.verkoopwaarde(producttype):19.2f}"
            line += f" | {self.winst(producttype):12.2f}"
            print(line)

        line_last = "-" * len(line_1) + "\n"
        line_last += f"Totale verkoopwaarde: {self._verkoopwaarde_stock():>13.2f} €\n"
        line_last += f"Totale winst: {self._winst_stock():>21.2f} €"

        print(line_last)

    def informatie(self, producttype=None):
        if producttype is None:
            self._info_stock()
        else:
            self._info_product(producttype)

    # ================================================================================================================
    # Data-Analyse Methodes (Opdracht 3)
    # ================================================================================================================

    def meestWinstgevend(self):
        """
        Berekend het meest winstgevend product tot nu toe, en hoeveel winst het heeft opgeleverd
        :return: een tuple met twee elementen: het producttype en de gemaakte winst
        """
        if len(self._verkocht) == 0:
            return None, 0

        originele_winst = list(self._verkocht.items())[0]
        for producttype, aantal in list(self._verkocht.items())[1:]:
            if aantal * self._winst_product(producttype) > originele_winst[1] * self._winst_product(originele_winst[0]):
                originele_winst = (producttype, aantal)

        return originele_winst[0], self._winst_product(originele_winst[0])

    def meestGespendeerd(self):
        klant_winst_koppel = (None, 0)
        for klant in self._klantenlijst:
            besteld = klant.getVerwerkteBestellingen()

            winst_opgeleverd = 0
            for bestelling in besteld:
                winst_opgeleverd += bestelling.bereken_winst()

            if winst_opgeleverd > klant_winst_koppel[1]:
                klant_winst_koppel = (klant, winst_opgeleverd)

        return klant_winst_koppel


class ProductType:
    def __init__(self, naam, aankoopprijs, verkoopprijs):
        self._naam = naam
        self._aankoopprijs = aankoopprijs
        self._verkoopprijs = verkoopprijs

    def getNaam(self):
        return self._naam

    def getaankoopPrijs(self):
        return self._aankoopprijs

    def getverkoopPrijs(self):
        return self._verkoopprijs

    def __repr__(self):
        return f"{self._naam}:({self._aankoopprijs}, {self._verkoopprijs})"

    def __str__(self):
        # constante waarden voor de lay-out van de string
        naam_len = 20

        # naam aanpassen als de lengte te groot is
        if len(self._naam) > naam_len:
            naam = self._naam[:naam_len - 2] + ".."
        else:
            naam = self._naam

        # return de (aangepaste) naam, samen met aankoopprijs en verkoopprijs
        return f"{naam:{naam_len}s} | {self._aankoopprijs:12.2f} | {self._verkoopprijs:12.2f}"


class Klant:
    # Een mogelijks veiligere manier voor het aanmaken van een ID-nummer
    # from random import randint
    # klant_id = randint(0, 999999)

    # Note: Een incrementele manier om een ID-nummer aan te maken is een groot veiligheidsrisico in de echte wereld.
    _klant_id = 0

    def __init__(self, naam):
        self._naam = naam
        self._bestellingen = []
        self._verwerkte_bestellingen = []
        self._klant_id = Klant._klant_id
        Klant._klant_id += 1

    def getNaam(self):
        return self._naam

    def getId(self):
        return self._klant_id

    def getBestellingen(self):
        return self._bestellingen

    def getVerwerkteBestellingen(self):
        return self._verwerkte_bestellingen

    def maak_bestelling(self, producttype, aantal):
        bestelling = Bestelling(producttype, aantal)
        self._bestellingen.append(bestelling)
        return bestelling

    def verwerkBestelling(self, bestelling):
        self._bestellingen.remove(bestelling)
        self._verwerkte_bestellingen.append(bestelling)

    def __repr__(self):
        return self._naam + f" [{self._klant_id:04d}]"


class Bestelling:
    def __init__(self, producttype, aantal):
        self._aantal = aantal
        self._producttype = producttype

    def get_aantal(self):
        return self._aantal

    def get_producttype(self):
        return self._producttype

    def bereken_winst(self):
        return (self._producttype.getverkoopPrijs() - self._producttype.getaankoopPrijs()) * self._aantal


def simulatie():
    """
    De functie simulatie() simuleert het gebruik van de aangemaakte klassen en hun functies.
    """
    print("Start van de simulatie.")
    # Stap 1: Maak een nieuw magazijn aan.
    print("1. Aanmaken nieuw magazijn")
    colruyt_magazijn = Magazijn()

    # Stap 2: Voeg 3 producttypes toe aan het magazijn.
    print("2. Toevoegen van producttypes appel, peer en banaan aan het magazijn")
    appel = colruyt_magazijn.nieuwProducttype("Appels", 1.0, 1.5)
    peer = colruyt_magazijn.nieuwProducttype("Peren", 1.5, 2.5)
    banaan = colruyt_magazijn.nieuwProducttype("Bananen", 0.5, 0.7)

    # Stap 3: Er worden 50 appels, 100 peren en 10 bananen geleverd
    print("3. Verwerken van leveringen van 50 appels, 100 peren en 10 bananen")
    colruyt_magazijn.addProducten(appel, 50)
    colruyt_magazijn.addProducten(peer, 100)
    colruyt_magazijn.addProducten(banaan, 10)

    # Stap 4: De magazijnmanager vraagt de verkoopwaarde van de appels op
    print("4. Verkoopwaarde appels opvragen")
    print("De verkoopwaarde van de huidige stock appels is:", colruyt_magazijn.verkoopwaarde(appel), "\n")

    # Stap 5: De magazijnmanager vraagt de verkoopwaarde van de volledige stock op
    print("5. Verkoopwaarde van de volledige stock opvragen")
    print("De verkoopwaarde van de volledige stock is:", colruyt_magazijn.verkoopwaarde(), "\n")

    # Stap 6: Maak 2 klanten aan
    print("6. Aanmaken van 2 klanten")
    klant1 = colruyt_magazijn.nieuwKlant("Klant 1")
    klant2 = colruyt_magazijn.nieuwKlant("Klant 2")

    # Stap 7: Klant 1 koopt 10 appels
    print("7. Klant 1 koopt 10 appels")
    bestelling1 = colruyt_magazijn.nieuwBestelling(klant1, appel, 10)
    colruyt_magazijn.verwerkBestelling(klant1, bestelling1)

    # Stap 8: Klant 2 koopt 5 peren
    print("8. Klant 2 koopt 5 peren")
    bestelling2 = colruyt_magazijn.nieuwBestelling(klant2, peer, 5)
    colruyt_magazijn.verwerkBestelling(klant2, bestelling2)

    # Stap 9: De magazijnmanager vraagt de gemaakte winst op appels op
    print("9. Totale winst op appels opvragen")
    print("Totale winst op appels: €", colruyt_magazijn.winst(appel), "\n")

    # Stap 10: De magazijnmanager vraagt de totale winst op
    print("10. Totale winst van de stock opvragen")
    print("Totale winst stock: €", colruyt_magazijn.winst(), "\n")

    # Stap 11, 12, 13: Klant 1 koopt 20 peren, maak een derde klant aan, klant 3 koopt 5 bananen
    print("11. Klant 1 koopt 20 peren")
    bestelling3 = colruyt_magazijn.nieuwBestelling(klant1, peer, 20)
    colruyt_magazijn.verwerkBestelling(klant1, bestelling3)

    print("12. Aanmaken van een derde klant")
    klant3 = colruyt_magazijn.nieuwKlant("Klant 3")

    print("13. Klant 3 bestelt 5 bananen")
    bestelling4 = colruyt_magazijn.nieuwBestelling(klant3, banaan, 5)
    colruyt_magazijn.verwerkBestelling(klant3, bestelling4)

    # Stap 14: De magazijnmanager vraagt de magazijninfo op
    print("14. Printen van alle info over het magazijn")
    colruyt_magazijn.informatie()

    # Stap 15: De magazijnbeheerder vraagt het meest winstgevend producttype op
    print("15. Meest winstgevend producttype opvragen")
    producttype, winst = colruyt_magazijn.meestWinstgevend()
    print(f"Het meest winstgevend product {producttype.getNaam()} heeft {winst:.2f} € opgebracht.")

    # Stap 16: De magazijnbeheerder vraagt de meest winstgevend klant op
    print("16. Meest winstgevende klant opvragen")
    klant, winst = colruyt_magazijn.meestGespendeerd()
    print(f"De meest winstgevende klant {klant.getNaam()} heeft {winst:.2f} € opgebracht.")


simulatie()
