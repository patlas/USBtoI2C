import time
import csv
from Driver import Driver, Dummy

class DataCollector:

    def __init__(self, Dir, desc,  device:Driver):
        self.dev = device
        self.dir = Dir
        self.desc = desc

    def _getTimeStamp(self):
        return time.time()

    def collectData(self, interval, count):
        fname = "{}/{}_{}_{}.csv".format(self.dir, self.dev.name, str(self._getTimeStamp()).replace('.','_'),self.desc)

        with open(fname, mode='w') as fd:
            writer = csv.writer(fd, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            writer.writerow(['Timestamp', 'X', "Y", "Z", "X[uT]", "Y[uT]", "Z[uT]", "Temp"])

            for i in range(count):
                measurement = self.dev.getMeasurement()
                print("{}: X: {:.4f}uT, Y: {:.4f}uT, Z: {:.4f}uT".format(i, *self.dev.scaleMeasurement(measurement[:3])))
                writer.writerow([self._getTimeStamp(), *measurement[:3], *self.dev.scaleMeasurement(measurement), 0 if len(measurement)<4 else measurement[3]])
                time.sleep(interval)

    
    def printData(self, interval, count):

        for _ in range(count):
            measurement = self.dev.getMeasurement()
            print("X: {:.4f}uT, Y: {:.4f}uT, Z: {:.4f}uT".format(*self.dev.scaleMeasurement(measurement[:3])))
            time.sleep(interval)



#  if __name__ == "__main__":
#
#      #  d = Dummy(2, 5)
#
#      dc = DataCollector(d)
#      dc.collectData(0.1, 100)

