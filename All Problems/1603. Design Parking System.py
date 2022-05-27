class ParkingSystem(object):
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.big -= 1
            if self.big >= 0:
                return True
            else:
                return False
        elif carType == 2:
            self.medium -= 1
            if self.medium >= 0:
                return True
            else:
                return False
        elif carType == 3:
            self.small -= 1
            if self.small >= 0:
                return True
            else:
                return False


class FasterParkingSystem(object):
    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType - 1] >= 1:
            self.spaces[carType - 1] -= 1
            return True
        else:
            return False


if __name__ == '__main__':
    park_size = [1, 1, 0]
    cars = [1, 2, 3, 1]
    run = FasterParkingSystem(park_size[0], park_size[1], park_size[2])

    for car in cars:
        print(run.addCar(car))


