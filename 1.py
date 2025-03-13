import unittest
import Testing_1 as sc  # type: ignore

class TestShippingCost(unittest.TestCase):
    
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            sc.s_shipping_cost(-1, -1)
        with self.assertRaises(ValueError):
            sc.s_shipping_cost(2, -50)
        with self.assertRaises(ValueError):
            sc.s_shipping_cost(-3, 200)
    
    def test_weight_category_1(self):
        self.assertAlmostEqual(sc.s_shipping_cost(0.5, 400), 400.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(2.5, 600), 990.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(10, 600), 1320.0, places=1)
        
    def test_weight_category_2(self):
        self.assertAlmostEqual(sc.s_shipping_cost(2, 100), 150.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(5, 300), 450.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(3, 600), 990.0, places=1)
        
    def test_weight_category_3(self):
        self.assertAlmostEqual(sc.s_shipping_cost(6, 200), 400.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(10, 500), 1000.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(7, 700), 1540.0, places=1)
        
    def test_boundary_values(self):
        self.assertAlmostEqual(sc.s_shipping_cost(1, 100), 100.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(1.01, 100), 150.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(5, 100), 150.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(5.01, 100), 200.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(2, 500), 750.0, places=1)
        self.assertAlmostEqual(sc.s_shipping_cost(2, 500.01), 825.01665, places=1)

if __name__ == '__main__':
    unittest.main()