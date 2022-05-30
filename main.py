import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('image.jpeg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'aXRVj6DNWEUDwfTBzG1nivx9'},
)

if response.status_code == requests.codes.ok:
    with open('edited_image.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error", response.status_code, response.text)









