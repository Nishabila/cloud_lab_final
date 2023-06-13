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

@app.route("/")
def multiply_matrices():
    """Multiply two matrices and print the result.

    Returns:
        A string indicating the completion of matrix multiplication.
    """
    # Example matrices
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])

    # Perform matrix multiplication
    result = np.matmul(matrix1, matrix2)
    # Convert the resulting matrix to a list of lists
    result_list = result.tolist()

    # Return the result as JSON
    return jsonify(result=result_list)

    # Print the result
    #print(result)

    # Return a completion message
    #return "Matrix multiplication completed. Check the logs for the result."

if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=5000, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]