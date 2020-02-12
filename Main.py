from tkinter import *

"""Her importeres de ønskede Klasser fra modulet 'klasser.py'."""
from klasser import Bog, Film, CD, Video_spil

"""Initialisering af hvert unikt objekt vi skaber til vores system."""
"""Objekterne skabes ved at oprette et nyt variabelnavn, for efterfølgende at"""
"""associere dem med en Klasse, samt definerer de dertilhørende parametrer for denne klasse."""

bog1 = Bog("1", "Serpent Of Darkness", int(10), int(4), int(1818), "Bog", int(800), "Elizabeth Doyle",)
bog2 = Bog("2", "Human Of Freedom", int(7), int(2), int(1921), "Bog", int(250), "Jessica Pratt",)
bog3 = Bog("3", "Curse Of Water", int(35), int(1), int(2001), "Bog", int(120), "Melissa Villegas",)

film1 = Film("4", "Priests And Heroes", int(3), int(3), int(2007), "Film", "Jennifer Scott", int(120),)
film2 = Film("5", "Traitors And Guardians", int(8), int(1), int(1983), "Film", "Heather Barnes", int(180),)
film3 = Film("6", "Women Of The Ancients", int(6), int(2), int(1992), "Film", "Amanda Serrano", int(90),)

cd1 = CD("7", "Rastaman Vibration", int(4), int(1), int(1976), "CD", "Reggae", "Bob Marley",)
cd2 = CD("8", "Scorpion", int(20), int(15), int(2018), "CD", "Hip Hop", "Drake",)
cd3 = CD("9", "Point of Know Return", int(8), int(3), int(1977), "CD", "Rock", "Kansas",)

video_spil1 = Video_spil("10", "Fifa 2018", int(10), int(10), int(2018), "Videospil", "Sport", "Electronic Arts",)
video_spil2 = Video_spil("11", "Far Cry 5", int(5), int(2), int(2019), "Videospil", "Adventure", "Ubisoft",)
video_spil3 = Video_spil("12", "Cyberpunkt 2077", int(1), int(0), int(2020), "Videospil", "RPG", "CD Project Red",)



"""Listen der indeholder alle de objekter der findes i systemet."""
listMaterialer = [bog1, bog2, bog3, film1, film2, film3, cd1, cd2, cd3,video_spil1, video_spil2, video_spil3]

class Application(Frame):

    """Funktion der tillader brugeren at låne et lånte materiale, ved indput af ID-nummer."""
    def udlaan(self):
        self.listGui.delete('1.0', END)
        idnr = self.id_entry.get()
        print("Følgende ID ønskes udlånt: " + idnr)
        for materiale in listMaterialer:
            if idnr == materiale.idnr:
                if materiale.antal > materiale.antaludlaan:
                    materiale.antaludlaan += 1
                    self.listGui.insert(INSERT, "Du har nu lånt " + materiale.title + "\n")
                else:
                    self.listGui.insert(INSERT,"Beklager. Alle eksemplarer af " + materiale.title + " er udlånte" + "\n")
                return
        self.listGui.insert(INSERT, "Beklager. Dette er eksemplar er ikke vores")


    """Funktion der tillader brugeren at aflevere et lånte materiale, ved indput af ID-nummer."""
    def aflever(self):
        self.listGui.delete('1.0', END)
        idnr = self.aflever_entry.get()
        print("Følgende ID ønskes afleveret: " + idnr)
        for materiale in listMaterialer:
            if idnr == materiale.idnr:
                if materiale.antaludlaan == 0:
                    self.listGui.insert(INSERT, "Beklager. Dette er eksemplar er ikke vores" + "\n")
                else:
                    materiale.antaludlaan -= 1
                    self.listGui.insert(INSERT, "Du har nu afleveret " + materiale.title + "\n")
                return
        self.listGui.insert(INSERT, "Beklager. Dette materiale findes ikke")


    """Funktion der tillader brugeren at fremsøge materiale i listen af alle materialer."""
    """Brugeren kan enten søge på titel, ID-nummer eller type af materiale."""
    def sog_i_listen(self):
        soegetekst = self.entry.get()
        print("Søger på tekst: " + soegetekst)
        soegning = []
        self.listGui.delete('1.0', END)
        for materiale in listMaterialer:
            if soegetekst.lower() in materiale.title.lower() or soegetekst.lower() in materiale.idnr.lower() \
                    or soegetekst.lower() in materiale.type.lower():
                soegning.append(materiale)
        if soegning:
            for materiale in soegning:
                self.listGui.insert(INSERT, materiale.toString() + "\n")
        else:
            self.listGui.insert(INSERT, "Beklager. Det ønskede materiale findes ikke" + "\n")


    """Funktion der tillader brugeren at se totallisten af alle materialer i systemet."""
    def vis_hele_listen(self):
        print("Hele listen vises nu:")
        self.listGui.delete('1.0', END)
        for materiale in listMaterialer:
            self.listGui.insert(INSERT, materiale.toString() + "\n")


    """Funktion der tillader brugeren at sorterer totallisten i alfabetisk orden."""
    def sorterstigende(self):
        self.listGui.delete('1.0', END)
        listMaterialer.sort(key=lambda x: x.title, reverse = False)
        for materiale in listMaterialer:
            self.listGui.insert(INSERT, materiale.toString() + "\n")

    """Funktion der tillader brugeren at sorterer totallisten i omvendt alfabetisk orden."""
    def sorterfaldende(self):
        self.listGui.delete('1.0', END)
        listMaterialer.sort(key=lambda x: x.title, reverse=True)
        for materiale in listMaterialer:
            self.listGui.insert(INSERT, materiale.toString() + "\n")


    def create_widgets(self):
        frame = Frame(self)
        self.winfo_toplevel().title("Biblioteks databasen")

        # definition af quit knap
        self.QUIT = Button(frame, text="QUIT")
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

        # definition og mapping af vis hele listen knappen
        self.visListe = Button(frame,text="Vis hele listen")
        self.visListe["command"] = self.vis_hele_listen
        self.visListe.pack({"side": "left"})

        # definition af input søge feltet.
        self.L1 = Label(frame, text="Søge Streng")
        self.L1.pack(side=LEFT)
        self.entry = Entry(frame, bd=5)
        self.entry.pack(side=LEFT)

        # definition og mapping af søgeknappen.
        self.sogKnap = Button(frame, text="Søg i listen")
        self.sogKnap["command"] = self.sog_i_listen
        self.sogKnap.pack({"side": "left"})

        # definition af ID input feltet til udlån
        self.L1 = Label(frame, text="ID for udlån")
        self.L1.pack(side=LEFT)
        self.id_entry = Entry(frame, bd=5)
        self.id_entry.pack(side=LEFT)

        # definition af udlåns knappen og mapping til
        # en funktion.
        self.udlaanKnap = Button(frame, text="Udlån")
        self.udlaanKnap["command"] = self.udlaan
        self.udlaanKnap.pack({"side": "left"})

        # input felt til aflevering.
        self.L1 = Label(frame, text="ID for aflevering:")
        self.L1.pack(side=LEFT)
        self.aflever_entry = Entry(frame, bd=5)
        self.aflever_entry.pack(side=LEFT)

        # definition og mapping af afleveringsknap
        self.afleverKnap = Button(frame, text="Aflever")
        self.afleverKnap["command"] = self.aflever
        self.afleverKnap.pack({"side": "left"})

        #definition og mapping af sorterstigendeknap
        self.sorterstigendeKnap = Button(frame, text="Sorter stigende")
        self.sorterstigendeKnap["command"] = self.sorterstigende
        self.sorterstigendeKnap.pack({"side": "left"})

        #definition og mapping af sorterfaldendeknap
        self.sorterfaldendeKnap = Button(frame, text="Sorter faldende")
        self.sorterfaldendeKnap["command"] = self.sorterfaldende
        self.sorterfaldendeKnap.pack({"side": "left"})

        # Her definerer vi en Text widget - der kan indeholde multiple linjer
        self.listGui = Text(self, width=150)
        self.listGui.insert(INSERT, "\nVelkommen til Mikkels bibliotek.\nDu har nu følgende muligheder:\n\n\t-\tSe alle materialer\n\t-\tLån materiale\n\t-\tAflever materiale\n\t-\tSortér i materiale\n\t-\tAfslut")
        frame.pack()
        self.listGui.pack()

    # Denne constructor køres når programmet starter
    # og sørger for at alle vores widgets bliver lavet.
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

root = Tk()
app = Application(master=root)
app.mainloop()