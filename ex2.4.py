import timeit

my_setup = '''
import numpy as np

with open("pg2701.txt", 'r', encoding='utf-8') as file:
    data_list = file.readlines()
    
file.close()

data_array = np.array(data_list)

vowel_list = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
vowels_per_word_list = []
start_check = False
'''

my_code = '''
for line in data_array:
    
    # Start counting at "CHAPTER 1. Loomings."
    if start_check == False:
        if "CHAPTER 1. Loomings." in line:
            start_check = True
        else:
            continue
        
    # Separate each line into words
    line = line.split()
        
    for word in line:
        vowels_per_word = 0
        
        for char in word:
            if char in vowel_list:
                vowels_per_word += 1
            
        vowels_per_word_list.append(vowels_per_word)
'''

# avg_vowels = sum(vowels_per_word_list) / len(vowels_per_word_list)
# print("There is an average of", round(avg_vowels), "vowel(s) per word")

print("The average time taken is", (timeit.timeit(stmt=my_code, setup=my_setup, number=100)) / 100, "sec")
