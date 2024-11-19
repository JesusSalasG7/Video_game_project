
from typing import Any, Dict
import pygame

import settings

from gale.input_handler import InputData
from gale.state import BaseState
from gale.timer import Timer

from gale.state import StateStack
from gale.text import Text, render_text
from src.states import game_states

class ScenaState(BaseState):
    def enter(self, text: str) -> None:
        self.dialogo = "Caballero, nuestro reino esta envuelto en sombras.\nLa malvada criatura ha secuestrado a la\nprincesa, nuestra esperanza y guia. \nSolo tu puedes enfrentarte a esta oscuridad y devolver la paz.\n Ve ahora, rescata a nuestra amada princesa\n y devuelve la esperanza a nuestro pueblo"
        self.linea = self.dialogo.split("\n")
        self.index = 0
        self.parrafo = len(self.linea)
        self.alpha_transition = 0
        self.text = text
        # A surface that supports alpha for the screen
        self.screen_alpha_surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA
        )

        # A surface that supports alpha for the title and the menu
        self.text_alpha_surface = pygame.Surface((300, 58), pygame.SRCALPHA)
        pygame.draw.rect(
            self.text_alpha_surface, (255, 255, 255, 128), pygame.Rect(0, 0, 300, 58)
        )
        self.active = True

    def render(self, surface: pygame.Surface) -> None:
        self.surface = surface
        ancho_original, alto_original = settings.TEXTURES[self.text].get_size()

        # Calcular factor de escalado
        factor_ancho = settings.VIRTUAL_WIDTH / ancho_original
        factor_alto = settings.VIRTUAL_HEIGHT / alto_original
        factor_escalado = min(factor_ancho, factor_alto)
        
        # Calcular el nuevo tamaño escalado
        nuevo_ancho = int(ancho_original * factor_escalado)
        nuevo_alto = int(alto_original * factor_escalado)

        # Escalar la imagen usando smoothscale
        imagen_escalada = pygame.transform.smoothscale(settings.TEXTURES[self.text], (nuevo_ancho, nuevo_alto))
        
        # Calcular las coordenadas para centrar la imagen
        x = (settings.VIRTUAL_WIDTH - nuevo_ancho) // 2
        y = (settings.VIRTUAL_HEIGHT - nuevo_alto) // 2

        surface.fill((0, 0, 0))
        surface.blit(imagen_escalada, (x, y))
        
        render_text(
                surface,
                self.linea[self.index],
                    settings.FONTS["small"],
                    settings.VIRTUAL_WIDTH // 2,
                    settings.VIRTUAL_HEIGHT // 2 + 40,
                    (197, 195, 198),
                    center=True,
                    shadowed=True,
            )

        pygame.draw.rect(
            self.screen_alpha_surface,
            (255, 255, 255, self.alpha_transition),
            pygame.Rect(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT),
        )
        surface.blit(self.screen_alpha_surface, (0, 0))

    def on_input(self, input_id: str, input_data: InputData) -> None:

        def finish_dialogs():
             self.state_machine.pop()
             self.state_machine.push(game_states.PlayState(self.state_machine))

        if input_id == "enter" and input_data.pressed and self.active:
                if self.index < self.parrafo - 1:
                    self.index += 1
                else:
                    self.active = False
                    self.index = 0
                    Timer.tween(
                        1,
                        [(self, {"alpha_transition": 255})],
                        on_finish=finish_dialogs
                    )

