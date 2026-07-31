#!/usr/bin/env python3
"""
Screen Capture Module

This module handles capturing screenshots for analysis.
Focuses on educational computer vision techniques.
"""

import cv2
import numpy as np
import mss
import pyautogui
import logging
from typing import Optional, Tuple
from PIL import Image


class ScreenCapture:
    """Screen capture for computer vision analysis"""
    
    def __init__(self, config):
        """Initialize screen capture
        
        Args:
            config: Bot configuration object
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.method = config.get('computer_vision.screenshot_method', 'mss')
        
        # Initialize MSS if using that method
        if self.method == 'mss':
            self.sct = mss.mss()
        
        # Set up region of interest
        self.roi = self._setup_roi()
        
        self.logger.info(f"Screen capture initialized with method: {self.method}")
    
    def _setup_roi(self) -> dict:
        """Setup region of interest for capture
        
        Returns:
            ROI dictionary for capture
        """
        roi_config = self.config.get('computer_vision.roi')
        
        if roi_config:
            return {
                'left': roi_config.get('x', 0),
                'top': roi_config.get('y', 0),
                'width': roi_config.get('width', 1920),
                'height': roi_config.get('height', 1080)
            }
        
        # Default to full screen
        if self.method == 'mss':
            monitor = self.sct.monitors[1]  # Primary monitor
            return {
                'left': monitor['left'],
                'top': monitor['top'],
                'width': monitor['width'],
                'height': monitor['height']
            }
        
        return {'left': 0, 'top': 0, 'width': 1920, 'height': 1080}
    
    def capture(self) -> Optional[np.ndarray]:
        """Capture screenshot using configured method
        
        Returns:
            Screenshot as numpy array (BGR format) or None if failed
        """
        try:
            if self.method == 'mss':
                return self._capture_mss()
            elif self.method == 'pyautogui':
                return self._capture_pyautogui()
            else:
                self.logger.error(f"Unknown screenshot method: {self.method}")
                return None
        except Exception as e:
            self.logger.error(f"Error capturing screenshot: {e}")
            return None
    
    def _capture_mss(self) -> Optional[np.ndarray]:
        """Capture using MSS (fastest method)
        
        Returns:
            Screenshot as numpy array
        """
        screenshot = self.sct.grab(self.roi)
        
        # Convert to numpy array (BGRA -> BGR)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        
        return img
    
    def _capture_pyautogui(self) -> Optional[np.ndarray]:
        """Capture using PyAutoGUI (slower but more compatible)
        
        Returns:
            Screenshot as numpy array
        """
        screenshot = pyautogui.screenshot(
            region=(self.roi['left'], self.roi['top'], 
                   self.roi['width'], self.roi['height'])
        )
        
        # Convert PIL to numpy array (RGB -> BGR)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        return img
    
    def save_screenshot(self, image: np.ndarray, filename: str) -> bool:
        """Save screenshot for debugging or training data
        
        Args:
            image: Image to save
            filename: Output filename
            
        Returns:
            True if successful, False otherwise
        """
        try:
            cv2.imwrite(filename, image)
            return True
        except Exception as e:
            self.logger.error(f"Error saving screenshot: {e}")
            return False
    
    def preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """Preprocess image for analysis
        
        This is where you'd apply filters, normalization, etc.
        for computer vision processing.
        
        Args:
            image: Raw screenshot
            
        Returns:
            Preprocessed image
        """
        # Example preprocessing steps:
        
        # 1. Apply scaling if configured
        scale = self.config.get('computer_vision.image_scale', 1.0)
        if scale != 1.0:
            new_width = int(image.shape[1] * scale)
            new_height = int(image.shape[0] * scale)
            image = cv2.resize(image, (new_width, new_height))
        
        # 2. Optional: Convert to different color space
        # hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # 3. Optional: Apply noise reduction
        # image = cv2.bilateralFilter(image, 9, 75, 75)
        
        # 4. Optional: Enhance contrast
        # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        # image = clahe.apply(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
        
        return image
    
    def get_capture_stats(self) -> dict:
        """Get capture performance statistics
        
        Returns:
            Dictionary with capture stats
        """
        return {
            'method': self.method,
            'roi': self.roi,
            'total_captures': getattr(self, '_capture_count', 0)
        }