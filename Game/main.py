import pygame
from game import moonglow

# Define constants for the game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Define colors using RGB values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

class menu:
    def __init__(self):  
        # Initialize Pygame
        pygame.init()

        # Create the game window and clock
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        # Set the font for the menu text
        font = pygame.font.Font(None, 64)

        # Define the menu options
        menu_items = ["PLAY", "SETTINGS", "QUIT"]
        menu_rects = []

        # Loop through the menu options and create Rect objects for each one
        for i, item in enumerate(menu_items):
            text = font.render(item, True, WHITE)
            rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + i*80))
            menu_rects.append(rect)

        # Define a variable to keep track of which menu option is selected
        selected_item = 0

        # Set up the game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        selected_item = (selected_item - 1) % len(menu_items)
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        selected_item = (selected_item + 1) % len(menu_items)
                    elif event.key == pygame.K_RETURN:
                        if selected_item == 0:
                            print("Play!")
                            
                            moonglow.run()
                        elif selected_item == 1:
                            print("Settings!")
                            menu.settings()
                        elif selected_item == 2:
                            running = False
                            

        # Draw the menu options
        for i, rect in enumerate(menu_rects):
            if i == selected_item:
                pygame.draw.rect(screen, WHITE, rect, 4)
            screen.blit(font.render(menu_items[i], True, WHITE), rect)

        # Update the display
        pygame.display.update()

        # Limit the frame rate
        clock.tick(FPS)

    def settings(self):
        
        # Create the game window and clock
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Set the font for the menu text
        font = pygame.font.Font(None, 32)

        # Define the volume and screen size scrollbars
        volume_rect = pygame.Rect(50, 50, 200, 20)
        screen_size_rect = pygame.Rect(50, 100, 200, 20)

        # Define a variable to keep track of the volume and screen size
        volume = 50
        screen_size = (800, 600)


        # Clear the screen
        screen.fill(BLACK)

        # Draw the volume scrollbar
        pygame.draw.rect(screen, GRAY, volume_rect)
        pygame.draw.rect(screen, WHITE, pygame.Rect(volume_rect.left + volume_rect.width * volume / 100 - 5, volume_rect.top, 10, volume_rect.height))

        # Draw the screen size scrollbar
        pygame.draw.rect(screen, GRAY, screen_size_rect)
        pygame.draw.rect(screen, WHITE, pygame.Rect(screen_size_rect.left + (screen_size[0] - 400) / 1200 * screen_size_rect.width - 5, screen_size_rect.top + (screen_size[1] - 200) / 800 * screen_size_rect.height, 10, 20))

        # Draw the volume and screen size labels
        screen.blit(font.render("Volume: {}%".format(volume), True, WHITE), (50, 25))
        screen.blit(font.render("Screen Size: {} x {}".format(screen_size[0], screen_size[1]), True, WHITE), (50, 75))

        # Update the display
        pygame.display.update()


if __name__ == "__main__":
    menu = menu()
    