
from gale.input_handler import InputData

import settings
from src.states.entities.BaseEntityState import BaseEntityState
from gale.timer import Timer

class AttackState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.change_animation("attack")
        self.entity.texture_id = "Knight_Attack" 
        settings.SOUNDS["attack"].stop()
        settings.SOUNDS["attack"].play()
       
    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "attack" and input_data.released:
                self.entity.change_state("idle")