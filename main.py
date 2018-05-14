from bottle import Bottle, template
import os
import commands
import json


app = Bottle()

@app.get('/')
def index():
    return template('index.html')

@app.get('/config')
def get_config():
    # config = os.popen("sudo curl -X GET  --unix-socket /run/control.unit.sock http://localhost/config/")
    # print(type(config))
    # print(config.read())
    config = os.system("service unit saveconfig")
    config_content = ""
    with open('/etc/unit/config', 'r') as f:
        for l in f.read():
            config_content += l

    config_dict = json.loads(config_content)
    print(config_dict)
    return {'code':0, 'config':config_dict}


app.run(debug=True)