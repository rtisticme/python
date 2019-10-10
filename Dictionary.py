import json 
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w=w.lower() #converting all words entered to lower case
    if w in data:
        return data[w] #data[rain]
    elif w.title() in data: #if user entered "delhi" this will check for "Delhi" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0: 
        yn=input("Did you mean %s instead? Enter Y or N"%get_close_matches(w,data.keys())[0]).upper())
        if yn=='Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=='N':
             return "Sorry the word you are looking for is not in the dictionary"
        else:
             return "Enter only y or n"  
    else: #if the list is empty <=0
        return "the string is not present, please check"
   
#%s is replaced with w
#get close matches
#check entered word(W) with data keys and output the word with the highest match ratio, 
#0 is an index for the the question 

word = input("enter a word:")

output =translate(word)
if type(output)==list:
    for item in output :
        print(item)
        #output with mutiple definition are shown on 
        #seperate lines
else:
    print(output)
    #normal print without iteration 
    #gives the string is not present, please check
    #instead of 
    #string
    #is
    #not
    #...
    


    

