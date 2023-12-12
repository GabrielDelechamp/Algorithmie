def CompteLettre(texte):
    nbLettre=len(texte)
    return nbLettre

Tableau=[]
print(Tableau)
mot=''
i=0

while mot != 'STOP':
    mot=input('Entrer un mot : ')
    Tableau.append(CompteLettre(mot))
    i+=1

for j in range(0,i-1):
    print(Tableau[j])

