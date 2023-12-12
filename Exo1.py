def ChgmtEtoile(texte):
    Resultat=''
    for i in range (0,len(texte)):
        Resultat+= '*'
        
    return Resultat


mot=input("Entrer un mot : ")
print(ChgmtEtoile(mot))


