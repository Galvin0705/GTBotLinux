import os
from os import system
import requests

os.system('clear')
target = input('Target :  ')

post = requests.post(f'http://{target}/growtopia/server_data.php')
print(post.text)