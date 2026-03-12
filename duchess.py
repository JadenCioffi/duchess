"""
Duchess -- A chess project

Activate Environment -> source .venv/bin/activate

"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Duchess"

SQUARE_FILES = ["A", "B", "C", "D", "E", "F", "G", "H"]
SQUARE_RANKS = [1, 2, 3, 4, 5, 6, 7, 8]

# index 0: dark color, index 1: light color
SQUARE_COLORS = [arcade.color.AMAZON, arcade.color.LIGHT_GREEN]

PIECE_SCALING = 0.25

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background_color = arcade.color.WHEAT

        self.piece_list = None

        self.w_pawn = None
        

    def setup(self):
        self.piece_list = arcade.SpriteList()

        self.w_pawn = arcade.Sprite("pieces/w-pawn.png", PIECE_SCALING)
        self.w_pawn.center_x = 50
        self.w_pawn.center_y = 50
        self.piece_list.append(self.w_pawn)

    def on_draw(self):
        self.clear()

        # Draw the board
        flip = 0
        for x in range(8):
            for y in range(8):
                arcade.draw_lbwh_rectangle_filled(x*100, y*100, 100, 100, SQUARE_COLORS[flip])
                arcade.draw_text(f"{SQUARE_FILES[x]}, {SQUARE_RANKS[y]}", x*100, y*100 + 5, arcade.color.BLACK, 12, bold=True)
                if flip == 0: flip = 1
                else: flip = 0
            if flip == 1: flip = 0
            else: flip = 1

        # Draw the pieces

        self.piece_list.draw()
                    

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

class Square(arcade.Window):
    def __init__(self, file, rank, scale=1):
        # Identified by unique file (column a-h) and rank (row 1-8)
        self.file = file
        self.rank = rank

class Piece(arcade.Window):
    pass


        

def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()