
from typing import TypeVar

from gale.input_handler import InputData

from src.GameEntity import GameEntity
from src.states.entities import player_states

class Player(GameEntity):
    def __init__(self, x: int, y: int, game_level: TypeVar("GameLevel"), texture_id: str) -> None:
        super().__init__(
            x,
            y,
            16,
            20,
            texture_id,
            game_level,
            states={
                "idle": lambda sm: player_states.IdleState(self, sm),
                "walk": lambda sm: player_states.WalkState(self, sm),
                "jump": lambda sm: player_states.JumpState(self, sm),
                "fall": lambda sm: player_states.FallState(self, sm),
                "attack": lambda sm: player_states.AttackState(self, sm), 
            },
            # animation_defs={
            #     "idle": {"frames": [0]},
            #     "walk": {"frames": [1, 10], "interval": 0.15},
            #     "jump": {"frames": [9]},
            #     "attack": {"frames": [0, 1], "interval": 0.10},
            # },
            animation_defs={
                "idle": {"frames": [0]},
                "walk": {"frames": [9, 10], "interval": 0.15},
                "jump": {"frames": [2]},
            },
        )
    
    def on_input(self, input_id: str, input_data: InputData) -> None:
        self.state_machine.on_input(input_id, input_data)