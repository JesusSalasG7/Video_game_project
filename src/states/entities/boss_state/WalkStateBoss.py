
import pygame

import settings
from src.GameObject import GameObject
from src.states.entities.BaseEntityState import BaseEntityState

class WalkStateBoss(BaseEntityState):
    def enter(self, flipped: bool, position_player: pygame.math.Vector2) -> None:
        self.entity.change_animation("walk")
        self.entity.vx = settings.BOSS_SPEED
        self.position_player = position_player
        self.entity.flipped = flipped
        if self.entity.flipped:
             self.entity.vx *= -1

    def update(self, dt: float) -> None:
        if self.check_boundary():
            if self.entity.tilemap.check_solidness_on(int(self.entity.tilemap.to_i(self.entity.y)) + 2, int(self.entity.tilemap.to_j(self.entity.x + self.entity.width)), GameObject.TOP) or self.entity.tilemap.check_solidness_on(int(self.entity.tilemap.to_i(self.entity.y)) + 2, int(self.entity.tilemap.to_j(self.entity.x)), GameObject.TOP):
                self.entity.change_state("idle")
            elif (self.entity.x, self.entity.x).ditance_to(self.position_player) <= 15:
                self.entity.change_state("attack")
            self.entity.vx *= -1
            self.entity.flipped = not self.entity.flipped
            

    def check_boundary(self) -> bool:
        world_width = self.entity.tilemap.width

        if self.entity.x + self.entity.width >= world_width:
            self.entity.x = world_width - self.entity.width
            return True
        elif self.entity.x <= 0:
            self.entity.x = 0
            return True

        if (
            self.entity.handle_tilemap_collision_on_left()
            or self.entity.handle_tilemap_collision_on_right()
        ):
            return True

        # Avoid falling
        can_fall = False
        
        #Nota debido a las dimensiones del personas se le suma una posicion mas a las columnas
        if self.entity.vx > 0:
            
            row = int(self.entity.tilemap.to_i(self.entity.y))
            col = int(self.entity.tilemap.to_j(self.entity.x + self.entity.width))

            can_fall = not self.entity.tilemap.check_solidness_on(
                row + 2, col, GameObject.TOP
            )
        elif self.entity.vx < 0:
            
            row = int(self.entity.tilemap.to_i(self.entity.y))
            col = int(self.entity.tilemap.to_j(self.entity.x))

            can_fall = not self.entity.tilemap.check_solidness_on(
                row + 2, col, GameObject.TOP
            )

        return can_fall