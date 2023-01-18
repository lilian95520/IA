
from pickle import FALSE
from re import X
from turtle import pos, position

tour = 0
position_pion = [1,1,1,0,0,0,2,2,2]
def affichage ():
    
    for i in range(0,9,3):
        if i %3==0:
            print("----------")
        if position_pion[i]== 1:
            motif_1 = "X"
        elif position_pion[i]== 0:
            motif_1 = " "
        elif position_pion[i]== 2 :
            motif_1 = "O"
        if position_pion[i+1]== 1:
            motif_2 = "X"
        elif position_pion[i+1]== 0:
            motif_2 = " "
        elif position_pion[i+1]== 2 :
            motif_2 = "O"
        if position_pion[i+2]== 1:
            motif_3 = "X"
        elif position_pion[i+2]== 0:
            motif_3 = " "
        elif position_pion[i+2]== 2 :
            motif_3 = "O"

        
        print("|"+ motif_1,"|"+ motif_2,"|"+ motif_3,"|")



def bouger(pion,x):
    global tour
    
    if tour%2==0:
        if x-pion == 2 or x-pion== 4:
            position_pion[pion],position_pion[x]= 0, position_pion[pion]
        else:
            position_pion[pion],position_pion[x]=position_pion[x],position_pion[pion]

    else :
        if x-pion == -2 or x-pion== -4:
            position_pion[pion],position_pion[x]= 0,position_pion[pion]
        else:
            position_pion[pion],position_pion[x]=position_pion[x],position_pion[pion]
            
    

def gagner():
    global tour
    n = 0
    
    somme = 0
    somme_1 = 0
    for i in range (9):
        if position_pion[i]==1:
            somme +=1
        if position_pion[i]==2:
            somme_1+=1
    if somme ==0 or somme_1 == 0:
        return True
    if position_pion[0] == 2 or position_pion[1] == 2 or position_pion[2]==2 or position_pion[6] == 1 or position_pion[7] == 1 or position_pion[8]==1:
        return True
    
    
    if tour%2==0:
        liste = []
        for i in position_pion:
            if i == 1:
                liste.append(n)
                n+=1
            else :
                n+=1
        print(liste)
        for x in liste:
            for i in range(9):
                if peut_bouger(x,i):
                    return False
        return True
    
    elif tour%2==1:
        liste = []
        for i in position_pion:
            if i == 2:
                liste.append(n)
                n+=1
            else :
                n+=1
        print(liste)
        for x in liste:
            for i in range(9):
                if peut_bouger(x,i):
                    return False
        return True
                    
            
    
def peut_bouger(pion,x):
    global tour
    #peut bouger uniquement s'il avance où s'il va en diagonale pour gray
    if tour % 2 == 0:
        if position_pion[pion]!=1:
            return False
        if x-pion == 2 or x-pion ==4:
            if position_pion[x]==2:
                return True
            else: return False
    
        if x-pion == 3:
            if position_pion[x]==1 or position_pion[x]==2:
                return False
            else: return True
        else : 
            return False
    else :
        if position_pion[pion]!=2:
            return False
        if x-pion == -2 or x-pion == -4:
            if position_pion[x]==1:
                return True
            else: return False
    
        if x-pion == -3:
            if position_pion[x]==1 or position_pion[x]==2:
                return False
            else :
                return True
        else : 
            return False



def commencer_jeu():
    global tour
    affichage()
    joueur_1 = input("Joueur 1, quel est votre prénom ? ")
    while not gagner():
        if tour%2==0:            
            print("c'est à ",joueur_1)
        else:
            print("c'est au robot")
            
        pion = int(input("Quel pion souhaitez vous bouger ? "))
        position_2 = int(input("Où souhaitez vous le placez ? "))
        while peut_bouger(pion,position_2) == False:
            print("Impossible")
            pion = int(input("Quel pion souhaitez vous bouger ? "))
            position_2 = int(input("Où souhaitez vous le placez "))
        bouger(pion,position_2)
        print(affichage())   
        tour+=1
        
    if tour%2==1:
        print(joueur_1,"a gagné")
    else: print("Le robot a gagné")

                
                
                
commencer_jeu()
