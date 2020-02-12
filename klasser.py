"""Super-klasse kaldet 'Maeriale'."""
"""Klassen indeholder en 'toString'-methode der konverterer outputtet af parametrerne til datatypen 'String'."""
class Materiale (object):
    def __init__(self, idnr, title, antal, antaludlaan, aarstal, type):
        self.idnr = idnr
        self.title = title
        self.antal = antal
        self.antaludlaan = antaludlaan
        self.aarstal = aarstal
        self.type = type

    def toString(self):
        return str(self.idnr) + "\t\t" + str(self.title) + "\t\t" + str(self.antal) + "\t\t" + str(self.antaludlaan) + "\t\t" + str(self.aarstal) + "\t\t" + str(self.type)


"""Sub-klasse kaldet 'Bog', der arver fra Super-klassen 'Materiale."""
""" Denne klasse indeholder yderligere to parametrer ('antalsider' og 'forfatter')."""
"""Klassen indeholder ligeledes en 'toString'-funktion, der overskriver den 'toString'-funktion der findes i Super-Klassen."""
class Bog (Materiale):
    def __init__(self, idnr, title, antal, antaludlaan, aarstal, type, antalsider, forfatter):
        super().__init__(idnr, title, antal, antaludlaan, aarstal, type)
        self.antalsider = antalsider
        self.forfatter = forfatter

    def toString(self):
        return str(self.idnr) + "\t" + str(self.title) + "\t\t\t" + str(self.type) + "\t\t" + str(self.aarstal)



"""Sub-klasse kaldet 'Bog', der arver fra Super-klassen 'Materiale."""
""" Denne klasse indeholder yderligere to parametrer ('instruktør' og 'laengde')."""
"""Klassen indeholder ligeledes en 'toString'-funktion, der overskriver den 'toString'-funktion der findes i Super-Klassen."""
class Film (Materiale):
    def __init__(self, idnr, title, antal, antaludlaan, aarstal, type, instruktor, laengde):
            super().__init__(idnr, title, antal, antaludlaan, aarstal, type)
            self.instroktor = instruktor
            self.laengde = laengde

    def toString(self):
        return str(self.idnr) + "\t" + str(self.title) + "\t\t\t" + str(self.type) + "\t\t" + str(self.aarstal)


"""Sub-klasse kaldet 'Bog', der arver fra Super-klassen 'Materiale."""
""" Denne klasse indeholder yderligere to parametrer ('genre' og 'kunstner')."""
"""Klassen indeholder ligeledes en 'toString'-funktion, der overskriver den 'toString'-funktion der findes i Super-Klassen."""
class CD (Materiale):
    def __init__(self, idnr, title, antal, antaludlaan, aarstal, type, genre, kunstner):
            super().__init__(idnr, title, antal, antaludlaan, aarstal, type)
            self.genre = genre
            self.kunstner = kunstner

    def toString(self):
        return str(self.idnr) + "\t" + str(self.title) + "\t\t\t" + str(self.type) + "\t\t" + str(self.aarstal)


"""Sub-klasse kaldet 'Bog', der arver fra Super-klassen 'Materiale."""
""" Denne klasse indeholder yderligere to parametrer ('kategori' og 'udgiver')."""
"""Klassen indeholder ligeledes en 'toString'-funktion, der overskriver den 'toString'-funktion der findes i Super-Klassen."""
class Video_spil (Materiale):
    def __init__(self, idnr, title, antal, antaludlaan, aarstal, type, kategori, udgiver):
            super().__init__(idnr, title, antal, antaludlaan, aarstal, type)
            self.kategori = kategori
            self.udgiver = udgiver

    def toString(self):
        return str(self.idnr) + "\t" + str(self.title) + "\t\t\t" + str(self.type) + "\t\t" + str(self.aarstal)