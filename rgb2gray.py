from PIL import Image
import utils
import image_tranform


# Load image and convert to 3d array
rgbImage = Image.open('image.jpg')
rgbArray = utils.imageToArray(rgbImage)

# Average method : Transform array, convert to image and save to file
outputArray = image_tranform.rgb2gray_average(rgbArray)
outputImage = utils.arrayToImage(outputArray)
outputImage.save("rgb2gray_average.jpg", "JPEG")

# Lightness method : Transform array, convert to image and save to file
outputArray = image_tranform.rgb2gray_lightness(rgbArray)
outputImage = utils.arrayToImage(outputArray)
outputImage.save("rgb2gray_lightness.jpg", "JPEG")

# Luminosity method : Transform array, convert to image and save to file
outputArray = image_tranform.rgb2gray_luminosity(rgbArray)
outputImage = utils.arrayToImage(outputArray)
outputImage.save("rgb2gray_luminosity.jpg", "JPEG")

# Custom method : Transform array, convert to image and save to file
outputArray = image_tranform.rgb2gray_custom(rgbArray)
outputImage = utils.arrayToImage(outputArray)
outputImage.save("rgb2gray_custom.jpg", "JPEG")
