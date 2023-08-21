import os

def sort_letter_dict(letter_dict): #function to sort the dict so its more clearer to see the changes 
    sorted_dict = {}
    for key in sorted(letter_dict):
        sorted_dict[key] = letter_dict[key]
    return sorted_dict

def letter_sum(letter_dict): #the sum of all the letters in your file (actually the sum of your dict :D)
    letter_sum = 0
    for key in letter_dict:
        letter_sum += letter_dict[key]
    return letter_sum

with open("D:\VSC_Projects\syneto-lab-dark-side\homework\py_hw_3.txt", "r") as file: #replace with your own path
    
    letter_dict = {}
    
    for line in file.readlines(): #reading every line (i dont have 100)
        for word in line.split(): #splitting the line into words
            for letter in word: #dont need to say more, it's obvious the purpose of this loop
                if letter in letter_dict: #if the letter is already in the dict, add 1 to the value
                    letter_dict[letter] += 1 
                else: #else add it to the dict and set the value to 1
                    letter_dict[letter] = 1
                    
    print("\nmy dict:\n", letter_dict, "\n")
    print("sorted dict: \n", sort_letter_dict(letter_dict),"\n")
    print("total letters:", letter_sum(letter_dict), "\n")

                
                    