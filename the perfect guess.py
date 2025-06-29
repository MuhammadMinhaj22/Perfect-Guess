import random 
print("\nThe Perfect Guess\n")
n = random.randint(1, 100)
a = -1
guesses=1
while(a != n):
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
        guesses += 1
    elif(a<n):
         print("Higher number please")
         guesses += 1
print(f"\nYou have guessed the number {n} correctly in {guesses} attempts\n")
