import os
import subprocess
from flask import current_app
from backend.config import Config


class Deploy:
    def __init__(self, app):
        self.app = app

    def deploy(self):
        try:
            # Create a new directory for the deployment
            deployment_dir = os.path.join(Config.DEPLOYMENT_DIR, 'deployment')
            if not os.path.exists(deployment_dir):
                os.makedirs(deployment_dir)

            # Copy the application code to the deployment directory
            subprocess.run(['cp', '-r', '.', deployment_dir], check=True)

            # Install dependencies
            subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True, cwd=deployment_dir)

            # Run migrations
            subprocess.run(['python', 'migrations.py'], check=True, cwd=deployment_dir)

            # Start the application
            subprocess.run(['python', 'app.py'], check=True, cwd=deployment_dir)

        except Exception as e:
            current_app.logger.error(f'Deployment failed: {e}')
            raise

    def rollback(self):
        try:
            # Remove the deployment directory
            deployment_dir = os.path.join(Config.DEPLOYMENT_DIR, 'deployment')
            if os.path.exists(deployment_dir):
                subprocess.run(['rm', '-rf', deployment_dir], check=True)

        except Exception as e:
            current_app.logger.error(f'Rollback failed: {e}')
            raise