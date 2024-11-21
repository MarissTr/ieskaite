import datetime

class Rekins:
    def __init__(self, vards, teksts, izmers, materials):
        self.vards = vards
        self.teksts = teksts
        self.izmers = izmers
        self.materials = materials
        self.laiks = datetime.datetime.now()
        
    def aprekins(self):
        darba_samaksa = 15
        PVN = 21
        veltijuma_garums = len(self.teksts)
        platums, garums, augstums = self.izmers
        
        produkta_cena = (veltijuma_garums * 1.2) + ((platums / 100) * (garums / 100) * (augstums / 100) / 3 * self.materials)
        
        PVN_summa = (produkta_cena + darba_samaksa) * PVN / 100
        rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
        
        return rekina_summa
    
    def izdrukat(self):
        rekina_summa = self.aprekins()
        
        print(f"Rēķins izveidots: {self.laiks}")
        print(f"vards: {self.vards}")
        print(f"Veltījums: {self.teksts}")
        print(f"Izmērs (platums, garums, augstums): {self.izmers[0]}mm, {self.izmers[1]}mm, {self.izmers[2]}mm")
        print(f"Materiāla cena: {self.materials} EUR/m^2")
        print(f"Aprēķinātā summa: {rekina_summa:.2f} EUR")
    
    def saglabat(self):
        faila_nosaukums = f"{self.vards}_{self.laiks.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(faila_nosaukums, 'w') as file:
            file.write(f"Rēķins izveidots: {self.laiks}\n")
            file.write(f"vards: {self.vards}\n")
            file.write(f"Veltījums: {self.teksts}\n")
            file.write(f"Izmērs (platums, garums, augstums): {self.izmers[0]}mm, {self.izmers[1]}mm, {self.izmers[2]}mm\n")
            file.write(f"Materiāla cena: {self.materials} EUR/m^2\n")
            file.write(f"Aprēķinātā summa: {self.aprekins():.2f} EUR\n")
