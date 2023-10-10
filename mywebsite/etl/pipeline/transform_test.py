import unittest
from transform import clean_text_file
import os 

# creating an example file with same structred data in the raw data format 
# using this example file to see if the transform function is cleaning correctly 
# if the expected data should == the output of the cleaning function - tests pass


class TestCleaningData(unittest.TestCase):

    def test_clean_file(self):
        # examlpe raw file - with Opponent having either 1 name or 2 names, everything else is uniform
        lines = ['Date Opponent Result Location W/L Div', 
                 '01/01 A Team W 5-0 Home 1-0 0-0',
                 '02/02 BTeam L 12-32 Away 1-1 0-1'] 
        
        # creating the example file
        filename = 'example_file.txt'
        with open(filename,'w') as file:
            for line in lines:
                file.write(line+"\n")

        # calling the actual cleaning function 
        clean_df = clean_text_file(filename)

        # what the data would look like in dict format after being cleaned : easier to compare dicts than pandas DF 
        expected_data = [
            {'date': '01/01', 'opponent': 'A Team', 'result': 'W', 'ny_score': '5', 'opponent_score': '0', 'location': 'Home', 'total_wins': '1', 'total_losses': '0', 'divisional_wins': '0', 'divisional_losses': '0'},
            {'date': '02/02', 'opponent': 'BTeam', 'result': 'L', 'ny_score': '12', 'opponent_score': '32', 'location': 'Away', 'total_wins': '1', 'total_losses': '1', 'divisional_wins': '0', 'divisional_losses': '1'}
        ]


        # turning the data from clean_text_file funciton output to dict to compare with expected data
        clean_df_dict = clean_df.to_dict(orient='records')

        # making sure the expected data and actual data equal eachother - passes for one passes for all. Data is very uniform, they all share the same column names and data formatting
        self.assertEqual(clean_df_dict, expected_data)


        # delete the test file 
        try:
            os.remove(filename)
            print(f"File '{filename}' deleted successfully.")
        except OSError as e:
            print(f"Error deleting the file: {e}")

if __name__ == "__main__":
    unittest.main()

