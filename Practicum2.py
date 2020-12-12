__author__ = "Dieter Demuynck" + " & " + "Rayan Verheecke"
"""
Practicum 2 voor Beginselen van Programmeren
"""


class Magazijn:
    def __init__(self):
        self._producttypes = {}

    def getProducttypes(self):
        return self._producttypes

    def nieuw_producttype(self, producttype):
        if producttype not in self._producttypes:
            self._producttypes[producttype] = 0

    def add_producten(self, producttype, aantal):
        self._producttypes[producttype] += aantal

    def verwerk_bestelling(self, bestelling):
        product_type = bestelling.get_producttype()
        bestel_aantal = bestelling.get_aantal()
        stock_aantal = self._producttypes[product_type]

        # Bestelling kan zonder problemen doorgaan, er is genoeg in voorraad
        if bestel_aantal <= stock_aantal:
            self._producttypes[product_type] -= bestel_aantal

        # Als besteld aantal groter dan aantal in voorraad:
        # -- OPTIE 1 --
        # Stop de bestelling
        else:
            raise ValueError(f"Besteld aantal ({bestel_aantal}) is groter dan aantal in voorraad ({stock_aantal})")

        # -- OPTIE 2 --
        # Trek van de bestelling het aantal in voorraad af, stock wordt 0
        #
        # if bestel_aantal > stock_aantal:
        #     bestelling.set_aantal(bestel_aantal - stock_aantal)
        #     self._producttypes[product_type] = 0

    def verkoopwaarde_product(self, producttype):
        return self._producttypes[producttype] * producttype.getverkoopPrijs()

    def _aankoopwaarde_product(self, producttype):
        return self._producttypes[producttype] * producttype.getaankoopPrijs()

    def verkoopwaarde_stock(self):
        totale_prijs = 0
        for product, aantal in self._producttypes.items():
            totale_prijs += aantal * product.getverkoopPrijs()
        return totale_prijs

    def _aankoopwaarde_stock(self):  # interne functie voor winst te bepalen
        totale_prijs = 0
        for product, aantal in self._producttypes.items():
            totale_prijs += aantal * product.getaankoopPrijs()
        return totale_prijs

    def verkoopwaarde(self, producttype=None):
        if producttype is None:
            return self.verkoopwaarde_stock()
        return self.verkoopwaarde_product(producttype)

    def _aankoopwaarde(self, producttype=None):
        if producttype is None:
            return self._aankoopwaarde_stock()
        return self._aankoopwaarde_product(producttype)

    def winst(self, producttype=None):
        """
        Berekent de winst van een bepaald producttype als deze is opgegeven.
        Als het producttype niet werd opgegeven (is None), berekent de functie de winst van alle producten in voorraad.
        :param producttype: het producttype waarvan de mogelijke winst wordt berekend
        :return: de mogelijke winst van alle producten (van het gegeven producttype) in voorraad
        """
        if producttype is None:
            return self.verkoopwaarde_stock() - self._aankoopwaarde_stock()
        return self.verkoopwaarde_product(producttype) - self._aankoopwaarde_product(producttype)

    def _info_product(self, producttype):
        # initialise message var
        message = ""

        # add info
        message += f"Producttype: {producttype.getNaam():>20}\n"
        message += f"Aankoopprijs: {producttype.getaankoopPrijs():>17.2f} €\n"
        message += f"verkoopprijs: {producttype.getverkoopPrijs():>17.2f} €\n"
        message += f"Aantal in stock: {self._producttypes[producttype]:>16d}"

        print(message)

    def _info_stock(self):
        # Uitleg tabel
        line_1 = f"{'Producttype':<20} | aankoopprijs | verkoopprijs | {'aantal':>6}"
        seperator = "\n" + "-" * len(line_1)
        print(line_1 + seperator)

        # Werkelijke info, gebruik de __str__ functie van ProductType
        for producttype, aantal in self._producttypes.items():
            print(f"{str(producttype)} | {aantal:>6d}")

    def informatie(self, producttype=None):
        if producttype is None:
            self._info_stock()
        else:
            self._info_product(producttype)


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
    klant_id = 0

    def __init__(self, naam):
        self._naam = naam
        self._klant_id = Klant.klant_id
        Klant.klant_id += 1

    def getNaam(self):
        return self._naam

    def getId(self):
        return self._klant_id


class Bestelling:
    def __init__(self, producttype, aantal):
        self._aantal = aantal
        self._producttype = producttype

    def get_aantal(self):
        return self._aantal

    def get_producttype(self):
        return self._producttype


def simulatie():
    """
    De functie simulatie() simuleert het gebruik van de aangemaakte klassen en hun functies.
    """
    pass

