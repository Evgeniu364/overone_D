class Planet:
    def __init__(self, name, size, distance, circles):
        self.__name = name
        self.__size = size
        self.__distance = distance
        self.__circles = circles

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        self.__distance = value

    @property
    def circles(self):
        return self.__circles

    @circles.setter
    def circles(self, value):
        if type(value) == bool:
            self.__circles = value

    def __str__(self):
        return f"{self.__name}, {self.__size}, {self.__distance}"

    def edit_size(self, value):
        self.size += value