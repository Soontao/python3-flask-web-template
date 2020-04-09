
from flask import Flask
from .common import common_api

def mount_routes(app: Flask):
  """
  mount routes to flask instance
  """
  app.register_blueprint(common_api, url_prefix="/") 
  return app
