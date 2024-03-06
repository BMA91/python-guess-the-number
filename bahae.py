import random
def guessing_game():
  random_number = int(random.randint(1, 100))
  guessed_number= int(input("enter a number between 1 and 100: "))
  gsd=int(guessed_number)
  for i in range (2, 11):
        if int(gsd)<random_number:
            print("GO HIGHER" )   
        elif int(gsd)>random_number:
            print("GO LOWER")
        else :
            print("YOU WON!!!!!")
            break
        print("it is your",i, "attempt")
        gsd=input("enter again: ")     
 
  if i==10 :
        print("""you lost :(
        the number was """,random_number)

response="y"

while response=="y":
  guessing_game()
  response=input("if you want to replay press 'y' and if you dont press 'n': ")
  
print("END OF THE GAME") 
