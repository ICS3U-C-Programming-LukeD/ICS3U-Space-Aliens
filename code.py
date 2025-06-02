#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: May 5 , 2025

import ugame
import stage


def game_scene():

    # image banks from the PyBadge files directory
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background to span across the whole screen
    background = stage.Grid(image_bank_background, 10, 8)

    # grabs image out of spritesheet bank and assigns it to ship variable
    ship = stage.Sprite(image_bank_sprite, 5, 75, 66)

    # sets refresh rate to 60 times a second
    game = stage.Stage(ugame.display, 60)

    # adds background to list
    game.layers = [ship] + [background]
    game.render_block()

    # repeats forever, loops game
    while True:
        # get the user input

        # update the game logic

        # redraw sprites (not whole background)
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
