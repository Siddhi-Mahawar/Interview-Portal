import requests
import os

def compileAndRun(code, lang, input):

    RUN_URL = u'https://api.hackerearth.com/v3/code/run/'

    CLIENT_SECRET = 'd5521e8d3636cbac1084bbd01d80ee6fe6457f1f'

    data = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': code,
        'lang': lang,
        'time_limit': 5,
        'memory_limit': 262144,
        'input': input
    }

    r = requests.post(RUN_URL, data=data)
    json_result = r.json()
    run_status = json_result['run_status']
    print (run_status)

    if run_status['status'] == 'AC':
        return run_status['output_html']
    else:
        return run_status['status_detail']
