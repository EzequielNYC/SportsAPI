from django.core.management.base import BaseCommand
import subprocess
from mywebsite.settings import ETL_SCRIPT_PATH

class Command(BaseCommand):
    help = 'Run the ETL script'

    def handle(self, *args, **options):
        try:
            subprocess.run(['python', ETL_SCRIPT_PATH], check=True)
            self.stdout.write(self.style.SUCCESS('ETL script executed successfully.'))
        except subprocess.CalledProcessError as e:
            self.stderr.write(self.style.ERROR(f'Error executing ETL script: {e}'))
