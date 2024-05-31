import random
def plyrpick(): 
  pick = input("what is your choice\nrock = 0\npaper = 1\nscissors = 2\n")#get the players input
  if pick != "1" and pick != "2" and pick != "0":
    print("invalid input, try again")#see if input is valid
    return plyrpick()
  else:
    return pick

def whowin(plyr1, plyr2):
  if (plyr1 == plyr2):
    return "tie"
  elif (plyr1 == 0 and plyr2 == 1):
    return "computer wins"
  elif (plyr1 == 1 and plyr2 == 2):
    return "computer wins"
  elif (plyr1 == 2 and plyr2 == 0):
    return "computer wins"
  elif (plyr1 == 1 and plyr2 == 0):
    return "player wins"
  elif (plyr1 == 2 and plyr2 == 1):
    return "player wins"
  elif (plyr1 == 0 and plyr2 == 2):
    return "player wins"

def RockPaperScisor(x):
  if (x == 0):
    return "rock"
  elif (x == 1):
    return "paper"
  else:
    return "scissors"

def Gameloop():
  cguess = random.randint(0,2)
  plyrguess = int(plyrpick())
  print (whowin(plyrguess,cguess))
  print("you picked: " + RockPaperScisor(plyrguess) + "\nthe computer picked: " + RockPaperScisor(cguess))
  playagain = input("Do you want to play again? y/n\n")
