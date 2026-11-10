import random
print("Welcome to the number gussing game!!\n")

        
secret_number = random.randint(1,10)
attempt =0

while True:
    guess = input("enter a number between 1 and 10: ")
    guess = int(guess)
    attempt+=1
    
    if guess == secret_number:
        print(f"Correct\n You guessed the number in {attempt} triles")
        break
    elif guess > secret_number:
        print("Too high\n Try again")
    else:
        print("Too low\n Try again")