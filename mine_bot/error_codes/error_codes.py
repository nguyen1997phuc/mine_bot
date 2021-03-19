from enum import Enum

class ErrorCodes(Enum):
  issue_on_server_side = 400
  web_app_firewall = 429
  banned = 418