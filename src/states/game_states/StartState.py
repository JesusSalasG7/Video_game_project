from typing import Any
import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.state import StateMachine
from gale.text import Text, render_text
from gale.timer import Timer
from PIL import Image

import settings

class StartState(BaseState):
    def render(self, surface: pygame.Surface) -> None:
        ancho_original, alto_original = settings.TEXTURES["background"].get_size()
        
        # Calcular factor de escalado
        factor_ancho = settings.VIRTUAL_WIDTH / ancho_original
        factor_alto = settings.VIRTUAL_HEIGHT / alto_original
        factor_escalado = min(factor_ancho, factor_alto)
        
        # Calcular el nuevo tamaño escalado
        nuevo_ancho = int(ancho_original * factor_escalado)
        nuevo_alto = int(alto_original * factor_escalado)
        
        # Escalar la imagen usando smoothscale
        imagen_escalada = pygame.transform.smoothscale(settings.TEXTURES["background"], (nuevo_ancho, nuevo_alto))
        
        # Calcular las coordenadas para centrar la imagen
        x = (settings.VIRTUAL_WIDTH - nuevo_ancho) // 2
        y = (settings.VIRTUAL_HEIGHT - nuevo_alto) // 2
        
        surface.blit(imagen_escalada, (x, y))

        render_text(
            surface,
            "Press Enter",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2 + 40,
            (197, 195, 198),
            center=True,
            shadowed=True,
        )
    
    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "enter" and input_data.pressed:
            self.state_machine("play")