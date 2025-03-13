import unittest
import Testing_2 as cf  # type: ignore

class TestCheckFail(unittest.TestCase):
    
    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            cf.check_fail(-1, -1)

    def test_pass_conditions(self):
        self.assertEqual(cf.check_fail(6, 0), "Pass")
        self.assertEqual(cf.check_fail(3, 2), "Fail")
    

if __name__ == '__main__':
    unittest.main()