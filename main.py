import uvicorn
from fastapi import FastAPI
from env.settings import secret_key, api_key

app = FastAPI()

@app.get('/')
def index():
  return {'message': 'okay'}


def run():
  uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)
