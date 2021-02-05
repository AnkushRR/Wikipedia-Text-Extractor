import wikipedia
import os

inpt = open("pageTitleList.txt", "r")
lines = inpt.readlines()
try:
    os.mkdir("output")
except FileExistsError:
    pass

for line in lines:
    line = line.strip()
    print("Looking for: \""+line+"\"")
    try:
        page = wikipedia.page(line)
        print("found: \""+line+"\"")
        f = open("output/"+page.title+".txt", "w")
        f.write(page.content)
        f.close()
        print("Written to file: output/"+line+".txt \n--------------------------------------------------\n")
    except Exception as e:
        print(e)
        print("Skipping fetch for \""+line+"\" \n--------------------------------------------------\n")
    

