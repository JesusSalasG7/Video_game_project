import pygame

from gale.game import Game
from gale.input_handler import InputData
from gale.state import StateMachine

from src.states import game_states
from gale.state import StateStack
from src.Puzzle.Board import Board
class RescueofCeleste(Game):
    def init(self) -> None:
        self.state_machine = StateMachine(
            {
                "play": game_states.PlayState,
                "game_over": game_states.GameOverState,
                "winer_level": game_states.WinerLevelState,
                "pause": game_states.PauseState,
                "start": game_states.StartState,
            }
        )

        self.state_stack = StateStack()
        self.state_stack.push(game_states.ScenaState(self.state_stack), "Begin")
        self.state_stack.push(game_states.StartState(self.state_stack))
    
    def update(self, dt: float) -> None:
        self.state_stack.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        self.state_stack.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()
        else:
            self.state_stack.on_input(input_id, input_data)
