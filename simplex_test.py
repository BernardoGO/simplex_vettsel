#!/usr/bin/python3

from simplex import Simplex, Result
import unittest

class Test(unittest.TestCase):

    def test_case_1(self):
        #Numero 1 da lista de simplex
        f = ["min", 1, 2]
        r1 = [8, 2, ">=", 16]
        r2 = [1, 1, "<=", 6]
        r3 = [2, 7, ">=", 28]

        simplex = Simplex()
        table = [f,r1,r2,r3]
        simplex.reset()
        stn = simplex.standardize(table)
        result = simplex.execute(stn)

        expected_result =[['vnb', 'ml', 5, 3],
                ['f', 8.461538461538462, -0.2692307692307692, -0.05769230769230768],
                [2, 3.6923076923076925, -0.15384615384615385, 0.038461538461538464],
                [1, 1.076923076923077, 0.03846153846153846, -0.1346153846153846],
                [4, 1.2307692307692306, 0.11538461538461539, 0.09615384615384615]]

        self.assertTrue(result['table'] == expected_result)

    def test_case_2(self):
        #Numero 2 da lista de simplex
        f = ["max", 38, 49]
        r1 = [1, 1.5, "<=", 160]
        r2 = [2.5, 2.5, "<=", 256]
        r3 = [0, 1, ">=", 40]

        simplex = Simplex()
        table = [f,r1,r2,r3]
        simplex.reset()
        stn = simplex.standardize(table)
        result = simplex.execute(stn)

        expected_result = [['vnb', 'ml', 1, 4],
                ['f', 5017.6, -11.0, -19.6],
                [3, 6.399999999999977, -0.5000000000000002, -0.6000000000000001],
                [2, 102.4, 1.0, 0.4],
                [5, 62.400000000000006, 1.0, 0.4]]

        self.assertTrue(result['table'] == expected_result)

    def test_case_3(self):
        #numero 3 da lista de simplex
        f = ["min", 7, 8.5]
        r1 = [0.6, 0.8, ">=", 16]
        r2 = [24, 20, "<=", 1800]

        simplex = Simplex()
        table = [f,r1,r2]
        simplex.reset()
        stn = simplex.standardize(table)
        result = simplex.execute(stn)

        expected_result = [['vnb', 'ml', 3, 1],
                ['f', 170.00000000000003, -10.624999999999998, -0.6249999999999993],
                [4, 1400.0, 25.0, 9.000000000000002],
                [2, 20.00000000000001, -1.2499999999999998, 0.7499999999999999]]

        self.assertTrue(result['table'] == expected_result)

    def test_case_sens(self):
        #sensibilidade
        """
        f = ["max", 40, 30]
        r1 = [2/5, 1/2, "<=", 20]
        r2 = [0, 1/5, "<=", 5]
        r3 = [3/5, 3/10, "<=", 21]
        """
        f = ["max", 1, 1.5]
        r1 = [2, 2, "<=", 160]
        r2 = [1, 2, "<=", 120]
        r3 = [4, 2, "<=", 280]

        simplex = Simplex()
        table = [f,r1,r2,r3]
        simplex.reset()
        stn = simplex.standardize(table)
        result = simplex.execute(stn)
        """
        expected_result = [['vnb', 'ml', 3, 1],
                ['f', 170.00000000000003, -10.624999999999998, -0.6249999999999993],
                [4, 1400.0, 25.0, 9.000000000000002],
                [2, 20.00000000000001, -1.2499999999999998, 0.7499999999999999]]

        self.assertTrue(result['table'] == expected_result)
        ###//////////////////////
        simplex.print_table(result["table"])
        x1 = result["table"][4][1]
        x2 = result["table"][2][1]
        res = result["table"][1][1]
        perm1 = result["table"][0][-1]-len(table)+2
        perm2 = result["table"][0][-2]-len(table)+2
        ss1 = simplex.standardize_r(table[perm1])
        tt1 = (ss1[1]/ss1[3])*-1
        pp1 = (ss1[2]/ss1[3])*-1

        ss2 = simplex.standardize_r(table[perm2])
        tt2 = (ss2[1]/ss2[3])*-1
        pp2 = (ss2[2]/ss2[3])*-1

        ttt = [pp2,pp1]
        minc2 = (f[1]*-1)/min(ttt)
        minc1 = min(ttt)*(f[2]*-1)

        maxc2 = (f[1]*-1)/max(ttt)
        maxc1 = max(ttt)*(f[2]*-1)

        sens = [[minc1, maxc1], [minc2, maxc2]]
        print(sens)

        """
        simplex.print_table(result["table"])




if __name__ == '__main__':
    unittest.main()
