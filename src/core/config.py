#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Configuration module for the Medical Record Summarizer application
"""

import os
import json
import logging
from PyQt5.QtCore import QSettings

logger = logging.getLogger(__name__)

class Config:
    """Configuration manager for the application"""
    
    DEFAULT_CONFIG = {
        "app": {
            "name": "Medical Record Summarizer",
            "version": "1.0.0",
            "theme": "light",
            "recent_files": [],
            "max_recent_files": 10
        },
        "ocr": {
            "engine": "google",  # Options: google, tesseract
            "language": "en",
            "dpi": 300,
            "enhance_image": True
        },
        "summarization": {
            "model": "default",
            "max_length": 500,
            "min_length": 100,
            "extract_entities": True,
            "medical_terms_highlight": True
        },
        "export": {
            "default_format": "pdf",  # Options: pdf, docx, txt, html
            "default_directory": "",
            "include_original_text": False,
            "include_metadata": True
        },
        "ui": {
            "font_size": 10,
            "window_width": 1200,
            "window_height": 800,
            "show_toolbar": True,
            "show_statusbar": True
        }
    }
    
    def __init__(self):
        """Initialize the configuration"""
        self.settings = QSettings()
        self.config = self.DEFAULT_CONFIG.copy()
        self.load_config()
    
    def load_config(self):
        """Load configuration from QSettings"""
        # Load from QSettings if available
        if self.settings.contains("config"):
            stored_config = json.loads(self.settings.value("config"))
            # Update default config with stored values
            self._update_dict_recursive(self.config, stored_config)
            logger.info("Configuration loaded from settings")
        else:
            logger.info("Using default configuration")
            self.save_config()
    
    def save_config(self):
        """Save configuration to QSettings"""
        self.settings.setValue("config", json.dumps(self.config))
        self.settings.sync()
        logger.info("Configuration saved to settings")
    
    def get(self, section, key=None):
        """Get a configuration value or section"""
        if section not in self.config:
            logger.warning(f"Configuration section '{section}' not found")
            return None
        
        if key is None:
            return self.config[section]
        
        if key not in self.config[section]:
            logger.warning(f"Configuration key '{key}' not found in section '{section}'")
            return None
        
        return self.config[section][key]
    
    def set(self, section, key, value):
        """Set a configuration value"""
        if section not in self.config:
            logger.warning(f"Configuration section '{section}' not found")
            return False
        
        if key not in self.config[section]:
            logger.warning(f"Configuration key '{key}' not found in section '{section}'")
            return False
        
        self.config[section][key] = value
        self.save_config()
        return True
    
    def add_recent_file(self, file_path):
        """Add a file to the recent files list"""
        recent_files = self.config["app"]["recent_files"]
        
        # Remove if already exists
        if file_path in recent_files:
            recent_files.remove(file_path)
        
        # Add to the beginning of the list
        recent_files.insert(0, file_path)
        
        # Trim list if needed
        max_files = self.config["app"]["max_recent_files"]
        if len(recent_files) > max_files:
            recent_files = recent_files[:max_files]
        
        self.config["app"]["recent_files"] = recent_files
        self.save_config()
    
    def _update_dict_recursive(self, target, source):
        """Update a dictionary recursively"""
        for key, value in source.items():
            if key in target and isinstance(target[key], dict) and isinstance(value, dict):
                self._update_dict_recursive(target[key], value)
            elif key in target:
                target[key] = value