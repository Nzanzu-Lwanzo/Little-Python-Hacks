import unittest
from typing import TypedDict,List
from .equations import EqFirstDeg

class EQ_FIRST_DEG_MOCK_VALUES(TypedDict):
    a_coeff : int
    b_coeff : int
    eq_to : int
    b_coeff_simplified : int # Will be manually calculated
    result : int # Will be manually calculated
    
class TestEqFirstDeg(unittest.TestCase):

    def setUp(self):
        self.equations:List[EQ_FIRST_DEG_MOCK_VALUES] = [
            {
                'a_coeff' : 4,
                'b_coeff' : 4,
                'eq_to' : 2,
                'b_coeff_simplified' : 2,
                'result' : -0.5
            },
            {
                'a_coeff' : 5,
                'b_coeff' : 3,
                'eq_to' : 6,
                'b_coeff_simplified' : -3,
                'result': 0.6
            },
            {
                'a_coeff' : 7,
                'b_coeff' : 2,
                'eq_to' : -8,
                'b_coeff_simplified' : 10,
                'result' : -1.4285714285714286
            }
        ]

        return super().setUp()

    def test_simplificaction(self):

        for equation in self.equations:
            with self.subTest(equation=equation):

                instance = EqFirstDeg(
                    a=equation['a_coeff'],
                    b=equation['b_coeff'],
                    c=equation['eq_to']
                )

                self.assertTupleEqual(
                    instance.terms,
                    (equation['a_coeff'],equation['b_coeff_simplified'],0)
                )
    def test_resolution(self):
        
        for equation in self.equations:
            with self.subTest(equation=equation):
                instance = EqFirstDeg(
                    a=equation['a_coeff'],
                    b=equation['b_coeff'],
                    c=equation['eq_to']
                )

                self.assertAlmostEqual(
                    instance.resolve(),
                    equation['result']
                )