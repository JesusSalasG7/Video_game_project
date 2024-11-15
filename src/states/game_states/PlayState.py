
from typing import Dict, Any

import pygame

from gale.input_handler import InputData
from gale.state import BaseState

import settings
from src.Camera import Camera
from src.GameLevel import GameLevel
from src.Player import Player
from src.Boss import Boss


class PlayState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.level = enter_params.get("level", 1)
        self.game_level = GameLevel(self.level)
        self.tilemap = self.game_level.tilemap 
        self.player = enter_params.get(
            "player", Player(0, settings.VIRTUAL_HEIGHT - 66, self.game_level, "martian")
        )
        self.player.change_state("idle")
        self.boss = enter_params.get(
            "boss", Boss(250, settings.VIRTUAL_HEIGHT - 80,self.game_level, "Knight_Walk", self.player.x) 
        )
        self.boss.change_state("idle")

        self.camera = Camera(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
        self.camera.set_collision_boundaries(self.game_level.get_rect())
        self.camera.attach_to(self.player)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        self.player.on_input(input_id, input_data)

    def update(self, dt: float) -> None:
        self.player.update(dt)

        self.boss.update(dt)
        player = pygame.Vector2(self.player.x, self.player.y)
        boss = pygame.Vector2(self.boss.x, self.boss.y)
        
        if boss.distance_to(player) >= (self.boss.width/2 + self.player.width/2):
            self.boss.change_state("walk", self.player.x < self.boss.x, player)
        else:
            self.boss.change_state("idle")
        
        if boss.distance_to(player) <= (self.boss.width)*1.5:
            if player.y <= boss.y:
                if 0 <= abs(player.x - boss.x) <= 20:
                    self.boss.change_state("idle")
                else:
                    self.boss.change_state("walk", self.player.x < self.boss.x, player)
            else:
                self.boss.vx = 0
                self.boss.change_state("attack", player)
        else:
            if player.y <= boss.y:
                if 0 <= abs(player.x - boss.x) <= 20:
                    self.boss.change_state("idle")
                else:
                    self.boss.change_state("walk", self.player.x < self.boss.x, player)
                    
        self.camera.update()
        self.game_level.set_render_boundaries(self.camera.get_rect())
        self.game_level.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
        self.game_level.render(world_surface)
        self.player.render(world_surface)
        self.boss.render(world_surface)
        surface.blit(world_surface, (-self.camera.x, -self.camera.y))
