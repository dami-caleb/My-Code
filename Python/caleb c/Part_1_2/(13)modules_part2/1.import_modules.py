import sys #sys makes it possible use files (modules that are in other directories from our current directory)

from os.path import dirname, abspath
d = dirname(dirname(abspath(_file_)))

sys.path.append(d)

import update_guessing_game

update_guessing_game.game()
