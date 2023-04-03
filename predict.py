import requests
import json

def prediction(urls):
  params = {
    'url': f'{urls}',
    'models': 'nudity-2.0',
    'api_user': '433509463',
    'api_secret': 'KTyVa9kMbBSYuLvGPNoD'
  }
  try:
    r = requests.get('https://api.sightengine.com/1.0/check.json', params=params)
    print(r.text)
    output = dict(json.loads(r.text))['nudity']['erotica']
    return output
  except Exception as e:
    return -1
  outputs = f"Obscenity Confidence: {output}"
  return outputs