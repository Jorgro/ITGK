import json

with open('input-hashchain.json', 'r') as file:
    data = json.loads(file.read())

from hashlib import md5
initial = md5('julekalender'.encode('utf8')).hexdigest()

answer = ''

while len(answer) < len(data):

    for list in data:
        if md5((initial + list.get('ch')).encode('utf8')).hexdigest() == list.get('hash'):
            answer += list.get('ch')
            initial = md5((initial + list.get('ch')).encode('utf8')).hexdigest()
print(answer)
