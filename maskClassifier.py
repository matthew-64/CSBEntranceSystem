import requests
import json
import CustomEnum

CONFIDENCE_THRESHOLD = 0.5;

def classify(image):
    with open("config.json") as config, open(image, mode="rb") as test_data:
        customvision_data = json.load(config)["customvision"]
        endpoint = customvision_data["endpoint"]
        prediction_key = customvision_data["prediction_key"]
        content_type = customvision_data["content_type"]

        r = requests.post(endpoint, headers={"Prediction-Key": prediction_key, "Content-Type": content_type}, data=test_data)
        #print(r.status_code)
        #print(r.text)

        json_response_predictions = json.loads(r.text)["predictions"]

        mask_probability = 0.0;
        nomask_probability = 0.0;
        for prediction in json_response_predictions:
            if prediction["tagName"] == "mask":
                mask_probability = float(prediction["probability"])
            elif prediction["tagName"] == "nomask":
                nomask_probability = float(prediction["probability"])

        #print(mask_probability)
        #print(nomask_probability)

        if mask_probability < CONFIDENCE_THRESHOLD and nomask_probability < CONFIDENCE_THRESHOLD:
            return CustomEnum.MaskEnum.UNKNOWN
        if mask_probability > nomask_probability:
            return CustomEnum.MaskEnum.MASK
        else:
            return CustomEnum.MaskEnum.MASK

classify("inputData/test_img.jpg")
