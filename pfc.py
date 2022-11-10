from random import *
joueur1 = input("Joueur 1, quel est votre nom ? ")

score_j = 0
score_o = 0
cp=["caillou", "rock", "pierre"]
cf=["feuille", "papier", "paper"]
cc=["ciseaux","cissors", "cisors"]
    

while score_j != 3 and score_o != 3 :
    p1 = (input("Papier, caillou, ciseaux ? \n")).lower()
    p2 = randint(0,2)
    if p1 in cf :
        if p2 == 1 :
            print ('égalité')
        if p2 == 2 :
            score_o += 1
            print("un point pour l'ordinateur")
        if p2 == 0 :
            score_j += 1
            print("un point pour", joueur1)
    elif p1 in cp :
        if p2 == 0 :
            print('égalité')
        if p2 == 1 :
            score_o += 1
            print("un point pour l'ordinateur")
        if p2 == 2 :
            score_j += 1
            print("un point pour", joueur1)
    elif p1 in cc :
        if p2 == 2 :
            print('égalité')
        if p2 == 0 :
            score_o += 1
            print("un point pour l'ordinateur")
        if p2 == 1 :
            score_j += 1
            print("un point pour", joueur1)
    elif p1 == 'ciseau' :
        print("On dit une paire de ciseauX")
    elif p1 == 'puits' :
        print("Juste pour ça tu devrais perdre un point petit malin")
    else :
        print("saisie invalide, fais un effort")

if score_j == 3 :        
    if joueur1 == "Sylvain" :
        print("Bravo Sylvain, vous avez remporté la partie !!")
#quelques points en plus pour ce message personnalisé ??
    else :
        print("Victoire de ",joueur1 ,"!!")
else :
    print("Victoire de l'ordinateur, muahahaha")
