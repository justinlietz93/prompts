#!/usr/bin/env python3
"""
Prometheus AI Metadata Dialog

Dialog for viewing and editing prompt metadata.
"""

import os
import json
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLabel, 
                           QLineEdit, QTextEdit, QDialogButtonBox, QMessageBox)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from constants import DEFAULT_FONT_FAMILY, DEFAULT_FONT_SIZE

class MetadataDialog(QDialog):
    """Dialog to display and edit prompt metadata"""
    
    def __init__(self, prompt_type, prompt_library, parent=None):
        """Initialize the metadata dialog.
        
        Args:
            prompt_type (str): The type of prompt to edit
            prompt_library (PromptLibrary): Reference to the prompt library
            parent (QWidget, optional): Parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.prompt_type = prompt_type
        self.prompt_library = prompt_library
        self.prompt_data = prompt_library.get(prompt_type, {})
        
        self.setWindowTitle(f"Prompt Details: {prompt_type.replace('_', ' ').title()}")
        self.setMinimumWidth(500)  # Slightly wider for better readability
        
        # Main layout
        layout = QVBoxLayout(self)
        
        # Form layout for metadata
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        
        # Description
        self.description_edit = QTextEdit()
        self.description_edit.setPlaceholderText("Enter a description for this prompt")
        self.description_edit.setFont(QFont(DEFAULT_FONT_FAMILY, DEFAULT_FONT_SIZE))
        self.description_edit.setMinimumHeight(100)
        description = self.prompt_data.get("description", "")
        self.description_edit.setText(description)
        form_layout.addRow("Description:", self.description_edit)
        
        # Tags
        self.tags_edit = QLineEdit()
        self.tags_edit.setPlaceholderText("Enter tags separated by commas")
        self.tags_edit.setFont(QFont(DEFAULT_FONT_FAMILY, DEFAULT_FONT_SIZE))
        metadata = self.prompt_data.get("metadata", {})
        tags = metadata.get("tags", [])
        self.tags_edit.setText(", ".join(tags))
        form_layout.addRow("Tags:", self.tags_edit)
        
        # Author
        self.author_edit = QLineEdit()
        self.author_edit.setFont(QFont(DEFAULT_FONT_FAMILY, DEFAULT_FONT_SIZE))
        self.author_edit.setText(metadata.get("author", ""))
        form_layout.addRow("Author:", self.author_edit)
        
        # Version
        self.version_edit = QLineEdit()
        self.version_edit.setFont(QFont(DEFAULT_FONT_FAMILY, DEFAULT_FONT_SIZE))
        self.version_edit.setText(metadata.get("version", "1.0.0"))
        form_layout.addRow("Version:", self.version_edit)
        
        # Created date
        self.created_edit = QLineEdit()
        self.created_edit.setFont(QFont(DEFAULT_FONT_FAMILY, DEFAULT_FONT_SIZE))
        self.created_edit.setText(metadata.get("created", "2025-03-09"))
        form_layout.addRow("Date Added:", self.created_edit)
        
        # Updated date
        self.updated_edit = QLineEdit()
        self.updated_edit.setFont(QFont(DEFAULT_FONT_FAMILY, DEFAULT_FONT_SIZE))
        self.updated_edit.setText(metadata.get("updated", "2025-03-09"))
        form_layout.addRow("Last Updated:", self.updated_edit)
        
        # Add form to main layout
        layout.addLayout(form_layout)
        
        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
    def accept(self):
        """Save the metadata changes"""
        # Update the description
        self.prompt_data["description"] = self.description_edit.toPlainText()
        
        # Create or update metadata
        if "metadata" not in self.prompt_data:
            self.prompt_data["metadata"] = {}
        
        # Update metadata fields
        tags = [tag.strip() for tag in self.tags_edit.text().split(",") if tag.strip()]
        self.prompt_data["metadata"]["tags"] = tags
        self.prompt_data["metadata"]["author"] = self.author_edit.text()
        self.prompt_data["metadata"]["version"] = self.version_edit.text()
        self.prompt_data["metadata"]["created"] = self.created_edit.text()
        self.prompt_data["metadata"]["updated"] = self.updated_edit.text()
        
        # Save the changes back to the library
        self.prompt_library.save_prompt(self.prompt_type, self.prompt_data)
            
        super().accept() 