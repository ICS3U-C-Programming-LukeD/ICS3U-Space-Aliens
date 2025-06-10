#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: May 5 , 2025

# pyright: reportMissingImports=false
import ugame
import stage
import time
import random

import constants


def game_scene():
    # this function is for the main game

    # image banks from the PyBadge files directory
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # gets sounds ready
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # sets the background to span across the whole screen
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(2, 3)
            background.tile(x_location, y_location, tile_picked)

    # grabs image out of spritesheet bank and assigns it to ship variable
    ship = stage.Sprite(image_bank_sprite, 5, 75, 96)

    alien = stage.Sprite(
        image_bank_sprite,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # creates a list of lasers for shooting
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(
            image_bank_sprite, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        lasers.append(a_single_laser)

    # sets refresh rate to 60 times a second
    game = stage.Stage(ugame.display, constants.FPS)

    # adds background to list
    game.layers = lasers + [ship] + [alien] + [background]
    game.render_block()

    # repeats forever, loops game
    while True:
        # get the user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= 160:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(0 - 16, ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x > 0 - 16:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(160, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN:
            pass
        # update the game logic
        # plays a sound if A button was just pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # fire a laser if lasers have not all been used update
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
        # redraw sprites (not whole background)

        game.render_sprites(lasers + [ship] + [alien])
        game.tick()


def tutorial_scene():
    # this function is for the menu screen

    # image banks from the PyBadge files directory
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # add text objects
    text = []
    text1 = stage.Text(
        width=15, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 30)
    text1.text("MOVE = UP,DOWN,    LEFT, RIGHT\n\nSHOOT = A")
    text.append(text1)

    text2 = stage.Text(
        width=14, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(20, 100)
    text2.text("B to return to Menu")
    text.append(text2)

    # sets the background to span across the whole screen
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # sets refresh rate to 60 times a second
    game = stage.Stage(ugame.display, constants.FPS)

    # adds background to list
    game.layers = text + [background]
    game.render_block()

    # repeats forever, loops game
    while True:
        # get the user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X != 0:
            menu_scene()

        # update the game logic
        game.tick()


def menu_scene():
    # this function is for the menu screen

    # image banks from the PyBadge files directory
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(30, 10)
    text1.text("  EVIL QUINN   \n     V.S    \n    BERTY    \n      2      ")
    text.append(text1)

    text2 = stage.Text(
        width=19, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(31, 80)
    text2.text("Press START\nto play    \n\nPress SELECT\nfor tutorial")
    text.append(text2)

    # sets the background to span across the whole screen
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(2, 3)
            background.tile(x_location, y_location, tile_picked)

    # sets refresh rate to 60 times a second
    game = stage.Stage(ugame.display, constants.FPS)

    # adds background to list
    game.layers = text + [background]
    game.render_block()

    # repeats forever, loops game
    while True:
        # get the user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_START != 0:
            game_scene()
        if keys & ugame.K_SELECT != 0:
            tutorial_scene()

        # update the game logic
        game.tick()


def splash_scene():
    # this function is for the splash screen

    # image banks from the PyBadge files directory
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(30, 50)
    text1.text("  BIG BERT  \nGAME STUDIOS")
    text.append(text1)

    # sets the background to span across the whole screen
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # sets refresh rate to 60 times a second
    game = stage.Stage(ugame.display, constants.FPS)

    # adds background to list
    game.layers = text + [background]
    game.render_block()

    while True:
        # waits two seconds
        time.sleep(2.0)
        menu_scene()


splash_scene()

if __name__ == "__main__":
    menu_scene()
