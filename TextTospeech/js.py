import os
import json

f = open('synthesize-text.json','r')

data=json.load(f)

print(data['audioContent'])


