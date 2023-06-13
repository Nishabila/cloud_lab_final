# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask, jsonify
import numpy as np

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

def find_nth_largest(numbers, n):
    sorted_numbers = sorted(numbers, reverse=True)
    if 1 <= n <= len(sorted_numbers):
        return sorted_numbers[n-1]
    else:
        return None
    
@app.route("/")
def hello():
    numbers = [5, 9, 3, 1, 7, 2, 8, 6, 4]
    n = 3  # Change this value to the desired nth largest number
    
    nth_largest = find_nth_largest(numbers, n)
    if nth_largest is not None:
        return f"The {n}th largest number is: {nth_largest}"
    else:
        return f"There is no {n}th largest number in the list."


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=5001, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]