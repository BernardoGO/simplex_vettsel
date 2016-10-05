class simplex:
    def standardize(inp):
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




r1 =[8,2,'>=',16]
simplex.standardize(r1)
