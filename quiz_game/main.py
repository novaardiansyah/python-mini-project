print("welcome to my computer quiz!")

playing = input("do you want to play? ")

if (playing.lower() != "yes" and playing.lower() != "y"):
  quit()

print("okay! let's play :)")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
  print("correct!")
  score += 10
else:
  print("incorrect!")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
  print("correct!")
  score += 10
else:
  print("incorrect!")

answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
  print("correct!")
  score += 10
else:
  print("incorrect!")

print("you got " + str(score) + " points!")
print("You got " + str(int((score / 30) * 100)) + "%.")