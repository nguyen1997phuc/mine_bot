from endpoints.endpoints import EndPointApi
from utils.utils import forwards_api


response = forwards_api(
  url=f'{EndPointApi.v3.value}/api/v3/ping',
  method='GET',
  params_body=None,
  payload=None,
)

print(response)

