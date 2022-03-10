import csv

class PostingListIndex:
    postingDict = dict()

    def loadCSV(self, path):
        #   format : term, freq, index 1, index 2, ... , index n
        with open(path) as file:
            lines = csv.reader(file)
            for line in lines:
                self.postingDict[line[0]] =  set(map(int,line[2:]))
    
    def getIndex(self, term):
        if term in self.postingDict:
            index = self.postingDict[term]
            return index
        else:
            return None

    
    def indexAnd(self, term1, term2):
        if (term1 in self.postingDict) and (term1 in self.postingDict):
            index1 = self.postingDict[term1]
            index2 = self.postingDict[term2]
            return index1.intersection(index2)
        else:
            return None

    def indexOr(self, term1, term2):
        if (term1 in self.postingDict) and (term1 in self.postingDict):
            index1 = self.postingDict[term1]
            index2 = self.postingDict[term2]
            return index1.union(index2)
        else:
            return None

    


if __name__ == '__main__':
    test = InvertedIndex()
    path ="./output/postinglist.csv"
    test.loadCSV(path)
    # print(test.postingDict)
    print(test.indexAnd("ability", "conversation"))
    print(test.indexOr("ability", "conversation"))
    print(test.getIndex("ability"))