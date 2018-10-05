#!/bin/bash

filename="$1.txt"
value=$(<$filename)

curl -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
  -H "Content-Type: application/json; charset=utf-8" \
  --data "{
    'input':{
      'text':'$value'
    },
    'voice':{
      'languageCode':'en-US',
      'name':'en-US-Wavenet-C',
      'ssmlGender':'FEMALE'
    },
    'audioConfig':{
      'audioEncoding':'MP3'
    }
  }" "https://texttospeech.googleapis.com/v1/text:synthesize" > synthesize-text.json


python3 js.py > synthesize-output-base64.txt

outfile="$1.mp3"
base64 synthesize-output-base64.txt --decode > $outfile



