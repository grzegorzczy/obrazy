from abc import ABCMeta, abstractmethod
import numpy as np
import cv2

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

class CannyFilter:
    def __init__(self, threshold1, threshold2):
        self.threshold1 = threshold1
        self.threshold2 = threshold2

    def modify(self, image):
        edges = cv2.Canny(image, self.threshold1, self.threshold2)
        return edges


class ScharrFilter(Filter):
    def modify(self, image):
        gx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
        gy = cv2.Scharr(image, cv2.CV_64F, 0, 1)
        g = np.hypot(gx, gy)
        return np.abs(g)

    
class PrewittFilter(Filter):
    def modify(self, image):
        kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
        kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        gx = cv2.filter2D(image, -1, kernelx)
        gy = cv2.filter2D(image, -1, kernely)
        g = np.hypot(gx, gy)
        return np.abs(g)

class SobelFilter(Filter):
    def modify(self, image):
        sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
        sobel = np.sqrt(sobelx**2 + sobely**2)
        sobel = np.uint8(sobel / np.max(sobel) * 255)
        return sobel
    
