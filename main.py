from ImageHandler import *
from Filter import *
from scipy import fftpack
from scipy import signal
import numpy as np
from PIL import Image



if __name__ == '__main__':
    print("Wybierz funkcję (wpisz numer funkcji od 0 do 15):")
    print("0: Wyświetl obraz 'vertsine.gif'")
    print("1: Wyświetl obraz 'sin4h.gif'")
    print("2: Wyświetl obraz 'diagonalsine.jpg'")
    print("3: Wyświetl obraz 's2.jpg'")
    print("4: Wyświetl obraz 's3.jpg'")
    print("5: Wyświetl obraz 's4.png'")
    print("6: Wyświetl obraz 'flowers8.jpg'")
    print("7: Wyświetl obraz 'lines2.gif'")
    print("8: Wyświetl obraz 'flowersHD.jpg' po zastosowaniu filtra kołowego")
    print("9: Wyświetl obraz 'flowersHD.jpg' po zastosowaniu dużego filtra kołowego")
    print("10: Wyświetl obraz 'flowersHD.jpg' po zastosowaniu filtra kołowego (zmodyfikowany promień)")
    print("11: Wyświetl obraz 'flowersHD.jpg' po zastosowaniu filtra kołowego (odwrotny promień)")
    print("12: Wyświetl obraz 'flowersHD.jpg' po zastosowaniu filtru Cannyego")
    print("13: Wyświetl obraz 'flowersHD.jpg' po zastosowaniu filtru Scharff")
    print("14: Wyświetl obraz 'flowersHD.jpg' po zastosowaniu filtru Prewitt")
    print("15: Wyświetl obraz 'flowersHD.jpg' po zastosowaniu filtru Sobel")

    runCode = int(input("Numer funkcji: "))

    if(runCode == 0):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\vertsine.gif")
        im.image.show()
        im.showFourier()
        
    elif(runCode == 1):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\sin4h.gif")
        im.image.show()
        im.showFourier()

    elif(runCode == 2):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\diagonalsine.jpg")
        im.image.show()
        im.showFourier()

    elif(runCode == 3):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\s2.jpg")
        im.image.show()
        im.showFourier()
    elif(runCode == 4):

        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\s3.jpg")
        im.image.show()
        im.showFourier()

    elif(runCode == 5):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\s4.png")
        im.image.show()
        im.showFourier()

    elif(runCode == 6):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowers8.jpg")
        im.image.show()
        im.showFourier()

    elif(runCode == 7):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\lines2.gif")
        im.image.show()
        im.showFourier()

    elif(runCode == 8):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(50, outside=False)
        im.applyFilter(cf)
        im.showFourier()
        im.image.show()

    elif(runCode == 9):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(50, outside=True)
        im.applyFilter(cf)
        im.showFourier()
        im.image.show()

    elif(runCode == 10):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        cf = CircleFilter(50, 150, outside=False)
        im.applyFilter(cf)
        im.showFourier()
        im.image.show()

    elif(runCode == 11):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(50, 200, outside=False)
        im.applyFilter(cf)
        im.showFourier()
        
    elif(runCode == 12):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(100, 300, outside=False)
        im.applyFilter(cf)
        im.showFourier()
        canny_filter = CannyFilter(100, 200)  # Progi dla filtra Canny
        canny_image = canny_filter.modify(np.array(im.image.convert('L')))  # Konwersja do skali szarości przed Canny
        im.image = Image.fromarray(canny_image)
        im.image.show()
        
    elif(runCode == 13):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(100, 300, outside=False)
        im.applyFilter(cf)
        im.showFourier()
        scharr_filter = ScharrFilter()
        scharr_image = scharr_filter.modify(np.array(im.image))
        im.image = Image.fromarray(scharr_image.astype(np.uint8))
        im.image.show()
        
    elif(runCode == 14):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(100, 500, outside=False)
        im.applyFilter(cf)
        im.showFourier()
        prewitt_filter = PrewittFilter()
        prewitt_image = prewitt_filter.modify(np.array(im.image))
        im.image = Image.fromarray(prewitt_image.astype(np.uint8))
        im.image.show()
        
    elif(runCode == 15):
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(50, 100, outside=False)
        im.applyFilter(cf)
        im.showFourier()
        sobel_filter = SobelFilter()
        sobel_image = sobel_filter.modify(np.array(im.image))
        im.image = Image.fromarray(sobel_image.astype(np.uint8))
        im.image.show()
        
