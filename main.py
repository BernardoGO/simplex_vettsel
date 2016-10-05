import sys
import copy

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

    def standardize_f(inp):
        pos = 1
        newfrm = ["f", 0]
        if inp[0] == "min": pos = -1
        for x in range(1,len(inp)):
            newfrm.append(inp[x]*pos)
        return newfrm

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

    def phase_1(inp):
        print("Phase 1")
        pos_fst = -1
        col_perm = -1
        for x in range(1, len(inp)):
            if inp[x][1] < 0:
                print("Found: " + str(inp[x][1]))
                pos_fst = x
                break

        if pos_fst == -1:
            print ("TO PHASE 2")
            return -2

        for y in range(2, len(inp[pos_fst])):
            #print(inp[x][y])
            if inp[pos_fst][y] < 0:
                print("Found_2: " + str(inp[pos_fst][y]))
                col_perm = y
                break

        if col_perm == -1:
            print ("IMPOSSI")
            return -1

        mnr = float("inf")
        mnr_row = -1
        for x in range(1, len(inp)):
            if (inp[x][1]<0) != (inp[x][col_perm]<0): continue
            quo = inp[x][1]/inp[x][col_perm]
            if quo <= mnr:
                mnr = quo
                mnr_row = x
        print (mnr_row)
        ew = simplex.troca(inp, mnr_row, col_perm)
        for x in range(0, len(inp)):
            for y in range(0, len(inp[0])):
                inp[x][y] = ew[x][y]
        simplex.printTable(inp)
        return 0

    def troca(inp, mnr_row, mnr_col):
        newtbl = copy.deepcopy(inp)
        elemnpr = 1/newtbl[mnr_row][mnr_col]
        print("lempr = " + str(elemnpr))
        newtbl[mnr_row][mnr_col] = elemnpr;
        simplex.printTable(newtbl)
        for x in range(1, len(inp)):
            if x == mnr_row: continue
            newtbl[x][mnr_col] = newtbl[x][mnr_col] * (-1*elemnpr)
        simplex.printTable(newtbl)
        for x in range(1, len(inp[0])):
            if x == mnr_col: continue
            newtbl[mnr_row][x] = newtbl[mnr_row][x] * (1*elemnpr)
        simplex.printTable(newtbl)

        for x in range(1, len(inp)):
            for y in range(1, len(inp[0])):
                if y == mnr_col: continue
                if x == mnr_row: continue
                newtbl[x][y] = inp[mnr_row][y] * newtbl[x][mnr_col]


        xi = newtbl[mnr_row][0]
        yi = newtbl[0][mnr_col]
        newtbl[mnr_row][0] = yi
        newtbl[0][mnr_col] = xi
        print("MULT222")
        simplex.printTable(newtbl)
        for x in range(1, len(inp)):
            for y in range(1, len(inp[0])):
                if x == mnr_row: continue
                if y == mnr_col: continue
                newtbl[x][y] += inp[x][y]
        print("ODN2")
        simplex.printTable(newtbl)
        #simplex.printTable(newtbl)

        return newtbl

    def phase_2(inp):
        print("phase 2 --")
        pos_fst = -1
        for y in range(2, len(inp[0])):
            if inp[1][y] > 0:
                print("Found: " + str(inp[1][y]))
                pos_fst = y
                break
        if pos_fst == -1:
            return -2

        for y in range(2, len(inp[pos_fst])):
            #print(inp[x][y])
            if inp[pos_fst][y] > 0:
                print("Found_2: " + str(inp[y][pos_fst]) + "=" + str(pos_fst))
                col_perm = pos_fst
                break

        if col_perm == -1:
            print ("ILIM")
            return -1

        mnr = float("inf")
        mnr_row = -1
        for x in range(1, len(inp)):
            if (inp[x][1]<0) != (inp[x][col_perm]<0): continue
            quo = inp[x][1]/inp[x][col_perm]
            if quo <= mnr:
                mnr = quo
                mnr_row = x
        print (mnr_row)
        simplex.printTable(inp)
        #input()
        print("row = " + str(mnr_row) + " col = " + str(col_perm))
        ew = simplex.troca(inp, mnr_row, col_perm)
        for x in range(0, len(inp)):
            for y in range(0, len(inp[0])):
                inp[x][y] = ew[x][y]
        simplex.printTable(inp)

        #input()
        return 0
        #return 0

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
rt = 0
while rt == 0:
    rt = simplex.phase_1(stn)

rt = 0
while rt == 0:
    rt = simplex.phase_2(stn)

#simplex.printTable(rt)
