import pathlib

import pygame

from gale import frames
from gale import input_handler
from typing import Dict

from src import loaders

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_p, "pause")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP_ENTER, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_d, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_a, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_SPACE, "jump")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_x, "attack")
input_handler.InputHandler.set_mouse_click_action(input_handler.MOUSE_BUTTON_1, "jump")

# Size we want to emulate
VIRTUAL_WIDTH = 400
VIRTUAL_HEIGHT = 192

# Size of our actual window
WINDOW_WIDTH = VIRTUAL_WIDTH * 4
WINDOW_HEIGHT = VIRTUAL_HEIGHT * 4

PLAYER_SPEED = 80

GRAVITY = 1000

NUM_LEVELS = 2

POINTS = 50

TILEMAP: Dict[str, Dict[int, str] ]= {
    
    "level1": {

        #TEXTURAS
        (1,103):"tiles",
        (177,244):"creatures"
    },
    "level2": {
        
        #TEXTURAS
        (1,60):"tiles3",
        (61,72): "creatures3",
        (73,144): "creatures",
        (145,450) :"tiles",
    }
}

BASE_DIR = pathlib.Path(__file__).parent

LevelLoader = loaders.TmxLevelLoader

TEXTURES = {
    "tiles": pygame.image.load(BASE_DIR / "assets" / "textures" / "tileset.png"),
    "tiles3": pygame.image.load(BASE_DIR / "assets" / "textures" / "tileset3.png"),
    #"Knight": pygame.image.load(BASE_DIR / "assets" / "textures" / "knight.png"),
    "Knight_Walk": pygame.image.load(BASE_DIR / "assets" / "textures" / "Knight_Walk.png"),
    "Knight_Attack": pygame.image.load(BASE_DIR / "assets" / "textures" / "Knight_Attack.png"),
    "martian": pygame.image.load(BASE_DIR / "assets" / "textures" / "martian.png"),
    "creatures": pygame.image.load(BASE_DIR / "assets" / "textures" / "creatures.png"),
    "creatures2": pygame.image.load(BASE_DIR / "assets" / "textures" / "ghost-25x35.png"),
    "creatures3": pygame.image.load(BASE_DIR / "assets" / "textures" / "creatures3.png"),
   
}

FRAMES = {
    "tiles": frames.generate_frames(TEXTURES["tiles"], 16, 16),
    "tiles3": frames.generate_frames(TEXTURES["tiles3"], 16, 16),
    "martian": frames.generate_frames(TEXTURES["martian"], 16, 20),
    #"Knight": frames.generate_frames(TEXTURES["Knight"], 32, 32),
    "Knight_Walk": frames.generate_frames(TEXTURES["Knight_Walk"], 25, 32),
    "Knight_Attack": frames.generate_frames(TEXTURES["Knight_Attack"], 34, 32),
    "creatures": frames.generate_frames(TEXTURES["creatures"], 16, 16),
    "creatures2": frames.generate_frames(TEXTURES["creatures2"], 25, 35),
    "creatures3": frames.generate_frames(TEXTURES["creatures3"], 16, 18),

}

TILEMAPS = {
    i: BASE_DIR / "assets" / "tilemaps" / f"level{i}" for i in range(1, NUM_LEVELS + 1)
}

pygame.mixer.init()

SOUNDS = {
    "pickup_coin": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "pickup_coin.wav"),
    "jump": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "SFX_Jump_33.mp3"),
    "attack": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "attack.mp3"),
    "dead": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "dead.wav"),
    "timer": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "timer.wav"),
    "count": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "count.wav"),
    "win_level": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "Win_level.ogg"),
}


SOUNDS["pickup_coin"].set_volume(0.5)


pygame.font.init()

FONTS = {
    "small": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 8),
    "medium": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 16),
}
