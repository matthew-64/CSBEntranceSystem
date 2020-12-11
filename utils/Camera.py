import cv2


def take_picture():
    camera = cv2.VideoCapture(0)
    for i in range(2):
        return_value, image = camera.read()
        cv2.imwrite('inputData/test_img.jpg', image)
    del (camera)
