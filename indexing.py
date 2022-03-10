"""
friday, 4th march 2022

indexing line in file.

required:
    pip install nltk

assignment for infomation retrival course
sekalian belajar list comprehension lah cok

author: github.com/andika-eka
"""
import sys
import os
import re
import nltk

if __name__ == '__main__':
    # use TuringTest.txt for test example. https://en.wikipedia.org/wiki/Turing_test
    path = "./TuringTest.txt" 

    if not os.path.exists(path):
        print("file is mising")
        sys.exit()

    lines = list()

    with open(path) as file:
        #split by lines
        lines = file.read().splitlines()
    
    #use regex to remove all puctuation and make all text lowercase
    lines = [re.sub(r'[^\w\s]', '', line).lower() for line in lines]
    lines = [re.sub(r'\d+','', line) for line in lines] #remove number

    # print(*lines, sep="\n")

    token = list()

    from nltk.tokenize import word_tokenize
    for line in lines:
        #tokenizing
        token.append(word_tokenize(line))
    
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    # print(stop_words)

    #remove all stop words
    for index, val in enumerate(token):
        token[index]  = [word for word in token[index] if not word in stop_words]
    
    tokenDocID = [[term, docID+1] for docID, terms in enumerate(token) for term in terms ]
    tokenSorted = sorted(tokenDocID, key=lambda item: item[0])
    # print(tokenSorted)

    #create posting list...uh i mean dictionary
    postingDict = dict()
    for item in tokenSorted:
        if item[0] in postingDict:
            postingDict[item[0]].add(item[1])
        else:
            postingDict[item[0]] = {item[1]}
    print(postingDict)

    # output all result into a csv file
    if not os.path.exists("./output"):
        os.mkdir("./output")
    with open("./output/tokenize.csv", 'w') as file:
        for item in tokenDocID:
            out = str(item[0]+ ','+ str(item[1])+",\n")
            file.write(out)

    with open("./output/sortPosting.csv", 'w') as file:
        for item in tokenSorted:
            out = str(item[0]+ ','+ str(item[1])+",\n")
            file.write(out)
    
    with open("./output/postingList.csv", 'w') as file:
        for key, val in postingDict.items():
            out = str(key+ ',' + str(len(val)) +', '+ ", ".join(map(str, val))+"\n")
            file.write(out)
    

    

    