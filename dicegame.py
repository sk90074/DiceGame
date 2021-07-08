#Importing the random module
import random

#The die class
class Die():
  faceImages = [" -------\n|       |\n|   O   |\n|       |\n -------", " -------\n|       |\n|  O O  |\n|       |\n -------", " -------\n| O     |\n|   O   |\n|     O |\n -------", " -------\n| O   O |\n|       |\n| O   O |\n -------", " -------\n| O   O |\n|   O   |\n| O   O |\n -------", " -------\n| O   O |\n| O   O |\n| O   O |\n -------"]
  faceValues = [1, 2, 3, 4, 5, 6]

  face = ""
  faceValue = -1


  def roll(self):
    index = random.randint(0,5)
    self.face = self.faceImages[index]
    self.faceValue = self.faceValues[index]

  def __str__(self):
    returnString = ""
    if self.faceValue > 0:
      returnString = self.face
    else:
      returnString = "The die is not yet rolled."
    return returnString

#The dice game class
class DiceGame():
  die1 = Die()
  die2 = Die()

  def play(self):
    self.die1.roll()
    self.die2.roll()
    print(str(self.die1))
    print(str(self.die2))
    print("Face value:",self.die1.faceValue + self.die2.faceValue)

 
#myGame
running = True

#The loop
while running == True:
  myGame = DiceGame()
  myGame.play()
  replay = int(input("Do you want to play again? Enter 1 for yes and 2 for no."))
  if replay == 1:
    pass
  elif replay == 2:
    running = False
  else:
    print("ERROR")
