
from src.states.entities.BaseEntityState import BaseEntityState


class DeadState(BaseEntityState):
    def enter(self) -> None:
        self.entity.is_dead = True
