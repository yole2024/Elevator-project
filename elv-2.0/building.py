from floor import *
from elevator import *


class Building:
    def __init__(self, num_of_floors, num_of_elevators):
        self.floors = [Floor(i) for i in range(num_of_floors)]
        self.elevators = [Elevator(i) for i in range(num_of_elevators)]

    def ide(self, x, y):# click is a touple of x,y coordinate
        for floor in self.floors:
            idx = floor.is_clicked(x, y)
            if idx is not None:
                return self.allocate_elevator(idx)






    def allocate_elevator(self, request_floor: int):
        best_elevator = None
        minimum_time = float('inf')
        for elevator in self.elevators:
            time_to_free = elevator.calculate_times_for_all()
            travel_time = elevator.calculate_time(request_floor)
            total_time = time_to_free + travel_time

            if total_time < minimum_time:
                minimum_time = total_time
                best_elevator = elevator

        best_elevator.append(request_floor, minimum_time)  
        self.floors[request_floor].countdown_timer(minimum_time - STOP_TIME)




    def update(self):
        pass

    def draw(self, screen, FLOOR_SPACER_HEIGHT):
        for floor in self.floors:
            floor.draw(screen, FLOOR_SPACER_HEIGHT)
        for elevator in self.elevators:
            elevator.draw(screen)
        
        

    