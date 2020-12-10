__author__ = "Dieter Demuynck" + " & " + "Rayan Verheecke"
"""
Practicum 2 voor Beginselen van Programmeren
"""


class Magazijn:
    def __init__(self, producttypes, aantal = 0):
        self._producttypes[producttype] = 0
        self._aantal[] = aantal

    def getAantal(self):
        return self._aantal
    def getProducttypes(self):
        return self._producttypes


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
    def __init__(self, naam, klant_id):
        self._naam = naam
        self._klant_id = klant_id


class Bestelling:
    def __init__(self, aantal, producttype):
        self._aantal = aantal
        self._producttype = producttype
