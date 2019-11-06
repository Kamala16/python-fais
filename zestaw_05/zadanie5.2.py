import fracs 
import unittest

class Testfracs(unittest.TestCase):

    def setUp(self):
        self.pierwszy = [2,1]
        self.drugi = [2, 3]
        self.trzeci = [-2, 5]
        self.czwarty = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac(self.pierwszy, self.drugi), [8, 3])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac(self.pierwszy, self.drugi), [4, 3])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac(self.pierwszy, self.drugi), [4, 3])

    def test_div_frac(self): 
        self.assertEqual(fracs.div_frac(self.pierwszy, self.drugi), [6, 2])

    def test_is_positive(self):
        self.assertFalse(fracs.is_positive(self.trzeci))

    def test_is_zero(self):
        self.assertTrue(fracs.is_zero(self.czwarty))

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac(self.pierwszy, self.drugi), -1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float(self.trzeci), -0.4)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()


    


