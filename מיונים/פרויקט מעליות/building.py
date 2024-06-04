from elevator import elevator
from setings import *
from floor import floor

class building:
    def __init__(self):
        self.floors = []
        k = HEIGHT - 100
        for i in range(NUM_FLOORS):
            self.floors.append(floor(0, k))
            k -= 60
        self.elevators = []
        z = HEIGHT -100
        for i in range(NOM_ELEVATORS):
            self.elevators.append(elevator(6,z))
            z -= 60

    def select_best_elevator(elevators, request_floor):
        best_elevator = None
        minimum_time = float('inf')
        for elevator in elevators:
            time_to_free = elevator.calculate_times_for_all()
            travel_time = elevator.calculate_time(request_floor)
            total_time = time_to_free + travel_time

            if total_time < minimum_time:
                minimum_time = total_time
                best_elevator = elevator
        best_elevator.append(request_floor)   
        request_floor.countdown_timer(minimum_time)
    
    def drow(self, screen):
        for i in self.floors:
            i.draw_floor(screen)

    
    
    