import numpy as np
import os

go = True
while go:
    new_random = np.random.randint(10000000000)
    os.system(f"figlet {new_random} | lolcat")
