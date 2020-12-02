#replace '/n' with comma
inputfile=open("aoc2.txt","r+")
input=inputfile.read()
input=input.replace('\n',',')
outputfile=open("aoc2.txt","w+")
outputfile.write(input)
inputfile.close()
outputfile.close()

# PART 1
inputlist = input.split(',')

import pandas as pd
inputdf = pd.DataFrame()
inputdf = inputdf.append(inputlist)
inputdf = inputdf.rename(columns={0:"temp"})
inputdf = inputdf.temp.str.split(expand=True)
inputdf = inputdf.rename(columns={0:"temp"})
ranges = inputdf.temp.str.split('-',expand=True)
ranges = ranges.rename(columns = {0:'min', 1:'max'})
inputdf = inputdf.rename(columns={1:'letter', 2:'password'})
inputdf = pd.concat((inputdf, ranges), axis=1)

countlist = []
for symbol, pw in zip(inputdf.letter, inputdf.password):
    count = 0
    for character in pw:
        if character == symbol[0]:
            count +=1
    countlist.append(count)
inputdf['character_freq'] = countlist
            
inputdf = inputdf.freq.str.split('-',expand=True)
inputdf = inputdf.rename(columns={0:"min", 1:'max'})

valid_passwords = 0
for row in inputdf.iterrows():
    if row[1]['character_freq'] in range (int(row[1]['min']), int(row[1]['max'])+1):
        valid_passwords+=1

print('There are',valid_passwords,'valid passwords in this dataset')
#############################################
# PART 2
#add column for character pos
pos_list = []
for pw, letter in zip(inputdf.password, inputdf.letter): 
    positions = ([pos +1 for pos, char in enumerate(pw) if char == letter[0]])
    pos_list.append(positions)
inputdf['positions'] = pos_list

n=0
for pos, minval, maxval in zip(inputdf['positions'], inputdf['min'], inputdf['max']):
    if int(minval) in pos:
        if int(maxval) in pos:
            continue
        else:
            n+=1
    elif int(maxval) in pos:
        if int(minval) in pos:
            continue
        else:
            n+=1
    else:
        continue

print('There are',n,'valid passwords in this dataset')
