import random
print("lets play a game")
player_wins=0
computer_wins=0
List=["rock","paper","scissors"]
while True:
    player_choice=input("enter a choice rock paper scissor or quit \n ").lower()
    if player_choice=="q":
        break
    if player_choice==["rock","paper","scissors"]:
        continue
    rand=random.randint(0,2)
    computer_choice=List[rand]
    print("computer chooses : ",computer_choice)
    if(player_choice=="scissors" and computer_choice=="paper"):
        print("player wins")
        player_wins+=1
        continue
   
    elif(player_choice=="rock" and computer_choice=="scissors"):
        print("player wins")
        player_wins+=1
        continue

        
    elif(player_choice=="paper" and computer_choice=="rock"):
        print("player wins")
        player_wins+=1
        continue
    elif(player_choice==computer_choice):
        print("none of the party wins")
        continue
    else:
        print("computer wins")
        computer_wins+=1
        continue
print("player wins",player_wins)
print("computer wins",computer_wins)


