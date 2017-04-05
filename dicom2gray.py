import image_tranform
import utils

windowing_min = -160
windowing_max = 240

# Load image as array

dicomArray = utils.load_16bit("CTImage.dcm")

# Perform windowing

outputArray = image_tranform.windowing_16bit(dicomArray, windowing_min, windowing_max)

# Save to file

outputImage = utils.arrayToImage(outputArray)
outputImage.save("dicom2gray_windowing_" + str(windowing_min) + "_" + str(windowing_max) + ".jpg", "JPEG")
