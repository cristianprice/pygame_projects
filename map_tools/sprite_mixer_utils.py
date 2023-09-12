
from pathlib import Path

import pygame
from pygame_gui.windows.ui_file_dialog import UIFileDialog


def create_open_file_dialog(manager) -> UIFileDialog:
    file_dialog = UIFileDialog(pygame.Rect(
        160, 50, 440, 500), manager=manager, allow_picking_directories=True)

    return file_dialog
