count=0
print("welcome to my quiz")
playing=input("do you want to play? ")
if(playing!= "yes"):
    quit()
print("welcome to my quiz!!")

answer=input("what does cpu stand for \n")
if(answer.lower()=="control processing unit" ):
    print("correct")
    count+=1
    print("your marking",count)
else:
    print("incorrect")
    
answer=input("what does gpu stand for \n")
if(answer.lower()=="graphical processing unit" ):
    print("correct")
    
    
    
else:
    print("incorrect")
 
answer=input("what doegrs psu stand for \n")
if(answer.lower()=="power supplying unit" ):
    print("correct")
    
    count+=1
    print("your marking",count)
else:
    print("incorrect")


print ("YOU COMPLETED QUIZ")
print("YOUR RESULT:",count)

   

