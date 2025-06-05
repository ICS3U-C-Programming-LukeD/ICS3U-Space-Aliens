#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: May 5 , 2025

# pyright: reportMissingImports=false
import ugame
import stage

import constants


def menu_scene():

    # image banks from the PyBadge files directory
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(30, 10)
    text1.text("  BIG BERT  \nGAME STUDIOS")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(30, 110)
    text2.text("PRESS START!")
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
        if keys & ugame.K_START != 0:
            game_scene()

        # update the game logic
        game.tick()


def game_scene():

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

    # grabs image out of spritesheet bank and assigns it to ship variable
    ship = stage.Sprite(image_bank_sprite, 5, 75, 96)

    alien = stage.Sprite(
        image_bank_sprite,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # sets refresh rate to 60 times a second
    game = stage.Stage(ugame.display, constants.FPS)

    # adds background to list
    game.layers = [ship] + [alien] + [background]
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
            sound.play(pew_sound)
        # redraw sprites (not whole background)
        game.render_sprites([ship] + [alien])
        game.tick()


if __name__ == "__main__":
    menu_scene()
