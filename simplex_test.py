#!/usr/bin/python3

from simplex import Simplex, Result

class Test(object):

    def test01(self):
        #Numero 1 da lista de simplex
        f = ["min", 1, 2]
        r1 = [8, 2, ">=", 16]
        r2 = [1, 1, "<=", 6]
        r3 = [2, 7, ">=", 28]

        simplex = Simplex()
        table = [f,r1,r2,r3]
        simplex.reset()
        stn = simplex.standardize(table)
        simplex.print_table(stn)
        print(simplex.execute(stn))

    def test02(self):
        #Numero 2 da lista de simplex
        f = ["max", 38, 49]
        r1 = [1, 1.5, "<=", 160]
        r2 = [2.5, 2.5, "<=", 256]
        r3 = [0, 1, ">=", 40]

        simplex = Simplex()
        table = [f,r1,r2,r3]
        simplex.reset()
        stn = simplex.standardize(table)
        simplex.print_table(stn)
        print(simplex.execute(stn))

    def test03(self):
        #numero 3 da lista de simplex
        f = ["min", 7, 8.5]
        r1 = [0.6, 0.8, ">=", 16]
        r2 = [24, 20, "<=", 1800]

        simplex = Simplex()
        table = [f,r1,r2]
        stn = simplex.standardize(table)
        simplex.print_table(stn)
        print(simplex.execute(stn))

if __name__ == '__main__':
    test = Test()
    test.test01()
    #test.test02()
    #test.test03()
