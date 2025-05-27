class Sanatiedosto: #lataa sanat tiedostosta
    pass

class Pelilogiikka:
    def __init__(self, sana):
        self.sana = sana
        self.arvaukset = set()
        self.yritykset = 6
        
    def arvaa(self, arvaus):
        arvaus = arvaus.lower()
        if not arvaus.isalpha():
            return "Anna vain kirjaimia."
        
        if len(arvaus) == 1:
            if arvaus in self.arvaukset:
                return "Olet jo arvannut tämän kirjaimen."
            self.arvaukset.add(arvaus)
            if arvaus in self.sanat:
                return "Kirjain on sanassa"
            else:
                self.yritykset -=1
                return "Väärä kirjain"
        else:
            if arvaus == self.sana:
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
        

class Hirsipuu: #pelin alustus, silmukka, tarkistukset(oikea kirjain-väärä kirjain), voitto/häviötilanteet
    pass


# Pelin käynnistys:
hirsipuu()
