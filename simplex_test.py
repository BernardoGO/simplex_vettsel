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
        stn = simplex.standardize(table)
        result = simplex.execute(stn)

        expected_result = [['vnb', 'ml', 3, 1],
                ['f', 170.00000000000003, -10.624999999999998, -0.6249999999999993],
                [4, 1400.0, 25.0, 9.000000000000002],
                [2, 20.00000000000001, -1.2499999999999998, 0.7499999999999999]]

        self.assertTrue(result['table'] == expected_result)

if __name__ == '__main__':
    unittest.main()
