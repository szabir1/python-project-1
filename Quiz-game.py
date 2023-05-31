print("Welcome to my computer quiz!")
playing= input("Do you want to play? ")
print(playing)
if playing.lower()!= "yes":
    quit()
print("Okay! Let's play :)")
score=0
marks=+0
answer= input("What does CPU stand for? ")
if answer.lower()== "central processing unit":
    print("correct!")
    score+=1
    marks+=1    
else:
    print("incorrect!")
    marks-=1
answer= input("What does GPU stand for? ")
if answer.lower()== "graphics processing unit":
    print("correct!")
    score+=1
    marks+=1
else:
    print("incorrect!")
    marks-=1
answer= input("What does ram stand for? ")
if answer.lower()== "random access memory":
    print("correct!")
    score+=1
    marks+=1
else:
    print("incorrect!")
    marks-=1  
answer= input("What does psu stand for? ")
if answer.lower()== "power supply unit":
    print("correct!")
    score+=1
    marks+=1
else:
    print("incorrect!")
    marks-=1
    
print("You got "+ str(score) +" questions correct!")
print("You got "+ str((score/4)*100) +"%" +" correct!")
print("You got "+ str(marks) +" marks")
