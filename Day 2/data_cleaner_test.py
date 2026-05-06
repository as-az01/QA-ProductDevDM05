import pandas as pd
import unittest
from pandas.testing import assert_series_equal

data = pd.read_csv('data/03_Library Systembook.csv')
data.drop(16, inplace=True)

data['Book checkout'] = data['Book checkout'].str.replace('"', "", regex=True)
data['Book checkout'] = pd.to_datetime(data['Book checkout'], format='mixed')
data['Book Returned'] = pd.to_datetime(data['Book Returned'], format='mixed')

na_dropped_data = data.dropna()
data_enriched = na_dropped_data.copy()

def enrich_dateDuration(colA, colB, df=data_enriched):
    df['date_delta'] = (df[colA] - df[colB]).dt.days
    return df['date_delta']

class TestDataCleaning(unittest.TestCase):
    def test_clean_data_output(self):
        expected = (data_enriched['Book Returned'] - data_enriched['Book checkout']).dt.days
        expected.name = 'date_delta'

        result = enrich_dateDuration(
            df=data_enriched,
            colA='Book Returned',
            colB='Book checkout'
        )

        assert_series_equal(result, expected)

if __name__ == "__main__":
    unittest.main()
