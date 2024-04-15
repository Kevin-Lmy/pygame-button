# Python Button Class with Pygame

A Python class for creating and customizing buttons using the Pygame library. The `Button` class allows you to easily create interactive buttons with customizable properties such as text, colors, fonts, and more.

---

## Table of Contents

* [Features](#features)
* [Getting Started](#getting-started)
* [Documentation](#documentaion)
* [Contributing](#contributing)
* [Licensa](#license)

---

## Features

* Create and customize buttons for Pygame applications.
* Easily set button text, colors, and fonts.
* Support for click and hover actions.
* Flexible button positioning and padding.
* Simple and intuitive class for button management.

---

## Getting Started

To use the `Button` class in your Pygame project, follow these steps:

1. Ensure Python is installed on your system.

1. Clone this repository or download the `button.py` file.

1. Include the `button.py` file in your Pygame project directory.

1. Install Pygame in the console:

   ```
   pip install pygame
   ```

1. Import the `Button` class in your Python script:

   ```
   from button import Button
   ```

---

## Documentaion

|Attribute|Description|Type|
|-|-|-|
|`x_pos`|The x-coordinate of the button's top-left corner|Integer|
|`y_pos`|The y-coordinate of the button's top-left corner|Integer|
|`pad_x`|Padding for the button's width|Integer|
|`pad_y`|Padding for the button's height|Integer|
|`text`|The text displayed on the button|String|
|`color`|The color of the button|Pygame Color Object|
|`hover_color`|The color of the button when hovered|Pygame Color Object|
|`text_color`|The color of the button's text|Pygame Color Object|
|`font`|The font used for the button's text| Pygame Font Object|
|`is_hovered`|A flag indicating if the button is being hovered over|Boolean|
|`rect`|A Pygame Rect object representing the button's dimensions and position|Pygame Rect Object|
|`width`|The width of the button (derived from text size and padding)|Integer|
|`height`|The height of the button (derived from text size and padding)|Integer|

## `__init__(self, x_pos, y_pos, text)`
#### Description
Initialize a Button instance.
#### Parameters
* `x_pos` (int): The x-coordinate of the button's top-left corner.
* `y_pos` (int): The y-coordinate of the button's top-left corner.
* `text` (str): The text displayed on the button.

## `draw(self, window)`
#### Description
Draw the button on the Pygame window.
#### Parameters
* `window` (Pygame Surface): The Pygame window on which the button will be drawn.

## `update_dimensions(self)`
#### Description
Update the dimensions of the button based on the text and font size.

## `set_padding(self, pad_x, pad_y)`
#### Description
Set the padding for the button's width and height and update the dimensions.
#### Parameters
* `pad_x` (int): The padding for the button's width.
* `pad_y` (int): The padding for the button's height.

## `set_pos(self, x_pos, y_pos)`
#### Description
Set the position of the button and update the rect.
#### Parameters
* `x_pos` (int): The new x-coordinate for the button's top-left corner.
* `y_pos` (int): The new y-coordinate for the button's top-left corner.

## `set_text(self, text)`
#### Description
Set the text of the button and update the dimensions and rect.
#### Parameters
* `text` (str): The new text to be displayed on the button.

## `set_color(self, color)`
#### Description
Set the color of the button.
#### Parameters
* `color` (str): The new color for the button.

## `set_hover_color(self, hover_color)`
#### Description
Set the color of the button when hovered.
#### Parameters
* `hover_color` (str): The color when the button is hovered.

## `set_text_color(self, text_color)`
#### Description
Set the color of the button's text.
#### Parameters
* `text_color` (str): The new text color.

## `set_font(self, font_name, font_size)`
#### Description
Set the font and font size for the button's text and update dimensions and rect.
#### Parameters
* `font_name` (str): The name of the font.
* `font_size` (int): The size of the font.

## `on_click(self, x, y, action=None)`
#### Description
Trigger an action when the button is clicked.
#### Parameters
* `x` (int): The x-coordinate of the mouse click.
* `y` (int): The y-coordinate of the mouse click.
* `action` (function): The action to be executed when the button is clicked.

## `on_hover(self, x, y, action=None)`
#### Description
Trigger an action when the mouse hovers over the button.
#### Parameters
* `x` (int): The x-coordinate of the mouse pointer.
* `y` (int): The y-coordinate of the mouse pointer.
* `action` (function): The action to be executed when the mouse hovers over the button.


---

## Example

```
import pygame
from button import Button

# Initialize Pygame
pygame.init()

# Create a Pygame window
window = pygame.display.set_mode((800, 600))

# Create a button
my_button = Button(100, 100, "Click Me")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if my_button.rect.collidepoint(event.pos):
                print("Button clicked!")

    # Draw the button
    my_button.draw(window)

    pygame.display.update()

# Quit Pygame
pygame.quit()
```
![Example button](example_button.png)

---

## Contributing

Bug reports and pull requests are welcomed.

---

## License

This repository is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).