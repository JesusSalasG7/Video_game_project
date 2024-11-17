from pathlib import Path

import pygame

from gale import frames
from gale import input_handler

from src import loaders

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_d, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_a, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP_ENTER, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_SPACE, "jump")
#input_handler.InputHandler.set_keyboard_action(input_handler.KEY_x, "attack")
input_handler.InputHandler.set_mouse_click_action(input_handler.MOUSE_BUTTON_1, "jump")
#input_handler.InputHandler.set_mouse_click_action(input_handler.MOUSE_BUTTON_3, "attack")

# Size we want to emulate
VIRTUAL_WIDTH = 400
VIRTUAL_HEIGHT = 192

# Size of our actual window
WINDOW_WIDTH = VIRTUAL_WIDTH * 4
WINDOW_HEIGHT = VIRTUAL_HEIGHT * 4

PLAYER_SPEED = 80

BOSS_SPEED = 60

GRAVITY = 980

NUM_LEVELS = 1

BASE_DIR = Path(__file__).parent

LevelLoader = loaders.TmxLevelLoader

TEXTURES = {
    "tiles": pygame.image.load(BASE_DIR / "assets" / "textures" / "tileset.png"),
    "Knight_Walk": pygame.image.load(BASE_DIR / "assets" / "textures" / "Knight_Walk.png"),
    "Knight_Attack": pygame.image.load(BASE_DIR / "assets" / "textures" / "Knight_Attack.png"),
    "martian": pygame.image.load(BASE_DIR / "assets" / "textures" / "martian.png"),
    "background": pygame.image.load(BASE_DIR / "assets" / "textures" / "background.png"),
    "Begin": pygame.image.load(BASE_DIR / "assets" / "textures" / "Begin.png"),
    "End": pygame.image.load(BASE_DIR / "assets" / "textures" / "End.png"),
    "Dialogo1": pygame.image.load(BASE_DIR / "assets" / "textures" / "Dialogo1.png"),
    "Dialogo2": pygame.image.load(BASE_DIR / "assets" / "textures" / "Dialogo2.png"),
}

FRAMES = {
    "tiles": frames.generate_frames(TEXTURES["tiles"], 16, 16),
    "Knight_Walk": frames.generate_frames(TEXTURES["Knight_Walk"], 25, 32),
    "Knight_Attack": frames.generate_frames(TEXTURES["Knight_Attack"], 34, 32),
    "martian": frames.generate_frames(TEXTURES["martian"], 16, 20),
}

TILEMAPS = {
    i: BASE_DIR / "assets" / "tilemaps" / f"level{i}" for i in range(1, NUM_LEVELS + 1)
}

pygame.font.init()

FONTS = {
    "small": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 8),
    "medium": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 16),
}
