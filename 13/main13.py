import requests
import xmlrpc.client



req_php = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print(req_php)
print(req_php.system.listMethods())

print(req_php.system.methodHelp('phone'))

print(req_php.phone('evil'))
print(req_php.phone('He'))
print(req_php.phone('call'))
print(req_php.phone('him'))

print(req_php.phone('Bert'))

