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


class Klant:
    # from random import randint
    # klant_id = randint(0, 999999)

    # Is er geen betere manier om dit "veiliger" te maken?
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
    def __init__(self, aantal, producttype):
        self._aantal = aantal
        self._producttype = producttype
