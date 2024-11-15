from typing import TypeVar

from src.GameEntity import GameEntity
from src.states.entities import boss_state

class Boss(GameEntity):
    def __init__(
        self,
        x: float,
        y: float,
        game_level: TypeVar("GameLevel"),
        texture_id: str,
        position_player: float
    ) -> None:
        super().__init__(
            x,
            y,
            25,
            32,
            texture_id,
            game_level,
            states={
                "idle": lambda sm: boss_state.IdleStateBoss(self, sm),
                "walk": lambda sm: boss_state.WalkStateBoss(self, sm),
                "attack": lambda sm: boss_state.AttackStateBoss(self, sm),
            #     "jump": lambda sm: player_states.JumpState(self, sm),
            #     "fall": lambda sm: player_states.FallState(self, sm),
            },
            animation_defs={
                "idle": {"frames": [0]},
                "walk": {"frames": [1, 10], "interval": 0.15},
                "jump": {"frames": [9]},
            }
        )
        self.position_player = position_player
        self.state_machine.change("idle")