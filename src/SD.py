import requests
import json
import base64
from dependencies import WISMODEL_API

api_key = WISMODEL_API

url = "https://api.wizmodel.com/sdapi/v1/txt2img"


def generate_img(text_prompt: str):
    payload = json.dumps({
        "prompt": text_prompt,
        "num_images": 1,
        "steps": 100
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        response_data = response.json()

        images_list = response_data.get('images', [])  # Extract the "images" value from the JSON response

        if images_list:

            base64_image = images_list[0]  # Get the first element from the list (assuming there's only one element)

            image_data = base64.b64decode(base64_image)  # Decode the image from base64 format

            return image_data


        else:
            print("Изображение не найдено в ответе.")
    else:
        print("Ошибка при выполнении POST-запроса. Код состояния:", response.status_code)


if __name__ == '__main__':
    generate_img('a black sheep with white god ray and black background')
