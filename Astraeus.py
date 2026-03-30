import random
import time

 class SpaceStationAI:
 def __init__(self, astronauts, activity_level):  
    self.astronauts = astronauts  
    self.activity_level = activity_level.lower()  

    # Initial values (will change dynamically)  
    self.oxygen = random.uniform(80, 120)  
    self.water = random.uniform(80, 120)  
    self.co2 = random.uniform(1, 4)  

    #  Dynamic consumption  
    if self.activity_level == "low":  
        self.oxygen_rate = 1.5  
        self.water_rate = 0.8  
    elif self.activity_level == "medium":  
        self.oxygen_rate = 2  
        self.water_rate = 1  
    else:  
        self.oxygen_rate = 3  
        self.water_rate = 1.5  

# 🎲 Simulate sensors updating  
def update_sensors(self):  
    self.oxygen -= random.uniform(0.5, 2)  
    self.water -= random.uniform(0.3, 1)  
    self.co2 += random.uniform(0.1, 0.5)  

def calculate_time_left(self):  
    total_oxygen_usage = self.oxygen_rate * self.astronauts  
    total_water_usage = self.water_rate * self.astronauts  

    oxygen_time = self.oxygen / total_oxygen_usage  
    water_time = self.water / total_water_usage  

    return oxygen_time, water_time  

def predict_future_risk(self, oxygen_time):  
    if oxygen_time < 5:  
        return " Oxygen CRITICAL!"  
    elif oxygen_time < 10:  
        return "Oxygen getting low"  
    else:  
        return "Oxygen stable"  

def check_status(self, oxygen_time, water_time):  
    status = []  

    if oxygen_time < 5:  
        status.append("Oxygen extremely low!")  
    elif oxygen_time < 10:  
        status.append("Oxygen decreasing")  

    if water_time < 8:  
        status.append("Water low")  

    if self.co2 > 5:  
        status.append("High CO₂!")  

    if not status:  
        status.append("All systems normal")  

    return status

 MAIN LOOP (REAL-TIME SIMULATION)

print(" AI Space Station LIVE Monitoring")

astronauts = int(input("Enter number of astronauts: "))
activity = input("Enter activity level (low / medium / high): ")

ai = SpaceStationAI(astronauts, activity)

while True:
ai.update_sensors()  # 🔄 simulate sensors

oxygen_time, water_time = ai.calculate_time_left()  

print("\n==============================")  
print(f" Oxygen: {ai.oxygen:.2f}")  
print(f" Water: {ai.water:.2f}")  
print(f" CO₂: {ai.co2:.2f}%")  

print(f"Oxygen left: {oxygen_time:.2f} hrs")  
print(f" Water left: {water_time:.2f} hrs")  

print(" Status:")  
for s in ai.check_status(oxygen_time, water_time):  
    print("-", s)  

print(" Risk:", ai.predict_future_risk(oxygen_time))  

time.sleep(2)  # ⏱️ update every 2 seconds
