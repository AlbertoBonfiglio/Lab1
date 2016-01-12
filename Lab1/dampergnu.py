#!/usr/bin/python3

from classes.damper import Damper
import matplotlib.pyplot as plt

def select():
    isValid = False
    while isValid == False:
        try:
            retValue = int(input('Please select values:'))
            if retValue > 0 and retValue < 4:
                isValid = True
        except ValueError:
            print('Not a number')

    return retValue


def main():
    print(""" 1) - m=1.0, k=1.0, c=0.0, x=1.0, x_dot=0.0
        2) - m=1.0, k=1.0, c=1.0, x=1.0, x_dot=0.0
        3) - m=1.0, k=1.0, c=1.0, x=1.0, x_dot=1.0
        """)

    selectedValue = select()

    if selectedValue == 1:
        _damper = Damper(m=1.0, k=1.0, c=0.0)
        _y = _damper.dampOverTime(x=1.0, x_dot=0.0, t=0.01, epoch=1000)
    elif selectedValue == 2:
        _damper = Damper(m=1.0, k=1.0, c=1.0)
        _y = _damper.dampOverTime(x=1.0, x_dot=0.0, t=0.01, epoch=1000)
    elif selectedValue == 3:
        _damper = Damper(m=1.0, k=1.0, c=1.0)
        _y = _damper.dampOverTime(x=1.0, x_dot=1.0, t=0.01, epoch=1000)

    print(_y)

if __name__ == "__main__":
    main()
   