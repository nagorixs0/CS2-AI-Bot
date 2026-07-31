#!/usr/bin/env python3
"""
CS2 AI Bot - Logging Configuration

This module sets up logging for the CS2 AI Bot.
"""

import logging
import sys
from pathlib import Path
from datetime import datetime


def setup_logger(log_level: str = "INFO", log_file: bool = True) -> logging.Logger:
    """Setup logging configuration
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_file: Whether to log to file
        
    Returns:
        Configured logger
    """
    # Create logs directory
    log_dir = Path(__file__).parent.parent.parent / 'logs'
    log_dir.mkdir(exist_ok=True)
    
    # Configure logging
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Setup root logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # Clear existing handlers
    logger.handlers.clear()
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, log_level.upper()))
    console_formatter = logging.Formatter(log_format)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # File handler
    if log_file:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file_path = log_dir / f'cs2_bot_{timestamp}.log'
        
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)  # Always log everything to file
        file_formatter = logging.Formatter(log_format)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        
        logger.info(f"Logging to file: {log_file_path}")
    
    return logger