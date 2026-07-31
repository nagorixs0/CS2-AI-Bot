#!/usr/bin/env python3
"""
CS2 AI Bot - Main Bot Class

This module contains the main CS2Bot class that orchestrates
all the different components of the AI bot.
"""

import time
import logging
from typing import Optional

from .config import Config
from computer_vision.screen_capture import ScreenCapture
from computer_vision.object_detector import ObjectDetector
from game_integration.gsi_client import GSIClient
from input_controller.mouse_controller import MouseController
from input_controller.keyboard_controller import KeyboardController


class CS2Bot:
    """Main CS2 AI Bot class"""
    
    def __init__(self, config: Config):
        """Initialize the CS2 Bot
        
        Args:
            config: Bot configuration object
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.running = False
        
        # Initialize components
        self._init_components()
        
    def _init_components(self):
        """Initialize all bot components"""
        self.logger.info("Initializing bot components...")
        
        # Computer Vision
        self.screen_capture = ScreenCapture(self.config)
        self.object_detector = ObjectDetector(self.config)
        
        # Game Integration
        self.gsi_client = GSIClient(self.config)
        
        # Input Controllers
        self.mouse = MouseController(self.config)
        self.keyboard = KeyboardController(self.config)
        
        self.logger.info("All components initialized successfully.")
    
    def start(self):
        """Start the main bot loop"""
        self.logger.info("Starting CS2 AI Bot main loop...")
        self.running = True
        
        try:
            self._main_loop()
        except Exception as e:
            self.logger.error(f"Error in main loop: {e}")
            raise
        finally:
            self.stop()
    
    def stop(self):
        """Stop the bot and cleanup"""
        self.logger.info("Stopping CS2 AI Bot...")
        self.running = False
        
        # Cleanup components
        if hasattr(self, 'gsi_client'):
            self.gsi_client.stop()
    
    def _main_loop(self):
        """Main bot decision loop"""
        loop_count = 0
        
        while self.running:
            loop_start = time.time()
            loop_count += 1
            
            try:
                # Capture screen
                screenshot = self.screen_capture.capture()
                if screenshot is None:
                    continue
                
                # Get game state from GSI
                game_state = self.gsi_client.get_current_state()
                
                # Detect objects in screenshot
                detections = self.object_detector.detect(screenshot)
                
                # Make decisions based on current state
                self._make_decisions(screenshot, game_state, detections)
                
                # Log performance every 100 loops
                if loop_count % 100 == 0:
                    loop_time = time.time() - loop_start
                    fps = 1.0 / loop_time if loop_time > 0 else 0
                    self.logger.debug(f"Loop {loop_count}: {loop_time:.3f}s ({fps:.1f} FPS)")
                
            except Exception as e:
                self.logger.error(f"Error in main loop iteration {loop_count}: {e}")
                time.sleep(0.1)  # Brief pause on error
            
            # Maintain target FPS
            target_fps = self.config.get('performance.target_fps', 30)
            target_time = 1.0 / target_fps
            elapsed = time.time() - loop_start
            
            if elapsed < target_time:
                time.sleep(target_time - elapsed)
    
    def _make_decisions(self, screenshot, game_state, detections):
        """Make AI decisions based on current game state
        
        Args:
            screenshot: Current game screenshot
            game_state: Current game state from GSI
            detections: Object detection results
        """
        # TODO: Implement decision making logic
        # This is where the main AI logic will go
        
        # Placeholder for now
        if self.config.get('debug.log_detections', False):
            if detections:
                self.logger.debug(f"Detected {len(detections)} objects")
        
        # Example: Basic enemy detection response
        # if 'enemy' in detections:
        #     self.mouse.aim_at(detections['enemy']['position'])
        #     self.mouse.click()
        
        pass