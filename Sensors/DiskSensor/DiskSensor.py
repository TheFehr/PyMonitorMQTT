import psutil
from Sensors.Sensor import Sensor


TOPIC = 'disk_used_percentage'


class DiskSensor(Sensor):
    def Initialize(self):
        self.AddTopic(TOPIC)

    def Update(self):
        self.SetTopicValue(TOPIC, self.GetDiskUsedPercentage())

    def GetDiskUsedPercentage(self):
        return psutil.disk_usage('/')[3]
