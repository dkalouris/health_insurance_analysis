import sqlite3
import pandas as pd

# Define Sqlite reading driver and path
CONNECTION_PATH = "../data/database.sqlite"
# print(CONNECTION_PATH)

# To get all tables:

class SqliteTableExplorer:
    """Represents an SqliteTable, and reads from sWqlite database

    -----Parameters-----
    name: str
        Name of the table to read from the database
    """

    def __init__(self):
        self.connection = sqlite3.connect(CONNECTION_PATH)
        self.cursor = self.connection.cursor()
    

    def get_all_tables(self):
        """
        Reads database and returns all table names in a list 
        """
        # This query returns info about table like name, and its create statement
        # but we are only interested in the name
        # Also we should exclude Crosswalk2015 and Crosswalk2016 as these contain joint result
        # of all the tables so their information is reduntant.
        self.cursor.execute("SELECT name FROM sqlite_master where type='table' and name!='Crosswalk2015' and name!='Crosswalk2016';")
        table_tuple = self.cursor.fetchall()
        # Result will be a tuple with one element
        table_names = [x[0] for x in table_tuple]
        return table_names
    
    def get_table_col_types(self, name):
        """
        Return column info for the specified table
        
        ----PARAMETERS----
        name: str
            name of the database table we want info from
        """

        # Execute the PRAGMA statement to get information about the table
        self.cursor.execute(f"PRAGMA table_info('{name}')")

        column_info_tuple = self.cursor.fetchall()
        columns_info_types = [(i[1],i[2]) for i in column_info_tuple]
        return columns_info_types 

    def read(self, name, cols=[], limit=None):
        """
        Read table from sqlite and return a pandas table
        ----PARAMETERS----
        name: str
            name of the database table we want info from
        cols: List<str>, optional
            list of columns we want to retrieve
        """
        col_clause = "*"
        if len(cols) > 0:
            col_clause = ",".join(cols)
        limit_clause = ""
        if limit!=None and limit>0:
            limit_clause = f"LIMIT {limit}"
        query = f"Select {col_clause} from '{name}' {limit_clause}"
        return pd.read_sql_query(sql=query, con=self.connection)
    
    def __del__(self):
        # As part of destroying the object, close cursor and connection
        self.cursor.close()
        self.connection.close()
    
