import time
import random
# Simulating traffic data (number of vehicles waiting at each lane)
class TrafficLight:
    def __init__(self):
        self.green_time = 10  # Default green light duration in seconds
        self.red_time = 10  # Default red light duration in seconds

    def adjust_green_time(self, traffic_count):
        """
        Adjust the green light duration based on traffic count.
        The more vehicles waiting, the longer the green light.
        """
        if traffic_count > 50:
            self.green_time = 20  # Extend green light duration for heavy traffic
        elif traffic_count > 30:
            self.green_time = 15  # Moderate traffic
        else:
            self.green_time = 10  # Light traffic

    def run_cycle(self, lane_name, traffic_count):
        """
        Simulate a traffic light cycle.
        """
        print(f"\nTraffic Light for {lane_name}:")
        print(f"Vehicles waiting: {traffic_count}")
        self.adjust_green_time(traffic_count)

        print(f"Green light for {self.green_time} seconds.")
        time.sleep(self.green_time)

        print(f"Red light for {self.red_time} seconds.")
        time.sleep(self.red_time)
# Main function to simulate traffic flow optimization
def simulate_traffic_flow():
    lanes = ['North', 'East', 'South', 'West']  # 4 lanes for simplicity
    traffic_data = {lane: random.randint(0, 60) for lane in lanes}  # Simulate traffic count (0 to 60 cars)

    traffic_lights = {lane: TrafficLight() for lane in lanes}

    # Simulate a series of traffic light cycles
    for cycle in range(1, 6):  # Simulate 5 cycles
        print(f"\nCycle {cycle} of Traffic Flow Optimization")
        
        # Randomize vehicle counts (simulating real-time changes in traffic)
        for lane in lanes:
            traffic_data[lane] = random.randint(0, 60)
        
        # Run each lane's traffic light cycle
        for lane in lanes:
            traffic_lights[lane].run_cycle(lane, traffic_data[lane])
# Run the simulation
simulate_traffic_flow()

