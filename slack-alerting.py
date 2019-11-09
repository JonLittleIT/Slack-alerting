import httplib, json
import getopt, sys, os
import subprocess


def main():
 
  headers = {'Content-Type': 'application/json'}
  WEBHOOK_URL = os.environ['WEBHOOK_URL']
  ICON_URL = os.environ['ICON_URL']
  
  color = 'good'
  message = {
    'username': 'GD Alert',
    'color': color,
    'ICON_URL': ICON_URL,
    'fields': [
      {
        'title': "guard duty alert",
        'short': True
      }
    ]
  }

  connection = httplib.HTTPSConnection('hooks.slack.com')
  connection.request('POST', WEBHOOK_URL, json.dumps(message), headers)
  print json.dumps(message)
  response = connection.getresponse()
  print response.read().decode()

if __name__ == '__main__':
  main()
