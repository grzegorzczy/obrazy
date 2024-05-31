from PIL import Image
import numpy as np
from scipy import fftpack
from scipy import signal
import pylab as py

class ImageHandler:

    def __init__(self, fName=None, extend=False):
        if fName:
            self.orig = Image.open(fName).convert('L')
            self.image = Image.open(fName).convert('L')
            self.extend = extend
            self.four = self.dft()
            self.idft_image = None

    def loadImage(self, image, extend=False):
        self.image = image
        self.four = self.dft()

    def dft(self):
        # Wykonaj DFT i przesuń zerowe częstotliwości do środka spektrum
        F1 = fftpack.fft2(np.array(self.image))
        F2 = fftpack.fftshift(F1)
        return F2

    def idft(self):
        # Wykonaj IDFT na zmodyfikowanym obrazie w dziedzinie częstotliwości
        if self.four is not None:
            ifft_shift = fftpack.ifftshift(self.four)
            self.idft_image = Image.fromarray(np.abs(fftpack.ifft2(ifft_shift)).astype(np.uint8))

    def showFourier(self):
        # Pokaż spektrum mocy
        psd2D = np.log(np.abs(self.four)**2 + 1)
        (height, width) = psd2D.shape
        py.figure(figsize=(10, 10*height/width), facecolor='white')
        py.clf()
        py.rc('text', usetex=True)
        py.xlabel(r'$\omega_1$', fontsize=24)
        py.ylabel(r'$\omega_2$', fontsize=24)
        py.xticks(fontsize=16)
        py.yticks(fontsize=16)
        py.imshow(psd2D, cmap='Greys_r', extent=[-np.pi, np.pi, -np.pi, np.pi], aspect='auto')
        py.show()

    def showPhase(self):
        # Pokaż fazę spektrum
        phase2D = np.angle(self.four)
        (height, width) = phase2D.shape
        py.figure(figsize=(10, 10*height/width), facecolor='white')
        py.clf()
        py.rc('text', usetex=True)
        py.xlabel(r'$\omega_1$', fontsize=24)
        py.ylabel(r'$\omega_2$', fontsize=24)
        py.xticks(fontsize=16)
        py.yticks(fontsize=16)
        py.imshow(phase2D, cmap='Greys_r', extent=[-np.pi, np.pi, -np.pi, np.pi], aspect='auto')
        py.show()

    def showImage(self):
        # Pokaż obraz
        self.image.show()

    def showDFTImage(self):
        # Pokaż obraz po DFT
        if self.four is not None:
            dft_image = np.log(np.abs(self.four) + 1)
            dft_image = (dft_image - dft_image.min()) * (255 / (dft_image.max() - dft_image.min()))
            Image.fromarray(dft_image.astype(np.uint8)).show()

    def showIDFTImage(self):
        # Pokaż obraz po IDFT
        if self.idft_image is not None:
            self.idft_image.show()

    def applyFilter(self, fil):
        # Zastosuj filtr i wykonaj IDFT na zmodyfikowanym obrazie
        self.four = fil.modify(self.four)
        self.idft()

    def convolve(self, kernel):
        # Wykonaj konwolucję obrazu z danym jądrem
        matrix = np.array(self.image)
        convolved_matrix = signal.convolve2d(matrix, kernel, boundary='wrap', mode='same')
        self.image = Image.fromarray(np.clip(convolved_matrix, 0, 255).astype(np.uint8))

    def dft_idft_blocks(self, block_size):
        image_array = np.array(self.image)
        height, width = image_array.shape
        dft_blocks = []
        idft_blocks = np.zeros_like(image_array)

        # Podziel obraz na bloki i wykonaj DFT na każdym bloku
        for i in range(0, height, block_size):
            for j in range(0, width, block_size):
                block = image_array[i:i+block_size, j:j+block_size]
                dft_block = fftpack.fftshift(fftpack.fft2(block))
                dft_blocks.append(dft_block)
                
                # Wykonaj IDFT na każdym bloku
                idft_block = fftpack.ifft2(fftpack.ifftshift(dft_block))
                idft_blocks[i:i+block_size, j:j+block_size] = np.abs(idft_block)

        # Normalizacja IDFT bloku do zakresu [0, 255]
        idft_blocks = np.clip(idft_blocks, 0, 255).astype(np.uint8)
        self.idft_image = Image.fromarray(idft_blocks)

    def showDFTBlocks(self):
        # Pokaż obrazy DFT bloków
        image_array = np.array(self.image)
        height, width = image_array.shape
        block_size = int(min(height, width) / 10)  # Wybierz rozmiar bloku jako 1/10 najmniejszego wymiaru
        for i in range(0, height, block_size):
            for j in range(0, width, block_size):
                block = image_array[i:i+block_size, j:j+block_size]
                dft_block = fftpack.fftshift(fftpack.fft2(block))
                dft_image = np.log(np.abs(dft_block) + 1)
                dft_image = (dft_image - dft_image.min()) * (255 / (dft_image.max() - dft_image.min()))
                Image.fromarray(dft_image.astype(np.uint8)).show()
