import morpion_console

console = morpion_console.Console()
console.affiche()
victoire = False
while not victoire:
    col=int(input("Quelle colonne choisissez-vous ? ")) -1
    ligne=int(input("Quelle ligne choisissez-vous ? ")) -1  
    while not console.morpion.jeu_possible(col, ligne) :
        print( "Saisie invalide, rejouez")
        col=int(input("Quelle colonne choisissez-vous ? ")) -1
        ligne=int(input("Quelle ligne choisissez-vous ? ")) -1             
    case = 3*ligne + col
    console.morpion.plateau[case]= console.morpion.joueur
    console.affiche()
    victoire = console.morpion.victoire(case)
    vainqueur = console.morpion.joueur
    console.morpion.joueur = console.morpion.joueur % 2 +1
print("Victoire du joueur", vainqueur,"!")