import random

ANSI_RESET = "\033[0m"
ANSI_YELLOW = "\033[33m"
ANSI_GREEN = "\033[32m"
ANSI_BLUE = "\033[34m"
ANSI_RED = "\033[31m"
ANSI_WHITE = "\033[97m"
ANSI_MAGENTA = "\033[35m"
ANSI_CYAN = "\033[36m"

class Tile:
    def __init__(self, char: str):
        self.tile_definitions = {"X": {"name": "wall", "symbol": "X", "color": "\x1b[0;90;40m", "passable": False},
                                "c": {"name": "treasure chest", "symbol": "c", "color": "\x1b[0;33;40m", "passable": False},
                                #" ": {"name": "empty", "symbol": "_", "color": "\x1b[0;90;40m", "passable": True},
                                " ": {"name": "empty", "symbol": random.choice(['.', ',', '~']), "color": "\x1b[38;5;235m", "passable": True},
                                #" ": {"name": "empty", "symbol": " ", "color": ANSI_GREEN, "passable": True}
                                }
        self.symbol = self.tile_definitions[char]["symbol"]
        self.color = self.tile_definitions[char]["color"]
        self.passable = self.tile_definitions[char]["passable"]
        
    
    def __str__(self):
        str = f"{self.color}{self.symbol}{ANSI_RESET}"
        return str
    
    def random_char(self, charlist: list):
        pass

