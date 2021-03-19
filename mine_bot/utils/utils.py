import requests

HTTP_GET = 'GET'
HTTP_POST = 'POST'

def forwards_api(**kwargs):  
  url = kwargs.get('url')
  method = kwargs.get('method', HTTP_GET)
  params_body = kwargs.get('params_body', '') # use it pass data when use method POST
  payload = kwargs.get('payload', '') # use it to pass data when use method GET

  response = {}

  if not url:
    response['message'] = 'no url'
    return

  if method == HTTP_GET:
    data = requests.get(url, params=payload)
    return data.json()

  response_api = requests.post(url, data=params_body)
  return response_api.json()
