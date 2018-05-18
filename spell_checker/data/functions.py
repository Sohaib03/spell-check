import json
from data import prediction

def read_file():
    with open("data/file",'r') as file:
        return file.readlines()

# def read_dict():
#     with open("data/words_dictionary.json") as file:
#         return json.load(file)
def open_dict():
    with open ("data/l_words.txt",'r') as file:
        return file.readlines()
# with open("words.txt",'r') as dict:
#     d = dict.readlines()
#     with open("l_words.txt",'w') as writ:
#         for i in d:
#             writ.write(i.lower())

def suggest ( string ):
    return prediction.candidates(string)
    # matched_with=[]
    # for i in open_dict():
    #     match = SequenceMatcher(None,string+'\n' , i).ratio() + abs(len(string+'\n')-len(i))/len(string+'\n')
    #     if (match>max_match):
    #         max_match=match
    #         matched_with+=[i]
    # return matched_with

