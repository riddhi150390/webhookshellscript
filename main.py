import subprocess
from os import path
import flask
import json
import os

from config import secret_token, projects_to_scripts

script_path = 'scripts/webhook_handler.sh'

app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    if flask.request.headers.get('Authorization') != secret_token:
        return flask.abort(401)

    project_name = flask.request.json.get("project_name")
    if project_name is None:
        return flask.abort(400)

    script_name = projects_to_scripts.get(project_name)
    if script_name is None:
        return flask.abort(404)

    try:
        subprocess.run([script_path], check=True)
    except subprocess.CalledProcessError:
        return flask.abort(500)

    json_file_name = 'scan_results.json'
    jq_command = ["jq", ".", json_file_name]
    jq_process = subprocess.Popen(jq_command, stdout=subprocess.PIPE, text=True)
    jq_output, _ = jq_process.communicate()
  
    return jq_output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2015, threaded=False)
