import requests
import json


def classify(image):
    with open("config.json") as config, open(image, mode="rb") as test_data:
        customvision_data = json.load(config)["customvision"]
        endpoint = customvision_data["endpoint"]
        prediction_key = customvision_data["prediction_key"]
        content_type = customvision_data["content_type"]

        r = requests.post(endpoint, headers={"Prediction-Key": prediction_key, "Content-Type": content_type},
                          data=test_data)
        print(r.status_code)
        print(r.text)


classify("inputData/test_img.jpg")
