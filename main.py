# Spaghettio's Parser by Kyle Levy
import pandas as pd
import numpy as np
# Grab Contents of input file
file_path = 'input.txt'
file = open(file_path)

str = (file.read()).lower()

# Clean up the string to remove punctuation and spaces
str_cleaned = str.replace(" ","").replace("!","")

# Create a dataframe to keep track of all the letter stats
df = pd.DataFrame(np.array([[27,28,29,26,32,31,28,26,28,30,39,32,27,25,441,35,26,37,30,31,28,25,31,26,26,36]]),
                   columns=['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
                   # The 0 index is the frequency that the letter will appear in a given can of Spaghettios
                   # The 1 index is how many times the letter appeared in the input string

# Calculate number of times the characters appear in a string
df.loc[len(df.index)] = [
    str_cleaned.count('a'), 
    str_cleaned.count('b'), 
    str_cleaned.count('c'),
    str_cleaned.count('d'),
    str_cleaned.count('e'),
    str_cleaned.count('f'),
    str_cleaned.count('g'),
    str_cleaned.count('h'),
    str_cleaned.count('i'), 
    str_cleaned.count('j'), 
    str_cleaned.count('k'),
    str_cleaned.count('l'),
    str_cleaned.count('m'),
    str_cleaned.count('n'),
    str_cleaned.count('o'),
    str_cleaned.count('p'),
    str_cleaned.count('q'), 
    str_cleaned.count('r'), 
    str_cleaned.count('s'),
    str_cleaned.count('t'),
    str_cleaned.count('u'),
    str_cleaned.count('v'),
    str_cleaned.count('w'),
    str_cleaned.count('x'),
    str_cleaned.count('y'),
    str_cleaned.count('z')
]

#Find how many cans will be required to have all the necessary letters

df.loc[len(df.index)] = [
    df['a'][1] / df['a'][0], 
    df['b'][1] / df['b'][0], 
    df['c'][1] / df['c'][0], 
    df['d'][1] / df['d'][0], 
    df['e'][1] / df['e'][0], 
    df['f'][1] / df['f'][0], 
    df['g'][1] / df['g'][0], 
    df['h'][1] / df['h'][0], 
    df['i'][1] / df['i'][0], 
    df['j'][1] / df['j'][0], 
    df['k'][1] / df['k'][0], 
    df['l'][1] / df['l'][0], 
    df['m'][1] / df['m'][0], 
    df['n'][1] / df['n'][0], 
    df['o'][1] / df['o'][0], 
    df['p'][1] / df['p'][0], 
    df['q'][1] / df['q'][0], 
    df['r'][1] / df['r'][0], 
    df['s'][1] / df['s'][0], 
    df['t'][1] / df['t'][0], 
    df['u'][1] / df['u'][0], 
    df['v'][1] / df['a'][0], 
    df['w'][1] / df['w'][0], 
    df['x'][1] / df['x'][0], 
    df['y'][1] / df['y'][0], 
    df['z'][1] / df['z'][0], 
]



#Print the results!
num_cans = int(np.ceil(df.max(axis=1)[2]))
price_cans = num_cans*6.00

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("If you were to letter out this text file in Spaghettio's, you would need:", num_cans, "can(s).")
print("That would cost you: $%0.2f." %price_cans)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")