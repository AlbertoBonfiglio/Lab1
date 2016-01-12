#!/usr/bin/python3

import numpy as np
from classes.damper import Damper
import matplotlib.pyplot as plt

def main():
    _damper = Damper(m=1.0, k=1.0, c=0)
    _y = _damper.dampOverTime(x=1.0, x_dot=0.0, t=0.01, epoch=1000)
    plt.plot(_y, label =" function")
    plt.show()

    _damper = Damper(m=1.0, k=1.0, c=1.0)
    _y = _damper.dampOverTime(x=1.0, x_dot=0.0, t=0.01, epoch=1000)
    plt.plot(_y, label =" function")
    plt.show()

    _damper = Damper(m=1.0, k=1.0, c=1.0)
    _y = _damper.dampOverTime(x=1.0, x_dot=1.0, t=0.01, epoch=1000)
    plt.plot(_y, label =" function")
    plt.show()


if __name__ == "__main__":
    main()
   