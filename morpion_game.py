class Morpion_game:
    def __init__(self):
    #définit le plateau et le joueur
        self.plateau = [0]*9
        self.joueur = 1

    def jeu_possible(self,colonne, ligne):
    #renvoie un booléen, True si la case est libre, False sinon
        return colonne in [0,1,2] and ligne in [0,1,2] and self.get_case(ligne, colonne) == 0
    
    def get_case(self,l,c):
    #renvoie le contenu de la case en ligne l et colonne c
        p= 3*l+c
        return self.plateau[p]

    def consecutif(self,case,direction):
    #calcule le nombre de jetons consécutifs du même joueur dans une direction donnée
        if direction == 'g':           
            if case % 3 == 0 :
                return 0
            case-=1
        elif direction == 'd':
            if case % 3 == 2 :
                return 0
            case+=1
        elif direction == 'h':
            if case // 3 == 0 :
                return 0
            case-=3
        elif direction == 'b':
            if case // 3 == 2 :
                return 0
            case+=3
        elif direction == 'hg':
            if case % 3 == 0 or case // 3 == 0 :
                return 0
            case-=4
        elif direction == 'hd': 
            if case % 3 == 2 or case // 3 == 0 :
                return 0
            case-=2
        elif direction == 'bg':
            if case % 3 == 0 or case // 3 == 2 :
                return 0
            case+=2
        elif direction == 'bd':
            if case % 3 == 2 or case // 3 == 2 :
                return 0
            case+=4

        if self.plateau[case] != self.joueur :
            return 0
        return 1 + self.consecutif(case,direction)
        

    def victoire(self,case):
    #si le nombre de jetons alignée est supérieur ou égal à 4, on retourne True
        horizontal  = self.consecutif(case,'g') + self.consecutif(case,'d') + 1
        diagonale_hg = self.consecutif(case,'hg') + self.consecutif(case,'bd') + 1
        diagonale_hd = self.consecutif(case,'hd') + self.consecutif(case,'bg') + 1
        verticale = self.consecutif(case,'h') + self.consecutif(case,'b') + 1
        if horizontal == 3 or diagonale_hd == 3 or diagonale_hg >= 3 or verticale >= 3 :
            return True
        return False

        

if __name__ == "__main__":
    game = Morpion_game()
    for loop in range (10):
        col=int(input("Quelle colonne choisissez-vous ? ")) -1  
        while not game.jeu_possible(col):
            col=int(input("Colonne invalide, rejouez : ")) -1            
        game.jeu(game.joueur, col)

        if game.joueur == 1 :
            game.joueur = 2
        else :
            game.joueur = 1
