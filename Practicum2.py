__author__ = "Dieter Demuynck" + " & " + "Rayan Verheecke"
"""
Practicum 2 voor Beginselen van Programmeren
"""


class Magazijn:
    pass


class ProductType:
    pass


class Klant:
    def __init__(self, naam, klant_id):
        self._naam = naam
        self._klant_id = klant_id


class Bestelling:
    def __init__(self, aantal, producttype):
        self._aantal = aantal
        self._producttype = producttype
