from RPG.scripts.game import Game
from RPG.scripts.game_processes.main_process import main_process
from RPG.scripts.utilities import load_level

game = Game()
game.start_new_game(load_level('resources/level_maps/level.txt'))
main_process(game)
