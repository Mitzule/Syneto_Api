import requests
import json

query = '500g chicken breast with sourcream'
api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
response = requests.get(api_url, headers={'X-Api-Key': 'zduTvlSzuNrRqhEztMZXoA==uULzTTKSkNIZEapU'})

if response.status_code == requests.codes.ok:
    data = response.json()
    formatted_response = json.dumps(data, indent=4)

    print(formatted_response)
    
    total_calories = 0

    for item in data:
        calories = item["calories"]
        total_calories += calories

    print("Total Calories:", total_calories)
else:
    print("Error:", response.status_code, response.text)
