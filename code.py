#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: May 5 , 2025

# pyright: reportMissingImports=false
import ugame
import stage

import constants


def game_scene():

    # image banks from the PyBadge files directory
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background to span across the whole screen
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # grabs image out of spritesheet bank and assigns it to ship variable
    ship = stage.Sprite(image_bank_sprite, 5, 75, 96)

    # sets refresh rate to 60 times a second
    game = stage.Stage(ugame.display, constants.FPS)

    # adds background to list
    game.layers = [ship] + [background]
    game.render_block()

    # repeats forever, loops game
    while True:
        # get the user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= 160:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(0 - 16, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x > 0 - 16:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(160, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # update the game logic

        # redraw sprites (not whole background)
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
