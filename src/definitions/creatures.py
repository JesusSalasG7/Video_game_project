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

    0: {
        "texture_id": "dead_Walk",
        "walk_speed": 25,
        "animation_defs": {"fly": {"frames": [0],}},
        "states": {"fly": creatures_states.FlyState},
        "first_state": "fly",
    },
    10: {
        "texture_id": "creatures3",
        "walk_speed": 30,
        "animation_defs": {"walk": {"frames": [9,10,11],"interval": 0.25}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    36: {
        "texture_id": "creatures",
        "walk_speed": 50,
        "animation_defs": {"fly": {"frames": [36,37,], "interval": 0.15}},
        "states": {"fly": creatures_states.FlyState},
        "first_state": "fly",
    },
    49: {
        "texture_id": "creatures",
        "walk_speed": 25,
        "animation_defs": {"walk": {"frames": [49],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    51: {
        "texture_id": "creatures",
        "walk_speed": -25,
        "animation_defs": {"walk": {"frames": [51],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    52: {
        "texture_id": "creatures",
        "walk_speed": 25,
        "animation_defs": {"walk": {"frames": [52],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    53: {
        "texture_id": "creatures",
        "walk_speed": 40,
        "animation_defs": {"walk": {"frames": [53],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    56: {
        "texture_id": "creatures",
        "walk_speed": 25,
        "animation_defs": {"walk": {"frames": [56],}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },
    57: {
        "texture_id": "creatures",
        "walk_speed": 40,
        "animation_defs": {"fly": {"frames": [57],}},
        "states": {"fly": creatures_states.FlyState},
        "first_state": "fly",
    },
    58: {
        "texture_id": "creatures",
        "walk_speed": 60,
        "animation_defs": {"fly": {"frames": [58],}},
        "states": {"fly": creatures_states.FlyState},
        "first_state": "fly",
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
        "animation_defs": {"walk": {"frames": [64, 65],"interval": 0.70}},
        "states": {"walk": creatures_states.WalkState},
        "first_state": "walk",
    },    
    66: {
        "texture_id": "creatures",
        "walk_speed": -35,
        "animation_defs": {"walk": {"frames": [66, 67],"interval": 0.70}},
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

}

