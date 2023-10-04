import schedule
import time
import subprocess

def run_pipeline():
    # Specify the command to run your main.py script
    command = "python main.py"

    # Run the script using subprocess
    subprocess.call(command, shell=True)

# Schedule the job to run daily
schedule.every().day.at("00:00").do(run_pipeline)

# Run the scheduled jobs continuously
while True:
    # Run any pending jobs
    schedule.run_pending()
  
    # Wait for 1 second
    time.sleep(1)
