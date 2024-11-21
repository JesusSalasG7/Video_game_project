
import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text

from gale.animation import Animation
from src.states import game_states


import settings

class FinalState(BaseState):
    def enter(self,level) -> None:
        self.level = level
       

    def render(self, surface: pygame.Surface) -> None:

        if self.level == 1:
            surface.fill((100, 100, 100))
        else:
            surface.fill((51, 25, 102))  

        render_text(
            surface,
            "FINAL",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
             settings.VIRTUAL_HEIGHT // 2,
            (255, 255, 255),
            center=True,
            shadowed=True,
        )
        
