import sys
import copy
import json

class simplex:
    cntfolg = 1

    #Reset Variables
    def reset():
        simplex.cntfolg = 1

    #Transform a restriction into one in the standard form
    def standardize_r(inp):
        pos = 1
        newfrm = []
        for x in range(len(inp)):
            if isinstance(inp[x], str):

                # Introducing new variables
                if '>' in inp[x]: pos = -1
                newfrm.extend([simplex.cntfolg+2,inp[x+1]*pos])
                simplex.cntfolg+=1

                for y in range(len(inp)-1):
                    if y == x: continue
                    newfrm.append(inp[y]*pos)
                break
        return newfrm

    #Transform the objective function into one in the standard form
    def standardize_f(inp):
        pos = 1
        newfrm = ["f", 0]
        if inp[0] == "min": pos = -1
        for x in range(1,len(inp)):
            newfrm.append(inp[x]*pos)
        return newfrm

    #Transform the linear program to one in standard form
    def standardize(inp):
        fp = simplex.standardize_f(inp[0])
        sd = (["vnb", "ml"])
        sd.extend(x+1 for x in range(len(fp)-2))
        newtable = [sd,fp]
        for x in range(1, len(inp)):
            newtable.append(simplex.standardize_r(inp[x]))
        return newtable

    def printTable(inp):
        for x in inp:
            print(x)

    def phase_1(inp):
        print("Phase 1")
        pos_fst = col_perm = -1

        for x in range(2, len(inp)):
            if inp[x][1] < 0:
                print("Found: " + str(inp[x][1]))
                pos_fst = x
                break

        # There is no negative row, what leads us to the second phase
        if pos_fst == -1:
            print ("TO PHASE 2")
            return -2

        # Find the column for the feasible region
        for y in range(2, len(inp[pos_fst])):
            #print(inp[x][y])
            if inp[pos_fst][y] < 0:
                print("Found_2: " + str(inp[pos_fst][y]))
                col_perm = y
                break

        # There is no negative variable for the selected row, what characterizes an unfeasible solution
        if col_perm == -1:
            print ("Infeasible")
            return -1

        # Find the row for the feasible region
        mnr = float("inf")
        mnr_row = -1
        for x in range(2, len(inp)):
            if (inp[x][1]<0) != (inp[x][col_perm]<0): continue
            quo = inp[x][1]/inp[x][col_perm] if inp[x][col_perm] > 0 else float("inf")
            if quo <= mnr:
                mnr = quo
                mnr_row = x
        print (mnr_row)

        ew = simplex.troca(inp, mnr_row, col_perm)

        # Replace old values for the new values
        for x in range(0, len(inp)):
            for y in range(0, len(inp[0])):
                inp[x][y] = ew[x][y]

        simplex.printTable(inp)
        return 0

    def troca(inp, mnr_row, mnr_col):

        newtbl = copy.deepcopy(inp)

        # Calculate and set new pivot
        elemnpr = 1/newtbl[mnr_row][mnr_col]
        print("lempr = " + str(elemnpr))
        newtbl[mnr_row][mnr_col] = elemnpr;
        simplex.printTable(newtbl)

        # Calculate new values for the feasible row
        for x in range(1, len(inp)):
            if x == mnr_row: continue
            newtbl[x][mnr_col] = newtbl[x][mnr_col] * (-1*elemnpr)
        simplex.printTable(newtbl)

        # Calculate new values for the feasible column
        for x in range(1, len(inp[0])):
            if x == mnr_col: continue
            newtbl[mnr_row][x] = newtbl[mnr_row][x] * (1*elemnpr)
        simplex.printTable(newtbl)

        # Calculate new values for the rest of the table
        for x in range(1, len(inp)):
            for y in range(1, len(inp[0])):
                if y == mnr_col: continue
                if x == mnr_row: continue
                newtbl[x][y] = inp[mnr_row][y] * newtbl[x][mnr_col]

        # Switch column/row
        xi = newtbl[mnr_row][0]
        yi = newtbl[0][mnr_col]
        newtbl[mnr_row][0] = yi
        newtbl[0][mnr_col] = xi


        print("MULT222")
        simplex.printTable(newtbl)

        # Calculate the sum for the new table
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
        col_perm = -1
        pos_fst = -1
        for y in range(2, len(inp[0])):
            if inp[1][y] > 0:
                print("Found: " + str(inp[1][y]))
                pos_fst = y
                break

        # There is no positive variable for the function row, what characterizes an optimal solution
        if pos_fst == -1:
            print ("Optimal")
            if inp[1][1] < 0: inp[1][1] *=-1
            simplex.printTable(inp)
            return -2

        for y in range(2, len(inp[pos_fst])):
            #print(inp[x][y])
            if inp[pos_fst][y] > 0:
                print("Found_2: " + str(inp[y][pos_fst]) + "=" + str(pos_fst))
                col_perm = pos_fst
                break

        # There is no negative variable for the selected row, what characterizes an unfeasible solution
        if col_perm == -1:
            print ("Unbounded")
            return -1

        # Find the row for the feasible region
        mnr = float("inf")
        mnr_row = -1
        for x in range(1, len(inp)):
            if (inp[x][1]<0) != (inp[x][col_perm]<0): continue
            quo = inp[x][1]/inp[x][col_perm] if inp[x][col_perm] > 0 else float("inf")
            if quo <= mnr:
                mnr = quo
                mnr_row = x
        print (mnr_row)
        simplex.printTable(inp)
        #input()
        print("row = " + str(mnr_row) + " col = " + str(col_perm))
        ew = simplex.troca(inp, mnr_row, col_perm)

        #Replace values
        for x in range(0, len(inp)):
            for y in range(0, len(inp[0])):
                inp[x][y] = ew[x][y]
        simplex.printTable(inp)

        #input()
        return 0
        #return 0


    def execute(stn):
        rt = 0
        status = ''
        while rt == 0:

            rt = simplex.phase_1(stn)

        if rt == -1:
            print("DONE")
            status = 'impossivel'
        else:
            rt = 0
            while rt == 0:
                rt = simplex.phase_2(stn)

        if rt == -2:
            status = "otimo"
        elif rt == -1:
            status = "ilimitada"
        return simplex.toJSON(stn, status)

    def toJSON(inp, status):
        dic = {}
        dic['status'] = status
        for x in inp:
            if 'vnb' in x: continue
            s = str(x[0]) if 'f' in str(x[0]) else 'x' + str(x[0])
            dic[str(s)] = x[1]
        for x in inp[0]:
            if isinstance(x,str): continue
            s = str(x) if 'f' in str(x) else 'x' + str(x)
            dic[str(s)] = 0
        xx = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ': '))
        print(xx)
        return xx

###TESTS


#r1 =[8,2,'>=',16]
#simplex.standardize_r(r1)

#f = ["max",1,2]
#simplex.standardize_f(f)


def test01():
    #numero 3 da lista de simplex
    f = ["min", 7, 8.5]
    r1 = [0.6, 0.8, ">=", 16]
    r2 = [24, 20, "<=", 1800]

    table = [f,r1,r2]
    simplex.reset()
    stn = simplex.standardize(table)
    simplex.printTable(stn)
    rt = 0
    while rt == 0:
        rt = simplex.phase_1(stn)

    rt = 0
    while rt == 0:
        rt = simplex.phase_2(stn)

    #simplex.printTable(rt)

#inp[x][1]/inp[x][col_perm] if inp[x][col_perm] > 0 else float("inf")
def test03():
    #Numero 1 da lista de simplex
    f = ["max", 14, 22]
    r1 = [2, 4, "<=", 250]
    r2 = [5, 8, ">=", 460]
    r3 = [1, 0, "<=", 40]

    table = [f,r1,r2,r3]
    simplex.reset()
    stn = simplex.standardize(table)
    simplex.printTable(stn)
    simplex.execute(stn)

def test02():
    #Numero 1 da lista de simplex
    f = ["min", 1, 2]
    r1 = [8, 2, ">=", 16]
    r2 = [1, 1, "<=", 6]
    r3 = [2, 7, ">=", 28]

    table = [f,r1,r2,r3]
    simplex.reset()
    stn = simplex.standardize(table)
    simplex.printTable(stn)
    json = simplex.execute(stn)
    #simplex.toJSON(stn)

test02()
