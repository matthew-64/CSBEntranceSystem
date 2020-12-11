import requests
import json

CONFIDENCE_THRESHOLD = 0.5;

def is_wearing_mask():
    with open("config.json") as config, open("inputData/test_img.jpg", mode="rb") as test_data:
        customvision_data = json.load(config)["customvision"]
        endpoint = customvision_data["endpoint"]
        prediction_key = customvision_data["prediction_key"]
        content_type = customvision_data["content_type"]

        r = requests.post(endpoint, headers={"Prediction-Key": prediction_key, "Content-Type": content_type}, data=test_data)

        json_response_predictions = json.loads(r.text)["predictions"]

        mask_probability = 0.0
        nomask_probability = 0.0
        for prediction in json_response_predictions:
            if prediction["tagName"] == "mask":
                mask_probability = float(prediction["probability"])
            elif prediction["tagName"] == "nomask":
                nomask_probability = float(prediction["probability"])

        return mask_probability > nomask_probability

