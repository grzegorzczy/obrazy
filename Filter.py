from abc import ABCMeta, abstractmethod
import numpy as np

class Filter(metaclass=ABCMeta):
    def __init__(self, c=0):
        self.color = c
        self.points = set()

    def getPoints(self):
        return self.points

    @abstractmethod
    def modify(self, image):
        pass

class CircleFilter(Filter):
    def __init__(self, radiusI, radiusO=-1, outside=True, c=0):
        super().__init__(c)
        self.innerRadius = radiusI
        self.outerRadius = radiusO
        self.outside = outside

    def showMultImage(self, image):
        # Pokaż zmodyfikowany obraz w dziedzinie częstotliwości
        (height, width) = image.shape
        mult = np.ones((height, width)) if self.outside else np.zeros((height, width))
        
        if self.outerRadius != -1:
            self.fillCircle(mult, 0 if self.outside else 1, self.outerRadius, width, height)
            self.fillCircle(mult, 1 if self.outside else 0, self.innerRadius, width, height)
        else:
            self.fillCircle(mult, 0 if self.outside else 1, self.innerRadius, width, height)
        
        return mult

    def modify(self, image):
        return self.showMultImage(image) * image

    def fillCircle(self, arr, num, radius, width, height):
        center = (width // 2, height // 2)
        for i in range(height):
            for j in range(width):
                if (i - center[1]) ** 2 + (j - center[0]) ** 2 < radius ** 2:
                    arr[i, j] = num

class LineFilter(Filter):
    def __init__(self, width, height, c=0):
        super().__init__(c)
        self.width = width
        self.height = height
        self.mult = np.ones((height, width))

    def addLine(self, x1, y1, x2, y2, pixelWidth=1):
        steep = abs(y2 - y1) > abs(x2 - x1)
        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        
        dx = x2 - x1
        dy = abs(y2 - y1)
        error = dx / 2.0
        ystep = 1 if y1 < y2 else -1
        y = y1

        for x in range(x1, x2 + 1):
            coord = (y, x) if steep else (x, y)
            self.drawPixel(coord, pixelWidth)
            error -= dy
            if error < 0:
                y += ystep
                error += dx

    def drawPixel(self, coord, pixelWidth):
        x, y = coord
        for dx in range(-pixelWidth // 2, pixelWidth // 2 + 1):
            for dy in range(-pixelWidth // 2, pixelWidth // 2 + 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    self.mult[ny, nx] = 0

    def modify(self, image):
        return image * self.mult
