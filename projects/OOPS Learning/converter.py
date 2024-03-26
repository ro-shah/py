class ConvertTemperature:
    def __init__(self, temp: float):
        self.temp = temp
        assert temp >= 0, "Temp has to be greater than 0"

    def convert_to_fahrenheit(self):
        conversion = float((9 * self.temp) / 5 + 32)
        return conversion

    def convert_to_celsius(self):
        conversion = float((self.temp - 32) * 5 / 9)
        return conversion

which_conversion = input("Input temprature with unit at end (ex: 35 F): ")
temp = [which_conversion[0:-2], which_conversion[-1]]
if temp[1] == "C":
    tempfahrenheit = ConvertTemperature(int(temp[0]))
    print(str(round(tempfahrenheit.convert_to_fahrenheit(), 2)) + "°F")
elif temp[1] == "F":
    tempcelcius = ConvertTemperature(int(temp[0]))
    print(str(round(tempcelcius.convert_to_celsius(), 2)) + "°C")
else:
    print("Not in supported format.")