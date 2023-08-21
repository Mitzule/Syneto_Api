# import requests
# import json

# url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
# response = requests.get(url, params = {"s": "margarita"})

# json_object =response.json()
# json_formatted_str = json.dumps(json_object, indent=2)
# print(json_formatted_str)

# image = json_object["drinks"][0]["strDrinkThumb"]
# print(image)

# save_image = requests.get(image)
# with open("margarita.jpg", "wb") as file:
#     file.write(save_image.content)


 

    