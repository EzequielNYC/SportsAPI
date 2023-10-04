import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

def extract_data():
    # Path to chromedriver executable
    chrome_driver_path = '/usr/local/bin/chromedriver'

    # Set up ChromeDriver service
    chrome_service = ChromeService(chrome_driver_path)
    chrome_service.start()

    # Initialize the Chrome browser with the service
    browser = webdriver.Chrome(service=chrome_service)

    # Leagues and teams
    leagues = {
        'nba': ['knicks', 'nets'],
        'mlb': ['yankees', 'mets'],
        'nfl': ['giants', 'jets']
    }

    # Iterate through the leagues and teams
    for league, teams in leagues.items():
        for team in teams:
            # Construct the URL for the team
            if league == 'nba':
                if team == 'nets':
                    url = "https://www.teamrankings.com/nba/team/brooklyn-nets"
                else:
                    url = f"https://www.teamrankings.com/nba/team/new-york-{team}"
            elif league == 'mlb':
                url = f"https://www.teamrankings.com/mlb/team/new-york-{team}"
            elif league == 'nfl':
                url = f"https://www.teamrankings.com/nfl/team/new-york-{team}"

            # Access the website
            browser.get(url)

            table = browser.find_element(By.ID, 'DataTables_Table_0')

            # Define the full path to the "raw_data" folder
            data_folder = os.path.join(os.getcwd(), "raw_data")

            # Define the full path to the output file
            output_file_path = os.path.join(data_folder, f"{league}_{team}.txt")

            # Check if the file already exists
            if os.path.exists(output_file_path):
                # Remove the existing file
                os.remove(output_file_path)

            # Write the table.text to the output file
            with open(output_file_path, "w") as f:
                f.write(table.text)

    # Close the Chrome driver
    browser.quit()

# Call the extract_data() function to perform the extraction
extract_data()
