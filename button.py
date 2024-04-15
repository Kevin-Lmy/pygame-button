import pygame

class Button:
    def __init__(self, x_pos, y_pos, text):
        # Initialize the Button with the provided position and text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.pad_x = 20  # Default padding for the button width
        self.pad_y = 10  # Default padding for the button height
        self.text = text
        self.color = "#2E3E4D"  # Default button color
        self.hover_color = "#005ABB"  # Default button color when hovering
        self.text_color = "#CCCCCC"  # Default text color
        self.font = pygame.font.Font(None, 36)  # Default font and font size
        self.is_hovered = False  # Flag to track if the button is being hovered over

        self.update_dimensions()  # Update the button dimensions
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width+self.pad_x, self.height+self.pad_y)

    def draw(self, window):
        # Draw the button on the provided window
        if self.is_hovered:
            pygame.draw.rect(window, self.hover_color, self.rect)
        else:
            pygame.draw.rect(window, self.color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        window.blit(text_surface, text_rect)
    
    def update_dimensions(self):
         # Update the dimensions of the button based on the text and font size
        text_surface = self.font.render(self.text, True, self.text_color)
        self.width, self.height = text_surface.get_size()

    def set_padding(self, pad_x, pad_y):
        # Set the padding for the button width and height and update the dimensions# Set the padding for the button width and height and update the dimensions
        self.pad_x, self.pad_y = pad_x, pad_y
        self.update_dimensions()
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width+self.pad_x, self.height+self.pad_y)

    def set_pos(self, x_pos, y_pos):
        # Set the position of the button and update the rect
        self.x_pos, self.y_pos = x_pos, y_pos
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width+self.pad_x, self.height+self.pad_y)

    def set_text(self, text):
        # Set the text of the button and update the dimensions and rect
        self.text = text
        self.update_dimensions()
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width+self.pad_x, self.height+self.pad_y)

    def set_color(self, colour):
        # Set the button color
        self.color = colour

    def set_hover_color(self, hover_color):
        # Set the button color when hovering
        self.hover_color = hover_color

    def set_text_color(self, text_color):
        # Set the text color
        self.text_color = text_color
    
    def set_font(self, font_name, font_size):
        # Set the font and font size for the button text and update dimensions and rect
        self.font = pygame.font.Font(font_name, font_size)
        self.update_dimensions()
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width+self.pad_x, self.height+self.pad_y)

    def on_click(self, x, y, action=None):
        # Trigger an action when the button is clicked
        if action is not None:
            if self.rect.collidepoint(x, y):
                action()
        else:
            lambda: None  # Default action if no action is provided

    def on_hover(self, x, y, action=None):
        # Trigger an action when the mouse hovers over the button
        if action is not None:
            if self.rect.collidepoint(x, y):
                self.is_hovered = True
                if action is not None:
                    action()
            else:
                self.is_hovered = False
        else:
            lambda: None  # Default action if no action is provided