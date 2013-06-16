import sys
import serial
import time
from dispenser import *
from drink import *
class BarBot(object):
    def __init__(self, serial_port, dispensers={}, drinks={}, serial_baud=9600):
        self.port = serial.Serial(serial_port, serial_baud)
        self.dispensers = {}
        if isinstance(dispensers, list):
            for dispenser in dispensers:
                if isinstance(dispenser, Dispenser):
                    self.dispensers[dispenser.name] = Dispenser
                else:
                    raise TypeError
        else:
            raise TypeError

        self.drinks = {}
        if isinstance(drinks, list):
            for drink in drinks:
                if isinstance(drink, Drink):
                    self.drinks[drink.name] = drink
                else:
                    raise TypeError
        else:
            raise TypeError


    def close(self):
        self.port.close()

    def dispense(self, name):
        sys.stderr.write("dispensing {0}\n".format(name))
        self.port.write(self.dispensers[name].open_cmd)
        
    def stop_dispense(self, name):
        sys.stderr.write( "stop dispensing {0}\n".format(name))
        self.port.write(self.dispensers[name].close_cmd)
                
    def make_drink(self, drink_name, N = 1):

        drink = self.drinks[drink_name]
        # First check to make sure we have all the ingredients available.
        for step in drink.recipe:
            if step[0] not in self.dispensers:
                raise

        sys.stderr.write("Making a {0}\n".format(drink.name))

        # Now actually execute the recipe (naively)
        for step in drink.recipe:
            self.dispense(step[0])
            time.sleep(drink.timebase * N * step[1] - 0.5)
            self.stop_dispense(step[0])
            time.sleep(1)

        sys.stderr.write("Enjoy!\n".format(drink.name))

