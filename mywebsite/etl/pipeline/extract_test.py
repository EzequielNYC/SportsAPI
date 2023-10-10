import os
import unittest
from extract import extract_data

# Testing for 3 things 
# 1. files are being put populated in the raw data folder
# 2. the files have data inside of them 
# 3. the files are being replaced with new files - since new data is added for each game played 

class TestExtractData(unittest.TestCase):

    def test_extract_data(self):

        data_folder = os.path.join(os.getcwd(), "raw_data")
        extract_data()

        leagues = {
            'nba': ['knicks', 'nets'],
            'mlb': ['yankees', 'mets'],
            'nfl': ['giants', 'jets']
        }

        for league, teams in leagues.items():
            for team in teams:
                output_file_path = os.path.join(data_folder, f"{league}_{team}.txt")

                # checking to see if the files are being populated in the raw_data folder 
                self.assertTrue(os.path.exists(output_file_path))

                # Verify that the file has data
                with open(output_file_path, "r") as f:
                    file_content = f.read()
                    self.assertNotEqual(file_content, "")

                # Check if the file was replaced with new data
                replaced = (os.stat(output_file_path).st_mtime > os.stat(__file__).st_mtime)
                self.assertTrue(replaced)

if __name__ == "__main__":
    unittest.main()
