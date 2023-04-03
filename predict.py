import requests
import json

def prediction(urls):
  params = {
    'url': f'{urls}',
    'models': 'nudity-2.0',
    'api_user': '86785559',
    'api_secret': 'dgDy9CifFDfgufJWhT8h'
  }
  r = requests.get('https://api.sightengine.com/1.0/check.json', params=params)

  output = dict(json.loads(r.text))['nudity']['erotica']
  outputs = f"Obscenity Confidence: {output}"
  return outputs