class Planet:
    def __init__(self, name, size, distance, circles):
        self.__name = name
        self.__size = size
        self.__distance = distance
        self.__circles = circles

    def __str__(self):
        return f"{self.__name}, {self.__size}, {self.__distance}"

p1 = Planet("hscbshjdbk", 12344, 7627638277287, True)
print(p1)