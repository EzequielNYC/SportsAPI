import os
import unittest
import sqlite3
import pandas as pd
from load import insert_data_into_database

class TestLoadingData(unittest.TestCase):

    def setUp(self):
        # Create a temporary SQLite database for testing
        self.database_name = 'test_database.db'
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def tearDown(self):
        # Close the database connection and delete the temporary database
        self.connection.close()
        os.remove(self.database_name)

    def test_insert_data_into_database(self):
        # Create a clean DataFrame with sample data
        data = pd.DataFrame([
            {'date': '01/01', 'opponent': 'A Team', 'result': 'W', 'ny_score': '5', 'opponent_score': '0', 'location': 'Home', 'total_wins': '1', 'total_losses': '0', 'divisional_wins': '0', 'divisional_losses': '0'},
            {'date': '02/02', 'opponent': 'BTeam', 'result': 'L', 'ny_score': '12', 'opponent_score': '32', 'location': 'Away', 'total_wins': '1', 'total_losses': '1', 'divisional_wins': '0', 'divisional_losses': '1'}
        ])

        # Create and initialize the database table
        team = 'test_team'
        table_name = f"{team}_data"
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                date TEXT PRIMARY KEY,
                opponent TEXT,
                result TEXT,
                {team}_score TEXT,
                opponent_score TEXT,
                location TEXT,
                total_wins TEXT,
                total_losses TEXT,
                divisional_wins TEXT,
                divisional_losses TEXT
            )
        """
        self.cursor.execute(create_table_query)

        # Insert data into the database
        insert_data_into_database(self.database_name, data, team)

        # Check if the data was inserted correctly
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        # Assert that the number of rows in the database matches the number of rows in the DataFrame
        self.assertEqual(len(rows), len(data))

if __name__ == "__main__":
    unittest.main()
