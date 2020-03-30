from random import choice


class Elevator:
    def __init__(self):
        self.__left_elevator = [0,1,2]
        self.__right_elevator = [0,1,2]
        self.__call_elevator = [0,1,2]

    def get_random_left_elevator_floor(self) -> int:
        left_elevator = self.__left_elevator
        return choice(left_elevator)

    def get_random_right_elevator_floor(self) -> int:
        right_elevator = self.__right_elevator
        return choice(right_elevator)

    def get_random_elevator_call(self) -> int:
        call_elevator = self.__call_elevator
        return choice(call_elevator)

