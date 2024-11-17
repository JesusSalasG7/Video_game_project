
from typing import Any, List
import pygame
import settings

from gale.timer import Timer
from gale.state import BaseState
from gale.state import StateMachine

class FadeInState(BaseState):
    def enter(self) -> None:
        self.transition_alpha = 255
        self.level_label_y = -64
        # A surface that supports alpha for the screen
        self.screen_alpha_surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA
        )

         # first, over a period of 1 second, transition out alpha to 0
        # (fade-in).
        Timer.tween(
            1,
            [(self, {"transition_alpha": 0})],
            # once that is finished, start a transition of our text label to
            # center of the screen over 0.25 seconds
            on_finish=lambda: Timer.tween(
                0.25,
                [(self, {"level_label_y": settings.VIRTUAL_HEIGHT // 2 - 30})],
                # after that, pause for 1.5 second with Timer.after
                on_finish=lambda: Timer.after(
                    1.5,
                    # Then, animate the label going down past the bottom edge
                    lambda: Timer.tween(
                        0.25,
                        [(self, {"level_label_y": settings.VIRTUAL_HEIGHT + 30})],
                        # We are ready to play
                        on_finish=lambda: self.state_machine.change("play")
                    ),
                ),
            ),
        )
    
   

        