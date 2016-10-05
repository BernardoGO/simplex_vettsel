class simplex:
    cntfolg = 1
    def standardize_r(inp):
        pos = 1
        newfrm = []
        for x in range(len(inp)):
            if isinstance(inp[x], str):
                if '>' in inp[x]: pos = -1
                newfrm.extend([simplex.cntfolg+2,inp[x+1]*pos])
                simplex.cntfolg+=1
                for y in range(len(inp)-1):
                    if y == x: continue
                    newfrm.append(inp[y]*pos)
                break
        return newfrm
        #print (newfrm)

    def standardize_f(inp):
        pos = 1
        newfrm = ["f", 0]
        if inp[0] == "min": pos = -1
        for x in range(1,len(inp)):
            newfrm.append(inp[x]*pos)
        return newfrm
        #print (newfrm)

    def standardize(inp):
        fp = simplex.standardize_f(inp[0])
        sd = (["vnb", "ml"])
        sd.extend(x+1 for x in range(len(fp)-2))
        newtable = []
        newtable.append(sd)
        newtable.append(fp)
        for x in range(1, len(inp)):
            newtable.append(simplex.standardize_r(inp[x]))
        return newtable

    def printTable(inp):
        for x in inp:
            print(x)




#r1 =[8,2,'>=',16]
#simplex.standardize_r(r1)

#f = ["max",1,2]
#simplex.standardize_f(f)


f = ["min", 7, 8.5]
r1 = [0.6, 0.8, ">=", 16]
r2 = [24, 20, "<=", 1800]

table = [f,r1,r2]
stn = simplex.standardize(table)
simplex.printTable(stn)
