"""
Utility functions for the Prometheus AI Prompt Generator.

This module contains utility functions used throughout the application.
"""

import os
import sys
import random
from PyQt6.QtGui import QColor, QPalette

def random_color():
    """Generate a random, visually pleasing color.
    
    Returns:
        QColor: A randomly generated color.
    """
    # Generate pleasing colors (avoid too dark or too light)
    hue = random.randint(0, 359)
    saturation = random.randint(50, 80)
    value = random.randint(70, 90)
    
    return QColor.fromHsv(hue, saturation, value)

def format_display_name(prompt_type):
    """Format a prompt type for display (e.g., snake_case to Title Case).
    
    Args:
        prompt_type (str): The raw prompt type string.
        
    Returns:
        str: Formatted display name.
    """
    return prompt_type.replace("_", " ").title()

def ensure_directory_exists(directory_path):
    """Ensure that a directory exists, create it if it doesn't.
    
    Args:
        directory_path (str): Path to the directory.
    """
    os.makedirs(directory_path, exist_ok=True)

def get_application_path():
    """Get the path to the application directory.
    
    Returns:
        str: The absolute path to the application directory.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def is_dark_theme(theme_name):
    """Check if a theme is a dark theme.
    
    Args:
        theme_name (str): Name of the theme.
        
    Returns:
        bool: True if it's a dark theme, False otherwise.
    """
    return theme_name.startswith("Dark")

def get_theme_color(theme_name):
    """Get the primary color for a theme based on its name.
    
    Args:
        theme_name (str): Name of the theme.
        
    Returns:
        QColor: The primary color for the theme.
    """
    # For demonstration, we'll use a fixed set of colors based on theme
    if theme_name == "Dark Blue" or theme_name == "Light Blue":
        return QColor("#2980b9")
    elif theme_name == "Dark Teal" or theme_name == "Light Teal":
        return QColor("#009688")
    elif theme_name == "Dark Amber" or theme_name == "Light Amber":
        return QColor("#ffc107")
    elif theme_name == "Dark Purple" or theme_name == "Light Purple":
        return QColor("#9c27b0")
    elif theme_name == "Dark Pink" or theme_name == "Light Pink":
        return QColor("#e91e63")
    elif theme_name == "Dark Red" or theme_name == "Light Red":
        return QColor("#f44336")
    elif theme_name == "Dark Yellow" or theme_name == "Light Yellow":
        return QColor("#ffeb3b")
    else:
        # Default to blue
        return QColor("#2980b9")

def set_palette_color(palette, role, color):
    """Set a color for a specific palette role.
    
    Args:
        palette (QPalette): The palette to modify
        role (QPalette.ColorRole): The color role to change
        color (QColor): The color to set
    """
    palette.setColor(role, color)

def generate_template_with_urgency(template, urgency_level):
    """Generate a prompt template with the specified urgency level applied.
    
    Args:
        template (str): The original prompt template.
        urgency_level (int): Urgency level from 1 to 10.
        
    Returns:
        str: The template with urgency applied.
    """
    # Define urgency modifiers based on urgency level (1-10 scale)
    urgency_modifiers = {
        1: {
            "intro": "Whenever you have free time, please consider",
            "deadline": "There is absolutely no rush at all.",
            "priority": "This is a very low priority task.",
            "tone": "The tone should be extremely casual and relaxed."
        },
        2: {
            "intro": "When you have time, please",
            "deadline": "There is no rush.",
            "priority": "This is a low priority task.",
            "tone": "The tone should be casual and relaxed."
        },
        3: {
            "intro": "I would appreciate if you could",
            "deadline": "This can be completed at your convenience.",
            "priority": "This is a below average priority task.",
            "tone": "The tone should be friendly and unhurried."
        },
        4: {
            "intro": "Please",
            "deadline": "This should be completed within a reasonable timeframe.",
            "priority": "This is a standard priority task.",
            "tone": "The tone should be professional but not urgent."
        },
        5: {
            "intro": "I would like you to",
            "deadline": "This should be completed in a timely manner.",
            "priority": "This is a moderately important task.",
            "tone": "The tone should be clear and straightforward."
        },
        6: {
            "intro": "I need you to",
            "deadline": "This should be completed soon.",
            "priority": "This is an important task.",
            "tone": "The tone should be direct and focused."
        },
        7: {
            "intro": "I strongly need you to",
            "deadline": "This should be completed promptly.",
            "priority": "This is a high priority task.",
            "tone": "The tone should convey notable importance."
        },
        8: {
            "intro": "I urgently need you to",
            "deadline": "This needs to be completed quickly.",
            "priority": "This is a very high priority task.",
            "tone": "The tone should convey significant importance and urgency."
        },
        9: {
            "intro": "URGENT: I require you to",
            "deadline": "This requires immediate attention.",
            "priority": "This is a critical priority task.",
            "tone": "The tone should convey strong urgency and importance."
        },
        10: {
            "intro": "CRITICAL URGENT ACTION REQUIRED:",
            "deadline": "This demands immediate action.",
            "priority": "This is the highest possible priority task.",
            "tone": "The tone should convey maximum urgency and critical importance."
        }
    }
    
    # Get modifiers for the specified urgency level (default to medium if out of range)
    modifiers = urgency_modifiers.get(urgency_level, urgency_modifiers[5])
    
    # Process any placeholders in the template (like {topic}, {language}, etc.)
    # For now, we'll keep the placeholders as they are since we don't have values for them
    processed_template = template
    
    # Add urgency to the template
    urgency_prefix = f"{modifiers['intro']} {processed_template.lstrip()}\n\n"
    urgency_suffix = f"\n\n{modifiers['deadline']} {modifiers['priority']} {modifiers['tone']}"
    
    return urgency_prefix + urgency_suffix 