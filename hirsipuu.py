from random import choice
class Sanatiedosto: 
    def valitse_sana():
        sanat = []
        with open("sanat.txt") as tiedosto:
            for sana in tiedosto:
                sana = sana.replace("\n","")
                sanat.append(sana)
        satunnainen = choice(sanat)
        return satunnainen
    def arvausten_maara():
        arvaukset = input("Anna väärien arvausten maksimi määrä: ")
        return int(arvaukset)

class Pelilogiikka:
    def __init__(self, sana):
        self.sana = sana
        self.arvaukset = set()
        self.yritykset = Sanatiedosto.arvausten_maara()
        
    def arvaa(self, arvaus):
        arvaus = arvaus.lower()
        if not arvaus.isalpha():
            return "Anna vain kirjaimia."
        
        if len(arvaus) == 1:
            if arvaus in self.arvaukset:
                return "Olet jo arvannut tämän kirjaimen."
            self.arvaukset.add(arvaus)
            if arvaus in self.sana:
                return "Kirjain on sanassa"
            else:
                self.yritykset -=1
                return "Väärä kirjain"
        else:
            if arvaus == self.sana:
                self.arvaukset.update(self.sana)
                return "Oikea sana"
            else:
                self.yritykset -=1
                return f"Väärä sana!! Sana ei ollut \"{arvaus}\"."
            
    def nykyinen_tila(self):
        return [kirjain if kirjain in self.arvaukset else "_" for kirjain in self.sana]
    
    def pelin_loppu(self):
        if self.yritykset == 0:
            return True, f"Hävisit! Oikea sana oli: {self.sana}"
        if all(k in self.arvaukset for k in self.sana):
            return True, f"Onneksi olkoon! Arvasit sanan oikein: {self.sana}"
        return False, ""
        

class Hirsipuu:
    def __init__(self):
        sana = Sanatiedosto.valitse_sana()
        self.peli = Pelilogiikka(sana)
    
    def kaynnista(self):
        print("Tervetuloa pelaamaan Hirsipuuta!")
        while True:
            print("Sana: ", " ".join(self.peli.nykyinen_tila()))
            print(f"Yrityksiä jäljellä: {self.peli.yritykset}")
            arvaus = input("Arvaa kirjain tai koko sana: ")
            palaute = self.peli.arvaa(arvaus)
            print(palaute)

            loppu, viesti = self.peli.pelin_loppu()
            if loppu:
                print(viesti)
                break


# Pelin käynnistys:
peli = Hirsipuu()
peli.kaynnista()
