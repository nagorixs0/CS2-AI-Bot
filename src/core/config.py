#!/usr/bin/env python3
"""
CS2 AI Bot - Configuration Management

This module handles loading and managing bot configuration.
"""

import yaml
import logging
from pathlib import Path
from typing import Any, Dict, Optional


class Config:
    """Configuration manager for CS2 AI Bot"""
    
    def __init__(self, config_path: Optional[Path] = None):
        """Initialize configuration
        
        Args:
            config_path: Path to configuration file
        """
        self.logger = logging.getLogger(__name__)
        
        if config_path is None:
            config_path = Path(__file__).parent.parent.parent / 'config' / 'settings.yml'
        
        self.config_path = config_path
        self.config_data = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file
        
        Returns:
            Configuration dictionary
        """
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r') as f:
                    config = yaml.safe_load(f)
                self.logger.info(f"Loaded configuration from {self.config_path}")
                return config or {}
            else:
                self.logger.warning(f"Configuration file not found: {self.config_path}")
                return self._get_default_config()
        except Exception as e:
            self.logger.error(f"Error loading configuration: {e}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration
        
        Returns:
            Default configuration dictionary
        """
        return {
            'performance': {
                'target_fps': 30,
                'max_cpu_percent': 80
            },
            'computer_vision': {
                'screenshot_method': 'mss',  # or 'pyautogui'
                'detection_confidence': 0.5,
                'detection_model': 'yolov8n'
            },
            'game_integration': {
                'gsi_port': 3000,
                'gsi_timeout': 1.0
            },
            'input_control': {
                'mouse_sensitivity': 1.0,
                'reaction_time_min': 0.1,
                'reaction_time_max': 0.3
            },
            'debug': {
                'log_level': 'INFO',
                'log_detections': False,
                'save_screenshots': False
            }
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value using dot notation
        
        Args:
            key: Configuration key (e.g., 'performance.target_fps')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.config_data
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """Set configuration value using dot notation
        
        Args:
            key: Configuration key (e.g., 'performance.target_fps')
            value: Value to set
        """
        keys = key.split('.')
        config = self.config_data
        
        for k in keys[:-1]:
            if k not in config or not isinstance(config[k], dict):
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def save(self):
        """Save current configuration to file"""
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, 'w') as f:
                yaml.dump(self.config_data, f, default_flow_style=False, indent=2)
            self.logger.info(f"Configuration saved to {self.config_path}")
        except Exception as e:
            self.logger.error(f"Error saving configuration: {e}")