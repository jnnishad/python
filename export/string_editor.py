from itertools import islice
import itertools



with open("testiter.txt","r") as f :
    linebefore = list()
    for line in f :
        linebefore.append(line.rstrip())
        if len(linebefore) > 4:
            linebefore.pop(0)
        if "of" in line:
            if len(linebefore) == 4:
                for data in range(3):
                    print(linebefore[data])
            else:
                print(''.join(linebefore))
            print("".join(line.rstrip()))
            print("".join(islice(f,3)))

