import pandas as pd
import unittest
from pandas.testing import assert_frame_equal
# Data engineering metrics (instantiation)

#Read the CSV file to clean it
data = pd.read_csv('data/03_Library Systembook.csv')
# Invalid Rows
data.drop(16, inplace=True)

# RETRY Converting the date of purchase to date format
data['Book checkout'] = data['Book checkout'].str.replace('"', "", regex=True)
data['Book checkout'] = pd.to_datetime(data['Book checkout'], format='mixed' ) 
data['Book Returned'] = pd.to_datetime(data['Book Returned'], format='mixed' ) 
#print(data.head())

na_dropped_data = data.dropna()
na_dropped_data.head()

duplicate_data = na_dropped_data.duplicated()
data_enriched = na_dropped_data.copy()

def enrich_dateDuration(colA, colB, df=data_enriched):
        """
        Takes the two input columns and the dataframe to create a new column date_delta which is the difference, in days, between colA and colB.
        
        Note: ColA should be the highest of the expected date columns.
        """
        df['date_delta'] = (df[colA]-df[colB]).dt.days
        return df['date_delta']

#print(enrich_dateDuration(df=data_enriched, colA='Book Returned', colB='Book checkout'))

#class TestDataCleaning:
#        def test_clean_data_output(self):
#            input_df = data_enriched
#            expected_df = (data_enriched['Book Returned']-data_enriched['Book checkout']).dt.days
#            result_df = enrich_dateDuration(df=data_enriched, colA='Book Returned', colB='Book checkout')#

#            assert_frame_equal(result_df, expected_df)#

#if __name__ == "__main__":
#    test_runner = TestDataCleaning()
#    test_runner.test_clean_data_output()
#    print("Test passed successfully!")

from pandas.testing import assert_series_equal

class TestDataCleaning:
    def test_clean_data_output(self):
        input_df = data_enriched

        expected_series = (data_enriched['Book Returned'] - data_enriched['Book checkout']).dt.days
        expected_series.name = 'date_delta'   # match the function output name

        result_series = enrich_dateDuration(
            df=data_enriched,
            colA='Book Returned',
            colB='Book checkout'
        )

        assert_series_equal(result_series, expected_series)
          