import requests

headers = {'email': 'azinokina@gmail.com',
           'password': 'Test14062022/',
           'auth_key': 'e0214d998b76d4659a8dfbb8cf36c43c13d2112888776c2be5d42fbd',
           'accept': 'application/json'}

data = {'name': 'Хан',
        'animal_type': 'Собака',
        'age': 6}
new_data = {'name': 'Ушкин',
            'animal_type': 'Кролик',
            'age': 1}

res_post = requests.post(f'https://petfriends.skillfactory.ru/api/create_pet_simple', headers=headers, data=data)
print(res_post.status_code)
print(res_post.json())

res_get = requests.get(f'https://petfriends.skillfactory.ru/api/pets', params={'filter': 'my_pets'}, headers=headers)
print(res_get.status_code)
print(res_get.json())

res_put = requests.put(f'https://petfriends.skillfactory.ru/api/pets/968528b1-58dc-4383-9f3f-823a5b1354f7',
                       headers=headers, data=new_data)
print(res_put.status_code)
print(res_put.json())

res_del = requests.delete(f'https://petfriends.skillfactory.ru/api/pets/9faf3ec1-c52b-45ad-8023-e6e1ec1ee951',
                          headers=headers)
print(res_del.status_code)
print(res_del.text)
