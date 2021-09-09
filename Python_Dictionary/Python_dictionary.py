import json 

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data(word.title())
    elif word.upper() in data:
        return data(word.upper())
         
    else:
        print("Invalid word")

word = input("Enter the word you want to search \n")
output = translate(word)
print(output)