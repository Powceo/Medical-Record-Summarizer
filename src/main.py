#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Medical Record Summarizer
Main application entry point
"""

import sys
import os
import logging
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSettings
from dotenv import load_dotenv

# Import application modules
from ui.main_window import MainWindow
from core.config import Config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def setup_environment():
    """Set up the application environment"""
    # Load environment variables from .env file if it exists
    load_dotenv()
    
    # Check for Google Cloud credentials
    if not os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'):
        # Look for credentials file in the project directory
        credentials_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                       'google_credentials.json')
        if os.path.exists(credentials_path):
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
            logger.info(f"Using Google credentials from: {credentials_path}")
        else:
            logger.warning("Google Cloud credentials not found. OCR functionality will be limited.")

def main():
    """Main application entry point"""
    # Set up environment
    setup_environment()
    
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Medical Record Summarizer")
    app.setOrganizationName("Powceo")
    
    # Load configuration
    config = Config()
    
    # Create and show the main window
    main_window = MainWindow(config)
    main_window.show()
    
    # Start the application event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()