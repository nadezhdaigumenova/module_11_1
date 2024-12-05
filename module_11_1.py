import numpy as np
import requests
from PIL import Image, ImageFilter, ImageDraw, ImageFont



# Работа с nampy№

array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Одномерный массив:", array_1d)
print("Двумерный массив:\n", array_2d)

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
result = array_a + array_b
print("Результат сложения:", result)

random_array = np.random.rand(5)
print("Случайный массив:", random_array)

std_deviation = np.std(random_array)
print("Стандартное отклонение:", std_deviation)

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])


matrix_product = np.dot(matrix_a, matrix_b)
print("Умножение матриц:\n", matrix_product)



#Работф с requests№

response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    print(response.json())
else:
    print(f'Ошибка:{response.status_code}')

url = 'https://jsonplaceholder.typicode.com/posts'
data = {'title': 'foo', 'body': 'bar','userId': 1}
response = requests.post(url, json=data)
if response.status_code == 201:
    print('Данные успешно отправлены:', response.json())
else:
    print(f"Ошибка: {response.status_code}")

try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    response.raiseforstatus()  # Это вызовет ошибку для статусов 4xx и 5xx
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(f"Ошибка HTTP: {err}")
except Exception as e:
    print(f"Ошибка: {e}")

#Работа с Pillow#

img = Image.open('img.jpg')
imgp_resized = img.resize((200, 200))

box = (100, 100, 400, 400)
img_cropped = img.crop(box)
img_cropped.show()

img_blurred = img.filter(ImageFilter.BLUR)
img_blurred.show()

imgp_resized.save('resizedimage.jpg')
print('Изображение успешно сохранено')

draw = ImageDraw.Draw(img)
font = ImageFont.load_default(100)
draw.text((10, 10), "Hello world!", fill="black", font=font)
img.show()












