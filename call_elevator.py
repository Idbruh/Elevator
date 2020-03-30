from Elevator import Elevator


class RunElevator:
    def __init__(self):
        self.elevator = Elevator()
        self.left_floor = self.elevator.get_random_left_elevator_floor()
        self.right_floor = self.elevator.get_random_right_elevator_floor()
        self.call_floor = self.elevator.get_random_elevator_call()

    def run_elevator(self):
        if (self.right_floor - self.call_floor) * (-1) < (self.left_floor - self.call_floor) * (-1):
            print(f"You're on {self.call_floor} floor, please wait for the right elevator that will come from floor"
                  f" {self.right_floor} that is as far from the left elevator that is on {self.left_floor}")
        elif (self.right_floor - self.call_floor) * (-1) == (self.left_floor - self.call_floor) * (-1):
            print(f"You're on {self.call_floor} floor, please wait for the right elevator that will come from floor"
                  f" {self.right_floor} that is as far from the left elevator that is on {self.left_floor} floor.")
        else:
            print(f"You're on {self.call_floor} floor, please wait for the left elevator on floor {self.left_floor}"
                  f" that is as far from the left elevator that is on {self.right_floor} floor")


e = RunElevator()
e.run_elevator()
