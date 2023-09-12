import pygame
import pygame_gui

# --- constants ---

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)

# --- classes ---

# ... empty ...

# --- functions ---


def open_file_dialog():
    global file_dialog

    # center dialog
    rect = pygame.Rect((0, 0), (200, 50))
    rect.center = screen.get_rect().center

    # create dialog
    file_dialog = pygame_gui.windows.ui_file_dialog.UIFileDialog(
        rect=rect, manager=manager, allow_picking_directories=True)

# --- main ---

# - init -


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# - objects -

# center button
rect = pygame.Rect((0, 0), (200, 50))
rect.center = screen.get_rect().center

# create button
button_directory = pygame_gui.elements.UIButton(
    relative_rect=rect, text='Select Directory', manager=manager)

# - mainloop -

clock = pygame.time.Clock()
is_running = True

while is_running:

    time_delta = clock.tick(30)/1000.0

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:

            # handle button's events
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_directory:
                    open_file_dialog()

            # handle dialog's events
            if event.user_type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
                if event.ui_element == file_dialog:
                    print('Selected:', event.text)

        manager.process_events(event)

    # - updates -

    manager.update(time_delta)

    # - draws -

    screen.fill(BLACK)

    manager.draw_ui(screen)

    pygame.display.update()
