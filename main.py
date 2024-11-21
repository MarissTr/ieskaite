from kaste import Rekins

def main():
    vards = input("ievadi vārdu")
    teksts = input("ievadi tekstu")
    izmers = input("Ievadi lādītes izmēru")
    materials = input("Ievadiet kokmateriāla cenu")

    rekins = Rekins(vards, teksts, izmers, materials)
    rekins.saglabat()
    rekins.izdrukat()