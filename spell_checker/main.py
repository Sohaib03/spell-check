from data import functions,prediction
# import json
# from pprint import pprint

def main():
    file = functions.read_file()
    dict = functions.open_dict()
    for line_no,line in enumerate(file):
        for word in line.split():
            if (word.lower()+'\n' not in dict):
                suggestions = functions.suggest(word)
                print ( word, " at line ",line_no+1, "is not found. But it matches :",suggestions)

if __name__== "__main__":
    main()