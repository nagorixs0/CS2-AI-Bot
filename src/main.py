#!/usr/bin/env python3
"""
CS2 AI Bot - Main Entry Point

This is the main entry point for the CS2 AI Bot.
It initializes all components and starts the main game loop.
"""

import sys
import time
import logging
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent))

from core.bot import CS2Bot
from core.config import Config
from core.logger import setup_logger


def main():
    """Main function to start the CS2 AI Bot"""
    # Setup logging
    logger = setup_logger()
    logger.info("Starting CS2 AI Bot...")
    
    try:
        # Load configuration
        config = Config()
        
        # Initialize bot
        bot = CS2Bot(config)
        
        # Start bot
        logger.info("Bot initialized successfully. Starting main loop...")
        bot.start()
        
    except KeyboardInterrupt:
        logger.info("Bot stopped by user (Ctrl+C)")
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        sys.exit(1)
    finally:
        logger.info("CS2 AI Bot shutdown complete.")


if __name__ == "__main__":
    main()