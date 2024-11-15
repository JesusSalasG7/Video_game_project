
from typing import Dict, Any

import pygame

from gale.factory import AbstractFactory
from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text
from gale.timer import Timer

import settings
from src.Camera import Camera
from src.Clock import Clock
from src.GameLevel import GameLevel
from src.Player import Player
from src.powerups.Shot import Shot
from gale.factory import Factory
import src.powerups


class PlayState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.level = enter_params.get("level", 1)
        self.lives = 3
        self.win = False
        self.game_level = enter_params.get("game_level")

        self.shots = enter_params.get("shots", [])

        if self.game_level is None:
            self.game_level = GameLevel(self.level)
            pygame.mixer.music.load(
                settings.BASE_DIR / "assets" / "sounds" / "musicWorld.ogg"
            )
            pygame.mixer.music.play(loops=-1)

        self.tilemap = self.game_level.tilemap
        self.player = enter_params.get("player")
        if self.player is None:
            self.player = Player(-0, 400 - 60, self.game_level)
            self.player.change_state("idle")

        self.camera = enter_params.get("camera")

        if self.camera is None:
            self.camera = Camera(0, 192, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
            self.camera.set_collision_boundaries(self.game_level.get_rect())
            self.camera.attach_to(self.player)

        
    def update(self, dt: float) -> None:

        if self.player.is_dead:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            Timer.clear()
            self.state_machine.change("game_over", self.level)
    
        self.player.update(dt)

        for shot in self.shots:
            shot.update(dt) 

        if self.player.y >= self.player.tilemap.height:
            self.player.change_state("dead")

        self.camera.update()
        self.game_level.set_render_boundaries(self.camera.get_rect())
        self.game_level.update(dt)

        for creature in self.game_level.creatures:
            if self.player.collides(creature):
                if self.player.texture_id == "Knight_Attack":
                    self.game_level.creatures.remove(creature)
                    settings.SOUNDS["dead"].play()

                elif self.lives == 0: 
                    self.player.change_state("dead")

                elif not self.player.wounded:
                    settings.SOUNDS["wounded"].play()
                    self.lives-=1    
                    self.player.wounded = True
                    Timer.after(3,self.player.recovery)

        for item in self.game_level.items:
            if not item.active or not item.collidable:
                continue

            if self.player.collides(item):
                item.on_consume(self.player) 
                if self.player.pickup_key: 
                    item.on_collide(self.player)
                 

        for trap in self.game_level.traps:
            if self.player.collides(trap):
                
                if self.lives == 0: 
                    self.player.change_state("dead")

                elif not self.player.wounded:
                    settings.SOUNDS["wounded"].play()
                    self.lives-=1    
                    self.player.wounded = True
                    Timer.after(3,self.player.recovery)

        if self.player.open_door:

            Timer.after(
                1,
                self.next_level
            )
            


    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
        self.game_level.render(world_surface)
        self.player.render(world_surface)
        surface.blit(world_surface, (-self.camera.x, -self.camera.y))

        heart_x = settings.VIRTUAL_WIDTH - 40

        i = 0
        # Draw filled hearts
        while i < self.lives:
            surface.blit(
                settings.TEXTURES["hearts"], (heart_x, 5), settings.FRAMES["hearts"][0]
            )
            heart_x += 11
            i += 1

        render_text(
            surface,
            f"Score: {self.player.score}",
            settings.FONTS["small"],
            5,
            5,
            (255, 255, 255),
            shadowed=True,
        )  

        for shot in self.shots:
            shot.render(surface)    


    def next_level(self) -> None:   
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        Timer.clear()
        self.state_machine.change(
                    "winer_level",
                    level= self.level + 1,
                    )                

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "pause" and input_data.pressed:
            Timer.pause()
            self.state_machine.change(
                "pause",
                level=self.level,
                camera=self.camera,
                game_level=self.game_level,
                player=self.player,   
            )
        elif input_id == "f" and input_data.pressed:
            if self.player.powerUP:
                        self.shot_factory = Factory(Shot)
                        print(self.player.x, self.player.y)
                        
                        collision_rect = self.player.get_collision_rect()
                        
                        x = self.tilemap.to_x(collision_rect.centery)
                        y = self.tilemap.to_y(collision_rect.left)
                        print(x, y)

                        x = self.tilemap.to_i(collision_rect.centery)
                        y = self.tilemap.to_j(collision_rect.left)
                        print(x, y)
                        #x= x*16
                        #y= y*16


                        a = self.shot_factory.create(self.player.x  / settings.WINDOW_HEIGHT  , self.player.y / settings.WINDOW_WIDTH)
                        self.shots.append(a) 
        else:
            self.player.on_input(input_id, input_data)

