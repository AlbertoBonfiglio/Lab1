#!/usr/bin/python3

import numpy
from classes.damper import Damper
import matplotlib.pyplot as plt

def main():

    x = numpy.arange(0, 1000, 1)

    _damper = Damper(m=1.0, k=1.0, c=0)
    _y0 = _damper.dampOverTime(x=1.0, x_dot=0.0, t=0.01, epoch=1000, out=True)

    _damper = Damper(m=1.0, k=1.0, c=1.0)
    _y1 = _damper.dampOverTime(x=1.0, x_dot=0.0, t=0.01, epoch=1000, out=True)

    _damper = Damper(m=1.0, k=1.0, c=1.0)
    _y2 = _damper.dampOverTime(x=1.0, x_dot=1.0, t=0.01, epoch=1000, out=True)

    #Plots the various functions . From an example at http://matplotlib.org/examples/pylab_examples/subplots_demo.html
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)
    ax1.plot(x, _y0)
    ax1.set_title('Damping Simulations')
    ax2.plot(x, _y1)
    ax3.plot(x, _y2)
    f.subplots_adjust(hspace=0.2)
    plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
    plt.show()


if __name__ == "__main__":
    main()
   