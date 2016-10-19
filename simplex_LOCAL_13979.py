import sys
import copy
from enum import Enum

class Result(Enum):
    optimal = 1
    infeasible = 2
    unbounded = 3
    multi = 4


class Simplex(object):
    cntfolg = 1

    def __init__(self):
        self.reset()

    #Reset Variables
    def reset(self):
        self.cntfolg = 1

    #Transform a restriction into one in the standard form
    def standardize_r(self, inp):
        pos = 1
        newfrm = []
        for x in range(len(inp)):
            if isinstance(inp[x], str):

                # Introducing new variables
                if '>' in inp[x]: pos = -1
                newfrm.extend([self.cntfolg+2,inp[x+1]*pos])
                self.cntfolg+=1

                for y in range(len(inp)-1):
                    if y == x: continue
                    newfrm.append(inp[y]*pos)
                break
        return newfrm

    #Transform the objective function into one in the standard form
    def standardize_f(self, inp):
        pos = 1
        newfrm = ["f", 0]
        if inp[0] == "min": pos = -1
        for x in range(1,len(inp)):
            newfrm.append(inp[x]*pos)
        return newfrm

    #Transform the linear program to one in standard form
    def standardize(self, inp):
        fp = self.standardize_f(inp[0])
        sd = (["vnb", "ml"])
        sd.extend(x+1 for x in range(len(fp)-2))
        newtable = [sd,fp]
        for x in range(1, len(inp)):
            newtable.append(self.standardize_r(inp[x]))
        return newtable

    def print_table(self, inp):
        for x in inp:
            print(x)

    def phase_1(self, inp):
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

        ew = self.troca(inp, mnr_row, col_perm)

        # Replace old values for the new values
        for x in range(0, len(inp)):
            for y in range(0, len(inp[0])):
                inp[x][y] = ew[x][y]

        self.print_table(inp)
        return 0

    def troca(self, inp, mnr_row, mnr_col):

        newtbl = copy.deepcopy(inp)

        # Calculate and set new pivot
        elemnpr = 1/newtbl[mnr_row][mnr_col]
        print("lempr = " + str(elemnpr))
        newtbl[mnr_row][mnr_col] = elemnpr;
        self.print_table(newtbl)

        # Calculate new values for the feasible row
        for x in range(1, len(inp)):
            if x == mnr_row: continue
            newtbl[x][mnr_col] = newtbl[x][mnr_col] * (-1*elemnpr)
        self.print_table(newtbl)

        # Calculate new values for the feasible column
        for x in range(1, len(inp[0])):
            if x == mnr_col: continue
            newtbl[mnr_row][x] = newtbl[mnr_row][x] * (1*elemnpr)
        self.print_table(newtbl)

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
        self.print_table(newtbl)

        # Calculate the sum for the new table
        for x in range(1, len(inp)):
            for y in range(1, len(inp[0])):
                if x == mnr_row: continue
                if y == mnr_col: continue
                newtbl[x][y] += inp[x][y]

        print("ODN2")
        self.print_table(newtbl)

        return newtbl

    def phase_2(self, inp):
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
            self.print_table(inp)
            return -2

        for y in range(2, len(inp[pos_fst])):
            if inp[pos_fst][y] > 0:
                print("Found_2: " + str(inp[y][pos_fst]) + "=" + str(pos_fst))
                col_perm = pos_fst
                break

        # There is no negative variable for the selected row, what characterizes an unfeasible solution
        if col_perm == -1:
            print ("Unbounded")
            return -3

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
        self.print_table(inp)
        print("row = " + str(mnr_row) + " col = " + str(col_perm))
        ew = self.troca(inp, mnr_row, col_perm)

        #Replace values
        for x in range(0, len(inp)):
            for y in range(0, len(inp[0])):
                inp[x][y] = ew[x][y]
        self.print_table(inp)

        return 0

    def execute(self, stn):
        rt = 0

        while rt == 0:
            rt = self.phase_1(stn)

        # first fase results:
        # -2 --> go phase2
        # -1 --> Infeasible

        if rt == -1:
            print("DONE")
            return { "status": Result.infeasible, "table": stn }
        else:
            rt = 0
            while rt == 0:
                rt = self.phase_2(stn)

        if rt == -3:
            print("DONE")
            return { "status": Result.unbounded, "table": stn }

        # first fase results:
        # -2 --> Optimal
        # -3 --> Unbounded

        return { "status": Result.optimal, "table": stn }
