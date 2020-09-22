import requests

req_php = requests.get("http://www.pythonchallenge.com/pc/phonebook.php")

print(req_php.text)