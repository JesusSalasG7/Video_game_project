
import settings
from src.AdventureGame import AdventureGame

if __name__ == "__main__":
    adventure_game = AdventureGame(
        "Game Project",
        settings.WINDOW_WIDTH,
        settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH,
        settings.VIRTUAL_HEIGHT,
    )
    adventure_game.exec()
