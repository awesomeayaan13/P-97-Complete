import random





number=random.randint(1,10)
chances=0
while chances<5:
    guess=int(input("Enter your guess: "))

    if(guess==number):
        print("Yay you did it")
        break
      
    elif(guess<number):
         print("Guess is to low")
            
    elif(guess>number):
        print("Guess is to high")
    
    chances+=1
if  chances>=5:
    print("You lose get good the number is:" , number)