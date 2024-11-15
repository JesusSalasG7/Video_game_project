"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition for items.
"""

from typing import Dict, Any

import random

from gale.timer import Timer

import settings
from src.GameItem import GameItem
from src.Player import Player


def pickup_key( player: Player) -> None:
    settings.SOUNDS["pickup_coin"].stop()
    settings.SOUNDS["pickup_coin"].play()
    player.pickup_key = True

def open_door( player: Player) -> None:
    settings.SOUNDS["pickup_coin"].stop()
    settings.SOUNDS["pickup_coin"].play()
    player.open_door = True    

def key( player: Player):
    pickup_key(player)

def door( player: Player):
    open_door(player)



ITEMS: Dict[str, Dict[int, Dict[str, Any]]] = {
    "coins": {

        74: {
            "texture_id": "tiles2",
            "solidness": dict(top=False, right=False, bottom=False, left=False),
            "consumable": True,
            "collidable": True,
            "on_collide": door,
        },
         82: {
            "texture_id": "tiles2",
            "solidness": dict(top=False, right=False, bottom=False, left=False),
            "consumable": True,
            "collidable": True,
            "on_collide": door,
        },
        90: {
            "texture_id": "tiles2",
            "solidness": dict(top=False, right=False, bottom=False, left=False),
            "consumable": True,
            "collidable": True,
            "on_consume": key,
        },

    },
}
