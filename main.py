class simplex:
    def standardize_r(inp):
        pos = 1
        newfrm = []
        for x in range(len(inp)):
            if isinstance(inp[x], str):
                if '>' in inp[x]: pos = -1
                newfrm.extend([1,inp[x+1]*pos])
                for y in range(len(inp)-1):
                    if y == x: continue
                    newfrm.append(inp[y]*pos)
                break
        print (newfrm)

    def standardize_f(inp):
        pos = 1
        newfrm = [0]
        if inp[0] == "min": pos = -1
        for x in range(1,len(inp)):
            newfrm.append(inp[x]*pos)
        print (newfrm)



r1 =[8,2,'>=',16]
simplex.standardize_r(r1)

f = ["max",1,2]
simplex.standardize_f(f)
