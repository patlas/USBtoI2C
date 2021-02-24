class Driver:
    def __init__(self, i2c_id:int, read_freq):
        pass

    def __enter__(self):
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit called")

    def getMeasurement(self):
        pass



from random import seed, randint

class Dummy(Driver):

    def __init__(self, i2c_id, freq):
        self.name="Dummy"
        seed(1)

    def getMeasurement(self, readTemp=False):
        m = [randint(-32000, 32000), randint(-32000, 32000), randint(-32000, 32000)]        
        if readTemp:
            m.append(randint(15,30))

        return m
    
    def scaleMeasurement(self, m):
        s = []
        for i in range(3):
            s.append(m[i]/100)

        return s

