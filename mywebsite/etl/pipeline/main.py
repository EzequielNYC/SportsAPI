import os
from transform import clean_text_file
from load import insert_data_into_database
from extract import extract_data

# Specify the full path to the raw data folder
data_folder = "/Users/ezequielesparza/SportsAPI/mywebsite/etl/pipeline/raw_data"

# pipeline to database 
database_name = "/Users/ezequielesparza/SportsAPI/mywebsite/db.sqlite3"

extract_data()

# Define the data files for each team
data_files = {
    "yankees": "mlb_yankees.txt",
    "mets": "mlb_mets.txt",
    "jets": "nfl_jets.txt",
    "giants": "nfl_giants.txt",
    "knicks": "nba_knicks.txt",
    "nets": "nba_nets.txt" 
}

# Iterate through the data files and clean/insert data
for team_name, data_file in data_files.items():
    # Define the file path based on the data folder
    file_path = os.path.join(data_folder, data_file)

    data = clean_text_file(file_path)

    insert_data_into_database(database_name, data, team_name)

    # Show success message
    print(f"Data for {team_name} cleaned and inserted into the database.")

print("All data processed successfully.")

