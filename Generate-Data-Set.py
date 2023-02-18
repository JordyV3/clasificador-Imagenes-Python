import os
import cv2
import matplotlib.pyplot as plt

Data_dir = "/Users/jordyvega/PycharmProjects/Clasificador/PetImages"
Category = ["Diseased-plant", "Healthy-plant"]


def GenerateData():
    for category in Category:
        path = os.path.join(Data_dir, category)
        for image_name in os.listdir(path):
            image_path = os.path.join(path, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            plt.imshow(image, cmap="gray")
            plt.show()


GenerateData()
