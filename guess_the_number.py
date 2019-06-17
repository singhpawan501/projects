import random as r
print("Game for Guess The Number")
key='yes'
count=0
match=0
while key=='yes' or key=='y' :
    guess=int(input("Guess The Number between : 1 to 8  :"))
    rand=r.randint(1,8)
    match=match+1
    if guess==rand:
        print("you have guess the correct number")
        print("you have WON !")
        count=count+1
    else :
        print("you have guess wrong number.")
    key=input("do you want to guess more number : ") 
print("THANKS FOR PLAYING THIS GAME")
print("you have play ",match," matches and won ",count," matches")
print("guess pridiction is : ",round((count/match)*100,2),"%." )    
