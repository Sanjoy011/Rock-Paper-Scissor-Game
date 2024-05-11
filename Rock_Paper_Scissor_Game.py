import random
l=["Paper","Rock","Scissor"]

while True:
    ucount=0 #user count
    ccount=0 #computer count
    uc=int(input('''
Lets! play a game guys are you ready?
1no.YES
2no.NO|Exit                                                                          
                Choose Enter the number:-----------> '''))
    if uc==1:
        print("Sure, I'm ready! What game do you have in mind?")
        for a in range(1,6): #1 to 5 times,
            UserInput=int(input('''
1no.Paper
2no.Rock
3no.Scissor                                                                
            Choose enter a number:-------->  '''))
            if UserInput==1:
                uchoise="Paper"
            elif UserInput==2:
                uchoise="Rock"
            elif UserInput==3:
                uchoise="Scissor"
            comchoise=random.choice(l) 
            if comchoise==uchoise:
                    print("User Choise:- ",uchoise)
                    print("Computer Choise:- ",comchoise)
                    print("Game Draw")
                    ucount=ucount+1
                    ccount=ccount+1
            elif (uchoise=="Paper" and comchoise=="Rock") or (uchoise=="Rock" and comchoise=="Scissor") or (uchoise=="Scissor"  and comchoise=="Paper"):
                    print("User Choise:- ",uchoise)
                    print("Computer Choise:- ",comchoise)
                    print("You Win!")
                    ucount=ucount+1
            else:
                    print("User Choise:- ",uchoise)
                    print("Computer Choise:- ",comchoise)
                    print("Computer Win") 
                    ccount=ccount+1 
        if ucount==ccount:
             print("Final Game is Draw.....")  
             print("Your score ",ucount)
             print("Your score ",ccount)
        elif ucount>ccount:
             print("Final you win the game.....")  
             print("Your score ",ucount)
             print("Your score ",ccount) 
        else:
            print("Final  computer win the game.....")  
            print("Your score ",ucount)
            print("Computer score ",ccount)               
    else:
        break    
                  