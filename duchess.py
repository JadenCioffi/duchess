"""
Duchess -- A chess project
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Duchess"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background_color = arcade.color.WHEAT

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()