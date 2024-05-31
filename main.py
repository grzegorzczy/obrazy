from ImageHandler import *
from Filter import *
import numpy as np

def padKernel(width, length, kernel):
    xL = length - len(kernel)
    xW = width - len(kernel[0])
    wPadLeft = xW // 2
    wPadRight = xW - wPadLeft
    lPadUp = xL // 2
    lPadDown = xL - lPadUp
    npad = ((lPadUp, lPadDown), (wPadLeft, wPadRight))
    newkernel = np.pad(kernel, pad_width=npad, mode='constant', constant_values=0)
    return newkernel

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
    print("12: Wyświetl obraz 'flowersgray.jpg' po zastosowaniu filtru liniowego")
    print("13: Wyświetl obraz 'flowersHD.jpg' po zastosowaniu dwóch filtrów kołowych")
    print("14: Wyświetl obraz 'flowers.jpg' po wykonaniu konwolucji")
    print("15: Wyświetl obraz 'flowersgray.jpg' po podzieleniu na bloki i zastosowaniu DFT oraz IDFT")

    runCode = int(input())

    if runCode == 0:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\vertsine.gif")
        im.image.show()
        im.showFourier()
        im.showPhase()
    elif runCode == 1:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\sin4h.gif")
        im.image.show()
        im.showFourier()
        im.showPhase()
    elif runCode == 2:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\diagonalsine.jpg")
        im.image.show()
        im.showFourier()
        im.showPhase()
    elif runCode == 3:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\s2.jpg")
        im.image.show()
        im.showFourier()
        im.showPhase()
    elif runCode == 4:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\s3.jpg")
        im.image.show()
        im.showFourier()
        im.showPhase()
    elif runCode == 5:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\s4.png")
        im.image.show()
        im.showFourier()
        im.showPhase()
    elif runCode == 6:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowers8.jpg")
        im.image.show()
        im.showFourier()
        im.showPhase()
    elif runCode == 7:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\lines2.gif")
        im.image.show()
        im.showFourier()
        im.showPhase()
    elif runCode == 8:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(20, outside=False)
        im.applyFilter(cf)
        im.showFourier()
        im.showPhase()
        im.showIDFTImage()
    elif runCode == 9:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(100, outside=True) # krawedzie
        im.applyFilter(cf)
        im.showFourier()
        im.showIDFTImage()
    elif runCode == 10:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(50,100, outside=False) # jak false to filtr dziala wewnatrz okreslonego pola pikselami, a zewnatrz odrzuca
        im.applyFilter(cf)
        im.showFourier()
        im.showPhase()
        im.showIDFTImage()
    elif runCode == 11:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(80,200, outside=True) # jak true to filtr dziala na zewnatrz okreslonego pola pikselami, a wewnatrz odrzuca
        im.applyFilter(cf)
        im.showFourier()
        im.showPhase()
        im.showIDFTImage()

    elif runCode == 12:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im.image.show()            # Wyświetl oryginalny obraz przed przetworzeniem
        im.showFourier()   
        im.showPhase()        # Wyświetl widmo Fouriera oryginalnego obrazu
        (height, width) = im.four.shape
        l = LineFilter(width, height)
        for i in range(83):
            if i != 41:
                l.addLine(int(round(23.41*i)) - 1, 0, int(round(23.41*i)) - 1, 1200, 3)
        for i in range(83):
            if i != 41:
                l.addLine(0, int(round(14.65 * i)) - 1, 1920, int(round(14.65 * i)) - 1, 3)
        im.applyFilter(l)          # Zastosuj filtr liniowy
        im.showFourier()           # Wyświetl widmo Fouriera po zastosowaniu filtru liniowego
        im.image.show()            # Wyświetl przetworzony obraz po zastosowaniu filtru liniowego

    elif runCode == 13:
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        cf = CircleFilter(80, outside=False)
        bigH = cf.showMultImage(im.four)
        im2 = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowersHD.jpg")
        im2.image = Image.fromarray(np.multiply(bigH, 255))
        im2.four = im2.fourier()
        im2.image.show()
        im2.showFourier()
        im2.showFourier()
        im.showPhase()
        im2.inverseFourier()
        im2.image.show()
        print(np.max(im2.image))

    elif runCode == 14:
        kernel = [[0, 0, 1.0/13, 0, 0], [0, 1.0/13, 1.0/13, 1.0/13, 0], [1.0/13, 1.0/13, 1.0/13, 1.0/13, 1.0/13], [0, 1.0/13, 1.0/13, 1.0/13, 0], [0, 0, 1.0/13, 0, 0]]
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowers.jpg")
        im.showImage()
        im.convolve(kernel)
        im.showImage()
        im.showFourier()
        im.showPhase()

        im2 = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\pics\\flowers.jpg")
        (height, width) = im2.four.shape
        kernelih = ImageHandler()
        kernelih.loadImage(Image.fromarray(padKernel(width, height, kernel)))
        kernelih.showImage()
        kernelih.showFourier()

        im2.showFourier()
        final = ImageHandler()
        Image.fromarray(signal.fftconvolve(im2.image, kernel)).show()

        final.loadImage(Image.fromarray(np.array([[0]])))
        final.four = np.multiply(np.fliplr(np.flipud(kernelih.four)), im2.four)
        final.four = np.multiply(kernelih.four, im2.four)
        final.inverseFourier()
        final.showFourier()
        final.showImage()
    
    elif runCode == 15:
        # Wybierz rozmiar bloku
        block_size = 8

        # Wczytaj obraz
        im = ImageHandler("C:\\Users\\Grzesiek\\Desktop\\ISA\\Identyfikacja_i_modelowanie_statystyczne-lab\\pics\\flowers.jpg")
        im.showImage()

        # Konwertuj obraz na macierz numpy
        image_array = np.array(im.image)

        # Uzyskaj wymiary obrazu
        height, width = image_array.shape

        # Utwórz pusty obraz dla obrazu wyjściowego po IDFT
        output_image = np.zeros((height, width), dtype=np.uint8)

        # Iteruj po blokach w obrazie
        for i in range(0, height, block_size):
            for j in range(0, width, block_size):
                # Wybierz aktualny blok
                block = image_array[i:i+block_size, j:j+block_size]

                # Wykonaj DFT na bloku
                block_dft = fftpack.fft2(block)

                # Wykonaj IDFT na bloku
                block_idft = np.abs(fftpack.ifft2(block_dft)).astype(np.uint8)

                # Zapisz wynikowy blok do obrazu wyjściowego
                output_image[i:i+block_size, j:j+block_size] = block_idft

        # Wyświetl obraz wyjściowy po IDFT
        output_image = Image.fromarray(output_image)
        output_image.show()
