import morpion_game

class Console():

    def __init__(self):
        self.morpion = morpion_game.Morpion_game()

    def affiche(self):
        for ligne in range(3):
            for colonne in range(3):
                contenu = self.morpion.get_case(ligne,colonne)
                if contenu == 0 :
                    print(' . ',end="")
                elif contenu == 1 :
                    print(' X ',end="")
                else :
                    print(' O ',end="")
            print()

if __name__ == '__main__':
    console = Console()
    console.affiche()
    victoire = False
    while not victoire:
        col=int(input("Quelle colonne choisissez-vous ? ")) -1 
        ligne=int(input("Quelle ligne choisissez-vous ? ")) -1     
        while not console.morpion.jeu_possible(col, ligne) :
            print("Saisie invalide, rejouez")
            col=int(input("Quelle colonne choisissez-vous ? ")) -1
            ligne=int(input("Quelle colonne choisissez-vous ? ")) -1            
        case = 3*ligne + col
        console.morpion.plateau[case]= console.morpion.joueur
        console.affiche()
        victoire =  console.morpion.victoire(case)
        console.morpion.joueur %= 2
        console.morpion.joueur += 1
    print("Victoire du joueur ", console.morpion.joueur," !")
