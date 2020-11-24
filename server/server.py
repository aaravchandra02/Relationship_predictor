from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


# This is how we expose HTTP endpoint:
@app.route("/hello")
def hello():
    return "Hi This is my first routing"


@app.route('/form-example', methods=['POST', 'GET'])
def formexample():
    print(f"\n{request.data}\n\n\n{request.args}\n\n\n{request.form}\n\n\n{request.files}\n\n\n{request.values}\n\n\n{request.get_json()}\n\n\n")
    return "hello"


@app.route("/relationship", methods=["POST"])
def predict_relationship_future():
    # This below needs to store the response that has come from POST of relationship.html
    resp_arr = request.form["location"]

    answer = util.get_prediction(resp_arr)

    response = jsonify(
        {"estimated_prediction": answer}
    )
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    print(f"\nStarting the Flask server for our wonderful predictor. Hurray!! \n\n")
    util.load_saved_models()
    app.run(debug=True)
