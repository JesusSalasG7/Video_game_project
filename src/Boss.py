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
        #position_player: float
    ) -> None:
        super().__init__(
            x,
            y,
            20,
            59,
            texture_id,
            game_level,
            states={
                "idle": lambda sm: boss_state.IdleStateBoss(self, sm),
                "walk": lambda sm: boss_state.WalkStateBoss(self, sm),
                "attack": lambda sm: boss_state.AttackStateBoss(self, sm),
            #     "fall": lambda sm: player_states.FallState(self, sm),
            },
            animation_defs={
                "idle": {"frames": [0]},
                "walk": {"frames": [0], "interval": 0.20},
                "attack": {"frames": [4]},
            }
        )
        self.wounded = False 
        self.state_machine.change("idle")


    def recovery(self) -> None:
        self.wounded = False
       