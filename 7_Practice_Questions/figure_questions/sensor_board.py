# Scenario:
# You are developing test automation for a robotic subassembly. 
# The subassembly includes three digital sensors connected via a simulated UART interface.

# 1.) Create a class called SensorTestRunner that runs test on all sensor and has a pass/fail limits

# | Sensor      | Min  | Max  |
# | ----------- | ---- | ---- |
# | temperature | 25.0 | 70.0 |
# | voltage     | 3.3  | 4.2  |
# | current     | 0.5  | 1.5  |

# 2.) Implement retry once if there is IOError

# 3.) Log test results in a csv

# timestamp,sensor,value,status
# 2025-06-26 14:35:23,temperature,63.5,PASS
# 2025-06-26 14:35:23,current,2.2,FAIL

import random
import time
import csv
import os

class SensorBoard:
    def __init__(self):
        self.sensors = {
            "temperature": lambda: round(random.uniform(20.0, 80.0), 2),
            "voltage": lambda: round(random.uniform(3.0, 5.0), 2),
            "current": lambda: round(random.uniform(0.1, 2.0), 2),
        }

    def read_sensor(self, name):
        time.sleep(0.1)  # simulate delay
        if name not in self.sensors:
            raise ValueError("Sensor not found")
        # if random.random() < 0.05:
            raise IOError("Communication error")  # simulate occasional failure
        return self.sensors[name]()
    
class SensorTestRunner:
    def __init__(self, logfile="results.csv"):
        self.limit = {
            "temperature": {
                "low": 25.0,
                "high": 70
            },
            "voltage": {
                "low": 3.3,
                "high": 4.2
            },
            "current": {
                "low": 0.5,
                "high": 1.5
            }
        }
        self.logfile = logfile
        self.datetime = time.localtime()
        self.results = []
        self.retry = 0
        self.value = None
        self.status = None

    def verify_sensor(self,names):
        # read value
        # compare the value to the limits
        # add line to csv
        # retry if needed
        for name in names:          
            self.value = SensorTestRunner().read_with_retry(name)
            if self.limit[f"{name}"]["low"] <= self.value <= self.limit[f"{name}"]["high"]:
                self.status = "pass"
            else:
                self.status = "fail"

            self.results.append(
                [
                f"{self.datetime.tm_year}-{self.datetime.tm_mon}-{self.datetime.tm_mday} {self.datetime.tm_hour}:{self.datetime.tm_min}:{self.datetime.tm_sec}",
                name,
                self.value,
                self.status
                ]
            )
            
        return SensorTestRunner().test_results()

    def read_with_retry(self,name):
        try:
            return SensorBoard().read_sensor(name)
        except IOError:
            return SensorBoard().read_sensor(name)

    def test_results(self):
        pwd = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(pwd, self.logfile)
        with open(csv_path, mode="w", newline="", ) as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "sensor", "value", "status"])
            writer.writerows(self.results)

names = ["temperature", "voltage", "current"]
testcase1 = SensorTestRunner()
testcase1.verify_sensor(names)
testcase1.test_results()



    

