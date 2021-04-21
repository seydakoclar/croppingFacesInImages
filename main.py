import os
from PIL import Image
import face_recognition

# load the file from its path and find the locations of faces in that image
def getFaceLocationsInImage(imagePath):
    img = face_recognition.load_image_file(imagePath)
    faceLocations = face_recognition.face_locations(img)
    return faceLocations

# get the boundries of the area that will be cropped and the path of the image then return cropped image
def cropImage(cropBox, imagePath):
    image = Image.open(imagePath)
    croppedImage = image.crop(cropBox)
    return croppedImage

def main():
    # give the path of the folder containing input images (it can be full path of any other folder in your computer)
    inputImagesPath = "testImages"

    # give path of the folder that will contain the cropped faces of images (it can be full path of any other folder in your computer)
    outputImagesPath = "croppedTestImages"

    for inputImage in os.listdir(inputImagesPath):
        # imagePath contains name of the image
        imgPath = os.path.join(inputImagesPath, inputImage)

        # faceLocations found in the image
        faceLocations = getFaceLocationsInImage(imgPath)

        # for each location crop that in the image
        for i,faceLocation in enumerate(faceLocations):
            # get the details of face location
            top, right, bottom, left = faceLocation

            # convert it as a cropBox for PIL Image
            cropBox = (left, top, right, bottom)

            # crop the face and get image of cropped area
            croppedFace = cropImage(cropBox, imgPath)

            # generate the output path of the image
            # since there might be more than one faces in an image, we add i as prefix of the actual image name
            outputImagePath = os.path.join(outputImagesPath, str(i) + inputImage)

            # save image to the directory
            croppedFace.save(outputImagePath)

if __name__ == '__main__':
     main()
