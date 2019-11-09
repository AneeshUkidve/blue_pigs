import winsound
import time
import letters

sentence=input("\nEnter something to write: ")

def bleat(sty):
    for i in sty:
        if i==".":
            winsound.Beep(700,200)
        elif i=="-":
            winsound.Beep(700,600)
                          
            
def leti(sad):
    for i in letters.letters:
        if i[0] == sad:
            print(i[1], end="|")
            bleat(i[1])

print("\nMORSE   ",end="")

for index in sentence:
    if index == " ":
        time.sleep(1.2)
        print("    ", end="")
    else:
        time.sleep(0.6)
        dar=index.lower()
        leti(dar)

print()
input("\nPress Enter To Exit")
