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
    
    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    
    # gets sounds ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # sets the background to span across the whole screen
    background = stage.Grid(image_bank_background,
    constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # grabs image out of spritesheet bank and assigns it to ship variable
    ship = stage.Sprite(image_bank_sprite, 5, 75, 96)
    
    alien = stage.Sprite(image_bank_sprite, 9,
    int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)

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
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("Select")
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
    game_scene()
