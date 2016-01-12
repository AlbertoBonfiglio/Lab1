#!/usr/bin/python3

import numpy as np
from classes.damper import Damper
import matplotlib.pyplot as plt

def main():
    _damper = Damper(m=1.0, k=1.0, c=1.0)
    _y = _damper.damp(x=1.0, x_dot=0.0, t=0.1, epoch=1000)
     

    plt.plot( _y, label =" function")
    plt.show()



if __name__ == "__main__":
    main()
   