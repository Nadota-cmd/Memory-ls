import math, time
from pick import pick
memory = ["baby.sh","koch","ad","sed","bn","vv","s","miseryzoloto.txt","d","me"]

t = 0
def heh():
    title = "You wanna more?: "
    options = ["no(⸝⸝⩌ ⤙ ⩌⸝⸝)", "MORE MORE(>/////<) ♡"]
    india = "➤"
    option, index = pick(options, title, indicator=india)
    if option == options[0]:
        print("♡𝔾𝕆𝕆𝔻 𝔹𝕆𝕐")                                      time.sleep(0.6)                                     elif option == options[1]:
        an = input("Okey, Create a new file: ")
        print(f"\033[1;32mInput a new file!\033[0m \033[1;34m{an}\033[0m")                                              memory.append(an)
        heh()

    return option                                       def newfile():
    inpt = input("append file: ")
    print(f"\033[1;32mInput a new file!\033[0m \033[1;34m{inpt}\033[0m")                                            heh()
    memory.append(inpt)
inp = newfile()
lam = len(memory)                                       la = lam - (lam // 2)
resul = math.ceil(la)
try:
    suka = memory.sort(key=len)                             for i in range(lam):
            print(f"\033[1m{memory[i]}\033[0m", end="")
            for j in range(len(memory[-1])):
                print(" ", end="")
            if memory[i + 1] != memory[-1]:                             print(f"\033[1m{memory[i + 1]}\033[0m")
except IndexError:                                          pass
print("")