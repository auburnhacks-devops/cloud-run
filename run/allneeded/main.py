# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_allneeded_service]
# [START run_allneeded_service]
import csv
import lib.pandas as pd
import requests
from lib.flask import Flask,render_template,request,redirect,Response,flash,url_for
#from lib.flask_table import Table, Col
import os     
import sys
from datetime import datetime
CSV_URL = 'https://api.covidtracking.com/v1/states/current.csv'
data=pd.read_csv(CSV_URL)

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_allneeded_service]
# [END cloudrun_allneeded_service]
