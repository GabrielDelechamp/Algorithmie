def VerifEntier (saisieF):
    while saisieF.isdigit()==False:
        saisieF=input("Entrer un Entier : ")

    return saisieF

def SaisieIndex(index):
    index=input('Saisir un index : ')
    VerifEntier(index)
    while int(len(Tab)) < int(index) :
        index=input('Saisir un index valide : ')
    return index

Tab = []
resultat=0
saisie=input('Entrer un nombre : ')
index1=0
index2=0

while saisie !=0 :
    saisie=input("Entrer un nombre : ")
    VerifEntier(saisie)
    saisie=int(saisie)
    Tab.append(saisie)
    resultat+=saisie
    if resultat>=100:
        break

index1=SaisieIndex(index1)
index2=SaisieIndex(index2)

index1=int(index1)
index2=int(index2)

SommeIndex=Tab[index1]+Tab[index2]

print (SommeIndex)
