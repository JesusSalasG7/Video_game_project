"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class GameOverState.
"""

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text

from src.animacion import SpriteAnimado


import settings
import time

class GameOverState(BaseState):
    def enter(self, player, level) -> None:
        self.player = player
        self.level = level
        settings.SOUNDS["gameover"].play()

        #self.animacion = SpriteAnimado(settings.VIRTUAL_WIDTH // 2 - 32, settings.VIRTUAL_HEIGHT // 2, 32, 23,"dead", animation_defs={"dead": {"frames": [0, 1, 2, 3,], "interval": 0.10},},)

    #def update(self, dt: float) -> None:
        #self.animacion.update(dt)


    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "enter" and input_data.pressed:
            settings.SOUNDS["gameover"].stop()
            self.state_machine.change("play")

    def render(self, surface: pygame.Surface) -> None:

        if self.level == 1:
            surface.fill((100, 100, 100))
        else:
            surface.fill((51, 25, 102))  

        render_text(
            surface,
            "Game Over",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            20,
            (255, 255, 255),
            center=True,
            shadowed=True,
        )

        #self.animacion.render(surface)

        surface.blit(
            settings.TEXTURES["dead"],
            (settings.VIRTUAL_WIDTH // 2 - 16 , settings.VIRTUAL_HEIGHT // 2),
            settings.FRAMES["dead"][0],
        )

            
            


        render_text(
            surface,
            "Press Enter to play again",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 20,
            (255, 255, 255),
            center=True,
            shadowed=True,
        )
