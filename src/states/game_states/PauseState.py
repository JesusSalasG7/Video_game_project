
from typing import Dict, Any

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text
from gale.timer import Timer

import settings


class PauseState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.level = enter_params["level"]
        self.camera = enter_params["camera"]
        self.game_level = enter_params["game_level"]
        self.tilemap = self.game_level.tilemap
        self.player = enter_params["player"]
        self.boss = enter_params.get("boss")
        self.move_boss = enter_params.get("move_boss")
        self.band = enter_params.get("band")
        self.lives_boss = enter_params.get("lives_boss")
        self.lives = enter_params.get("lives")
        pygame.mixer.music.pause()

    def exit(self) -> None:
        pygame.mixer.music.unpause()

    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
        self.game_level.render(world_surface)
        self.player.render(world_surface)
        surface.blit(world_surface, (-self.camera.x, -self.camera.y))

        render_text(
            surface,
            "PAUSE",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2,
            (255, 255, 255),
            center=True,
            shadowed=True,
        )


    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "pause" and input_data.pressed:
            if self.level == 1:
                self.state_machine.change(
                    "play",
                    level=self.level,
                    camera=self.camera,
                    game_level=self.game_level,
                    player=self.player,   
                    lives = self.lives,
                )
            elif self.level == 2:
                self.state_machine.change(
                    "play",
                    level=self.level,
                    camera=self.camera,
                    game_level=self.game_level,
                    player=self.player,   
                    boss=self.boss,
                    move_boss = self.move_boss,
                    band =  self.band,
                    lives_boss = self.lives_boss,
                    lives = self.lives,
                )
