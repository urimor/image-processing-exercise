from PIL import Image
import numpy as np
import dicom

class Pixel:
    def __init__(self, p):
        self.r = p[0].astype(np.double)
        self.g = p[1].astype(np.double)
        self.b = p[2].astype(np.double)

    def __str__(self):
        return "red: " + str(self.r) + ", green: " + str(self.g) + ", blue: " + str(self.b)


def imageToArray(image):
    return np.array(image.getdata(), dtype=np.uint8).reshape(image.size[::-1] + (3,)).transpose([1, 0, 2])


def arrayToImage(array):
    if len(array.shape) == 3:
        return Image.fromarray(array.transpose([1, 0, 2]))
    else:
        return Image.fromarray(array.transpose(), mode="L")


def load_16bit(fileName):
    dicom_object = dicom.read_file(fileName)
    return dicom_object.pixel_array.transpose().astype(np.double)*dicom_object.RescaleSlope + dicom_object.RescaleIntercept
