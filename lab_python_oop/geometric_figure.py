from abc import abstractmethod, ABC


class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        pass
