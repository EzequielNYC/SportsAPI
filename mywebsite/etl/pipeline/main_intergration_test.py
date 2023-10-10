import os
import unittest
import sqlite3
from transform import clean_text_file
from load import insert_data_into_database
from extract import extract_data


# Testing if the pipeline performs all aspects of the ETL together, using a testing database - checks if data is uploaded successfully 
# each ETL file has been tested and works - this test is to see if they all work together 

class TestETLPipeline(unittest.TestCase):

    def setUp(self):
        # Set up the test environment amd test database
        self.database_name = 'test_database.db'
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

        # Define the data files for each team
        data_files = {
            "yankees": "mlb_yankees.txt",
            "mets": "mlb_mets.txt",
            "jets": "nfl_jets.txt",
            "giants": "nfl_giants.txt",
            "knicks": "nba_knicks.txt",
            "nets": "nba_nets.txt" 
        }

        # Create and initialize the database tables for each team
        for team_name in data_files:
            table_name = f"{team_name}_data"
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    opponent TEXT,
                    result TEXT,
                    {team_name}_score TEXT,
                    opponent_score TEXT,
                    location TEXT,
                    total_wins TEXT,
                    total_losses TEXT,
                    divisional_wins TEXT,
                    divisional_losses TEXT
                )
            """
            self.cursor.execute(create_table_query)
        self.connection.commit()

    def tearDown(self):
        # Deletes Testing Database 
        self.connection.close()
        os.remove(self.database_name)

    def test_extract_transform_load(self):
        # Testing ETL Pipeline

        # raw data folder from extraction 
        data_folder = "/Users/ezequielesparza/SportsAPI/mywebsite/etl/pipeline/raw_data"

        # Define the data files in the raw folder for each team
        data_files = {
            "yankees": "mlb_yankees.txt",
            "mets": "mlb_mets.txt",
            "jets": "nfl_jets.txt",
            "giants": "nfl_giants.txt",
            "knicks": "nba_knicks.txt",
            "nets": "nba_nets.txt" 
        }

        # Perform extraction 
        extract_data()

        # Iterate through the data files and clean/insert data
        for team_name, data_file in data_files.items():
            # Define the file path based on the data folder
            file_path = os.path.join(data_folder, data_file)

            # Clean the text file
            data = clean_text_file(file_path)

            # checking to see if data exisit in the clean files- Knicks and Nets wont have data at this moment 10/10/23
            if not data.empty:
                # Insert the populated cleaned data into the database
                insert_data_into_database(self.database_name, data, team_name)

                # Query the database and check if data is inserted correctly
                query = f"SELECT * FROM {team_name}_data"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()

                # the knicks and nets have not started playing, so there should be no data in DB
                if team_name == "knicks" or team_name == "nets":
                    if data:
                        self.assertGreater(len(rows), 0)
                    else:
                        self.assertEqual(len(rows), 0) # passes here 
                else:
                    self.assertIsNotNone(rows) # everyother team should have rows - passes
                    self.assertGreater(len(rows), 0) # len(rows) should be greater than 0 - passes

if __name__ == '__main__':
    unittest.main()
