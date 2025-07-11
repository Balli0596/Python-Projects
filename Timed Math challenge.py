import random
import time
operand=["+","-","*","/"]
operand_1=3
operand_2=12
def generate_problem():
    left=random.randint(operand_1,operand_2)
    right=random.randint(operand_1,operand_2)
    op=random.choice(operand)
    expr=str(left)+" "+op+" "+str(right)
    answer=eval(expr)
    if op == '/':
        answer=f"{answer:.2f}" # Round division answers to 2 decimal places
    return expr, answer
wrong =0
print("Welcome to the Timed Math Challenge!")
print("You will be given 10 math problems to solve.")   
print("Try to answer them as quickly and accurately as possible.")
print("Let's begin!\n") 
start_time = time.time()

for i in range(10):
    expr,answer=generate_problem()
    while True:
       guess=input("problem "+str(i+1)+":"+expr+"=")
       if guess==str(answer):
           print("Correct!")  
           break 
       else:
           print("Incorrect! The answer is", answer)
           wrong+=1
end_time = time.time()
elapsed_time = end_time - start_time
print("\nChallenge completed!")
print("Elapsed time:", round(elapsed_time, 2), "seconds")
