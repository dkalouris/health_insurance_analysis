import pyspark.sql.functions as func
import pandas as pd

CSV_PATH = "../data/"

class PandasTableExplorer:
    """
    Class for exploring the tables
    """
    def __init__(self):
        pass
    
    def read_csv(self, name):
        """Read csv tables and return a pandas Dataframe

        ----Parameters----
        name: str
            Name of the csv file to read
        """
        return pd.read_csv(CSV_PATH + name + ".csv")


    def print_num_distinct_cols(self, df):
        """Print number of distinct values in each column

        ----Parameters----
        df: spark.Dataframe
            Dataframe that we want to explore
        """
        df.select([func.countDistinct(column) for column in df.columns]).show()


    def print_nan_cols(self, df):
        """Print number of nan values in each column

        ----Parameters----
        df: spark.Dataframe
            Dataframe that we want to explore
        """
        df.select([func.count(func.when(func.isnan(column), column)) for column in df.columns]).show()

    def print_null_cols(self, df):
        """Print number of null values in each column

        ----Parameters----
        df: spark.Dataframe
            Dataframe that we want to explore
        """
        df.select([func.count(func.when(func.col(column).isNull(), column)) for column in df.columns]).show()

    def explore(self, df):
        self.print_num_distinct_cols(df)
        self.print_null_cols(df)
        self.print_nan_cols(df)
