#!/usr/bin/env python3
"""
Object Detection Module

Educational computer vision for detecting game elements.
Focuses on learning CV techniques, not creating cheats.
"""

import cv2
import numpy as np
import logging
from typing import Dict, List, Tuple, Optional


class ObjectDetector:
    """Educational object detection for CS2 analysis"""
    
    def __init__(self, config):
        """Initialize object detector
        
        Args:
            config: Bot configuration object
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.confidence_threshold = config.get('computer_vision.detection_confidence', 0.5)
        
        # Initialize detection methods
        self._init_detectors()
        
        self.logger.info("Object detector initialized for educational analysis")
    
    def _init_detectors(self):
        """Initialize various detection methods for learning"""
        # Template matching templates (for learning purposes)
        self.templates = {}
        
        # Color-based detection ranges
        self.color_ranges = {
            'enemy_red': {
                'lower': np.array([0, 100, 100]),   # Lower HSV bound for red
                'upper': np.array([10, 255, 255])   # Upper HSV bound for red
            },
            'team_blue': {
                'lower': np.array([100, 100, 100]), # Lower HSV bound for blue
                'upper': np.array([130, 255, 255])  # Upper HSV bound for blue
            }
        }
        
        # Edge detection parameters
        self.edge_params = {
            'canny_lower': 50,
            'canny_upper': 150
        }
    
    def detect(self, image: np.ndarray) -> Dict:
        """Main detection function - educational analysis only
        
        Args:
            image: Screenshot to analyze
            
        Returns:
            Dictionary with detection results for learning
        """
        detections = {
            'timestamp': cv2.getTickCount(),
            'image_shape': image.shape,
            'analysis': {}
        }
        
        try:
            # Educational computer vision techniques:
            
            # 1. Color-based analysis (learning color spaces)
            detections['analysis']['colors'] = self._analyze_colors(image)
            
            # 2. Edge detection (learning feature extraction)
            detections['analysis']['edges'] = self._detect_edges(image)
            
            # 3. Template matching (learning pattern recognition)
            detections['analysis']['templates'] = self._template_matching(image)
            
            # 4. Contour analysis (learning shape detection)
            detections['analysis']['shapes'] = self._analyze_shapes(image)
            
            # 5. Statistical analysis of the image
            detections['analysis']['statistics'] = self._image_statistics(image)
            
        except Exception as e:
            self.logger.error(f"Error in detection analysis: {e}")
            detections['error'] = str(e)
        
        return detections
    
    def _analyze_colors(self, image: np.ndarray) -> Dict:
        """Analyze color distribution - educational purpose
        
        Args:
            image: Input image
            
        Returns:
            Color analysis results
        """
        # Convert to HSV for better color analysis
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        color_analysis = {}
        
        for color_name, color_range in self.color_ranges.items():
            # Create mask for this color range
            mask = cv2.inRange(hsv, color_range['lower'], color_range['upper'])
            
            # Calculate percentage of image with this color
            pixel_count = cv2.countNonZero(mask)
            total_pixels = image.shape[0] * image.shape[1]
            percentage = (pixel_count / total_pixels) * 100
            
            color_analysis[color_name] = {
                'pixel_count': pixel_count,
                'percentage': percentage,
                'detected': percentage > 0.1  # Threshold for "detected"
            }
        
        return color_analysis
    
    def _detect_edges(self, image: np.ndarray) -> Dict:
        """Edge detection for learning feature extraction
        
        Args:
            image: Input image
            
        Returns:
            Edge detection results
        """
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Canny edge detection
        edges = cv2.Canny(blurred, 
                          self.edge_params['canny_lower'], 
                          self.edge_params['canny_upper'])
        
        # Analyze edge density
        edge_pixels = cv2.countNonZero(edges)
        total_pixels = edges.shape[0] * edges.shape[1]
        edge_density = (edge_pixels / total_pixels) * 100
        
        return {
            'edge_density_percent': edge_density,
            'edge_pixel_count': edge_pixels,
            'has_strong_edges': edge_density > 5.0
        }
    
    def _template_matching(self, image: np.ndarray) -> Dict:
        """Template matching for pattern recognition learning
        
        Args:
            image: Input image
            
        Returns:
            Template matching results
        """
        # This would be where you load and match templates
        # For now, return placeholder for educational structure
        
        return {
            'templates_loaded': len(self.templates),
            'matches_found': 0,
            'confidence_threshold': self.confidence_threshold
        }
    
    def _analyze_shapes(self, image: np.ndarray) -> Dict:
        """Contour and shape analysis for learning
        
        Args:
            image: Input image
            
        Returns:
            Shape analysis results
        """
        # Convert to grayscale and apply threshold
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Analyze contours
        shape_analysis = {
            'total_contours': len(contours),
            'large_contours': 0,
            'circular_shapes': 0,
            'rectangular_shapes': 0
        }
        
        for contour in contours:
            area = cv2.contourArea(contour)
            
            if area > 100:  # Only analyze larger shapes
                shape_analysis['large_contours'] += 1
                
                # Approximate contour to polygon
                epsilon = 0.02 * cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)
                
                # Classify basic shapes
                if len(approx) > 6:
                    shape_analysis['circular_shapes'] += 1
                elif len(approx) == 4:
                    shape_analysis['rectangular_shapes'] += 1
        
        return shape_analysis
    
    def _image_statistics(self, image: np.ndarray) -> Dict:
        """Calculate basic image statistics for analysis
        
        Args:
            image: Input image
            
        Returns:
            Image statistics
        """
        # Convert to grayscale for statistics
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        return {
            'mean_brightness': float(np.mean(gray)),
            'std_brightness': float(np.std(gray)),
            'min_brightness': int(np.min(gray)),
            'max_brightness': int(np.max(gray)),
            'contrast_ratio': float(np.std(gray) / np.mean(gray)) if np.mean(gray) > 0 else 0
        }
    
    def visualize_detections(self, image: np.ndarray, detections: Dict) -> np.ndarray:
        """Create visualization overlay for educational purposes
        
        Args:
            image: Original image
            detections: Detection results
            
        Returns:
            Image with visualization overlay
        """
        overlay = image.copy()
        
        # Add text overlay with detection info
        y_offset = 30
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # Display basic statistics
        if 'analysis' in detections and 'statistics' in detections['analysis']:
            stats = detections['analysis']['statistics']
            text = f"Brightness: {stats['mean_brightness']:.1f}"
            cv2.putText(overlay, text, (10, y_offset), font, 0.6, (0, 255, 0), 2)
            y_offset += 25
            
            text = f"Contrast: {stats['contrast_ratio']:.2f}"
            cv2.putText(overlay, text, (10, y_offset), font, 0.6, (0, 255, 0), 2)
            y_offset += 25
        
        # Display edge information
        if 'analysis' in detections and 'edges' in detections['analysis']:
            edges = detections['analysis']['edges']
            text = f"Edge Density: {edges['edge_density_percent']:.1f}%"
            cv2.putText(overlay, text, (10, y_offset), font, 0.6, (0, 255, 255), 2)
        
        return overlay