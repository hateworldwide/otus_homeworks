from abc import ABC, abstractmethod

class Figure:

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Should be a Figure")
        a = self.get_area
        b = other_figure.get_area
        return a + b