
import imageio

fileNameIn = "paris.jpg"
fileNameOut = "paris_cropped.jpg"
imgIn = imageio.imread(fileNameIn)

yBegin = 1100
yStop = 1700

imgOut = imgIn[yBegin:yStop, :,:]

imageio.imwrite(fileNameOut,imgOut)