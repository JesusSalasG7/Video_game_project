"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition for tiles.
"""

from typing import Dict, Any

TILES: Dict[str, Dict[int, Dict[str, Any]]] = {
    "tiles" : {
    # Ground
        0: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        1: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        2: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        3: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        4: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        5: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        5: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        8: {"solidness": dict(top=False, right=False, bottom=False, left=False)},
        10: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        42: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        43: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        44: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        24: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        25: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
        26: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    # Blocks
        7: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
        11: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
        18: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
        28: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
        77: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
        78: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
        79: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
        6: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
        17: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
        41: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
        56: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    },
    "block" : {
        10: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    }
}
