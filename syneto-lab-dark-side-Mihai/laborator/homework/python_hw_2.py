import random

def guess():
    l=[0,0,0,0,0] #this is the list of the numbers that you guessed, or not :)
    x = random.randint(10000, 99999)
    #print(x)
    one = 0 #these are some flags for my if's
    two = 0
    three = 0
    four = 0
    five = 0
    while True: #if the number isnt guessed
        y = input("Enter a 5 digit number: ")
        y = int(y) #my "number" is actually a string type so i convert it to int
        if y == x:
            print("You guessed the number!")
            break
        else:
            if y % 10 == x % 10 and five == 0: #basic math knowledge
                five = 1
                print("Matched the last digit")
                l[4] = y%10 #those set the specific digit in the "guessing" list
                print(l) #we show the player the list with it's guessings
            if y // 10 % 10 == x // 10 % 10 and four == 0:
                print("Matched the fourth digit")
                l[3] = y//10%10
                print(l)
            if y // 100 % 10 == x // 100 % 10 and three == 0:
                print("Matched the third digit")
                l[2] = y//100%10
                print(l)
            if y // 1000 % 10 == x // 1000 % 10 and two == 0:
                print("Matched the second digit")
                l[1] = y//1000%10
                print(l)
            if y // 10000 % 10 == x // 10000 % 10 and one == 0:
                print("Matched the first digit")
                l[0] = y//10000%10
                print(l)
            if(one == 0 and two ==0 and three == 0 and four == 0 and five == 0):
               print("No matches")

guess()
