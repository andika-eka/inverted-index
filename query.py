import invertedIndex
import os

index = invertedIndex.PostingListIndex()
index.loadCSV("./output/postingList.csv")

print(" human and evaluator")
print(index.getIndex("human"))
print(index.getIndex("evaluator"))
print(index.indexAnd("human", "evaluator"))

if not os.path.exists("./queryOut"):
        os.mkdir("./queryOut")
with open("./queryOut/HumanAndEvaluator.csv", 'w') as file:
    file.write("human, " + ", ".join(map(str, index.getIndex("human")))+"\n")
    file.write("evaluator, " + ", ".join(map(str, index.getIndex("evaluator")))+"\n")
    file.write("result, " + ", ".join(map(str, index.indexAnd("human", "evaluator")))+"\n")

print(" human or machine")
print(index.getIndex("human"))
print(index.getIndex("machine"))
print(index.indexOr("human", "machine"))

if not os.path.exists("./queryOut"):
        os.mkdir("./queryOut")
with open("./queryOut/HumanOrMachine.csv", 'w') as file:
    file.write("human, " + ", ".join(map(str, index.getIndex("human")))+"\n")
    file.write("machine, " + ", ".join(map(str, index.getIndex("machine")))+"\n")
    file.write("result, " + ", ".join(map(str, index.indexOr("human", "machine")))+"\n")


print(" human and not machine")
print(index.getIndex("human"))
print(index.getIndex("machine"))
print(index.getIndex("human").difference(index.getIndex("machine")))


if not os.path.exists("./queryOut"):
        os.mkdir("./queryOut")
with open("./queryOut/HumanAndNotMachine.csv", 'w') as file:
    file.write("human, " + ", ".join(map(str, index.getIndex("human")))+"\n")
    file.write("machine, " + ", ".join(map(str, index.getIndex("machine")))+"\n")
    file.write("result, " + ", ".join(map(str, index.getIndex("human").difference(index.getIndex("machine"))))+"\n")





# print(test.indexOr("ability", "conversation"))