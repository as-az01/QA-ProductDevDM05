import unittest
import hello

class TestOperations(unittest.TestCase):
        def setUp(self):
             self.calc = Calculator(8,2)

        def test_enrich(self):
            calc = Calculator(8, 2)
            self.assertEqual(calc.enrich_dateDuration(), ??, "??")

expected_res=pd.Series([7,9,11,13,15])
pd.testing.assert_series_equal((df1['a']+df2['a']),expected_res,check_names=False)

if __name__ == "__main__":
      unittest.main()