
import pygame
from src.states.entities.BaseEntityState import BaseEntityState

class AttackStateBoss(BaseEntityState):
    def enter(self, position_player: pygame.math.Vector2) -> None:
        print("Esta atacando")
        # if pygame.math.Vector2(self.entity.x, self.entity.y).distance_to(position_player) <= 25:
        #     self.entity.vx = 0
        #     self.entity.vy = 0
        #     self.entity.change_animation("attack")
        #     self.entity.texture_id = "Knight_Attack"
        # elif pygame.math.Vector2(self.entity.x, self.entity.y).distance_to(position_player) >= 40:
        #     self.entity.change_state("walk", position_player.x < self.entity.x, position_player)
        # else:
        #     self.entity.change_state("idle")