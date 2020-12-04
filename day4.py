inputfile=open("day3.txt","r+")
input=inputfile.read()
input=input.replace('\n',' ')
outputfile=open("new_day3.txt","w+")
outputfile.write(input)
inputfile.close()
outputfile.close()

inputfile=open("new_day3.txt","r+")
input=inputfile.read()
input=input.replace('  ','\n')
outputfile=open("aoc3.txt","w+")
outputfile.write(input)
inputfile.close()
outputfile.close()

#PART 1
import re
index_no =0
dictionary = {}
dictlist = []
with open("aoc3.txt", "r") as file:
    for line in file:     
        dictlist = re.split(" ", line)
        dictionary[index_no] = {}
        for pair in dictlist:
            if pair.endswith('\n'):
                pair=pair.replace('\n','')
                dictionary[index_no][pair.split(':')[0]] = (pair.split(':')[1])
            else:
                dictionary[index_no][pair.split(':')[0]] = (pair.split(':')[1])
        index_no+=1

dictionary1 = {}
valid_passports = 0        
for key1 in range(len(dictionary)):
    if 'ecl' in dictionary[key1].keys():
        if 'eyr' in dictionary[key1].keys():
            if 'byr' in dictionary[key1].keys():
                if 'hcl' in dictionary[key1].keys():
                    if 'hgt' in dictionary[key1].keys():
                        if 'iyr' in dictionary[key1].keys():
                            if 'pid' in dictionary[key1].keys():
                                dictionary1[valid_passports] = dictionary[key1]
                                valid_passports+=1
print('there are', valid_passports, 'valid passports')
        
#PART 2
eye_cols = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

valid_passports = 0  
filtered1 = {} 
n=0   
for key1 in range(len(dictionary1)):
    if 'ecl' in dictionary1[key1].keys() and dictionary1[key1]['ecl'] in eye_cols:
        if 'eyr' in dictionary1[key1].keys() and 2020 <= int(dictionary1[key1]['eyr']) <= 2030:
            if 'byr' in dictionary1[key1].keys() and 1920 <= int(dictionary1[key1]['byr']) <= 2002:
                if 'hcl' in dictionary1[key1].keys():
                    if dictionary1[key1]['hcl'].startswith('#') and all(c in "0123456789abcdef" for c in dictionary1[key1]["hcl"][1:]):
                        if 'iyr' in dictionary1[key1].keys() and 2010 <= int(dictionary1[key1]['iyr']) <= 2020:
                            filtered1[n] = dictionary1[key1]
                            n+=1
filtered2 = {}                           
n = 0
for key1 in range(len(filtered1)):
    if 'pid' in filtered1[key1].keys():
        if len(filtered1[key1]['pid']) == 9 and filtered1[key1]['pid'].isnumeric():
            filtered2[n] = filtered1[key1]
            n+=1

filtered3 = {}                           
n = 0
valid_passports = 0
for key1 in range(len(filtered2)):   
    if 'hgt' in filtered2[key1].keys():
        if filtered2[key1]['hgt'].endswith('cm'):
            temp = re.compile("([0-9]+)([a-zA-Z]+)") 
            res = temp.match(filtered2[key1]['hgt']).groups() 
            if 150 <= int(res[0]) <= 193:
                valid_passports+=1
        elif filtered2[key1]['hgt'].endswith('in'):
            temp = re.compile("([0-9]+)([a-zA-Z]+)") 
            res = temp.match(filtered2[key1]['hgt']).groups() 
            if 59 <= int(res[0]) <= 76:
                valid_passports+=1
        else:
            continue
print('there are', valid_passports, 'valid passports')
