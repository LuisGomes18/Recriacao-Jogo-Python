import sys
import os
from random import randint


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extras.extra_def import welcome
from niveis.fase_bebe import fase_bebe
from niveis.fase_crianca import fase_crianca


welcome()
fase_bebe()
fase_crianca()
