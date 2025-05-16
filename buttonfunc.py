# Button Class

class Button():
    # Constructor
    def __init__(self, image, pos, textinput, font, colour, hovcolour):

# Attributes

        self.image = image # Button image
        # Creates list for positions (x, y)
        self.x_pos = pos[0] # x axis position
        self.y_pos = pos[1] # y axis position
        self.font = font # Text font
        self.colour, self.hovcolour = colour, hovcolour # Default colour / Hover colour
        # Find the difference between these
        self.textinput = textinput # Text in button
        self.text = self.font.render(self.textinput, True, self.colour) # Text displayed on button
        # ^ ^ ^ ^ ^
        if self.image is None: # (Only if no image is inserted)
            self.image = self.text # Allows text to replace an image
        # Rectangles ...
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

# Methods

    # (If there is an image inserted)
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    # Checks for input from button
    def checkforinput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    # Changes colour on mouse hover
    def changecolour(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.textinput, True, self.hovcolour)
        else:
            self.text = self.font.render(self.textinput, True, self.colour)