"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition for creatures.
"""

from typing import Dict, Any

from src.states.entities import creatures_states

CREATURES: Dict[int, Dict[str, Any]] = {
    56: {
        "texture_id": "creatures",
        "walk_speed": 25,
        "animation_defs": {"walk": {"frames": [56],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    57: {
        "texture_id": "creatures",
        "walk_speed": 25,
        "animation_defs": {"walk": {"frames": [57],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    58: {
        "texture_id": "creatures",
        "walk_speed": 25,
        "animation_defs": {"walk": {"frames": [58],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    59: {
        "texture_id": "creatures",
        "walk_speed": -25,
        "animation_defs": {"walk": {"frames": [59],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    }, 
    64: {
        "texture_id": "creatures",
        "walk_speed": -25,
        "animation_defs": {"walk": {"frames": [64],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },    
    65: {
        "texture_id": "creatures",
        "walk_speed": -25,
        "animation_defs": {"walk": {"frames": [65],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    66: {
        "texture_id": "creatures",
        "walk_speed": -25,
        "animation_defs": {"walk": {"frames": [66],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    67: {
        "texture_id": "creatures",
        "walk_speed": -25,
        "animation_defs": {"walk": {"frames": [67],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    59: {
        "texture_id": "creatures",
        "walk_speed": -25,
        "animation_defs": {"walk": {"frames": [59],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    }, 
}