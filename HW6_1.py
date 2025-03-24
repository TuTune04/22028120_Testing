import unittest
import Testing_1 as sc  # type: ignore

class TestShippingCost(unittest.TestCase):
    
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            sc.s_shipping_cost(-1, -1)
    
    def test_weight_category_1(self):
        self.assertAlmostEqual(sc.s_shipping_cost(0.5, 400), 400.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(2.5, 400), 600.0, places=1)

        
    def test_weight_category_2(self):
        self.assertAlmostEqual(sc.s_shipping_cost(10, 400), 800.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(10, 600), 1320.0, places=1)
        

if __name__ == '__main__':
    unittest.main()