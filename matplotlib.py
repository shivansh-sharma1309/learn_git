import requests  

response = requests.get(url = "https://leetcode.com/problemset/all/")

data = response.json()

response.iter_lines()