import time
import csv
import sys
from mag3110 import Mag3110Driver
from data_collector import DataCollector

if __name__ == "__main__":

    #  d = Dummy(2, 5)

    d = Mag3110Driver(1, "battery", 30)
    dc = DataCollector("mag3110",sys.argv[2],d)
     #  d = Hmc5883Driver(1, 30)
#    d = Qmc5883Driver(1, 30)
    #  d = Lis3mdlDriver(1, 30)
    #  dc = DataCollector("lis3mdl",sys.argv[2],d)
    #dc = DataCollector("mag3110",sys.argv[0],d)
    #  dc.collectData(0.1, int(sys.argv[1]))
    dc.printData(0.1, 1000)

