from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


# This is how we expose HTTP endpoint:


@app.route("/hello")
def hello():
    return "Hi This is my first routing"


@app.route('/json-example', methods=['POST', 'GET'])
def formexample():
    # request.headers.add('Access-Control-Allow-Origin', '*')
    usr_data = request.form.getlist("usr_data[]")
    usr_data = list(map(int, usr_data))  # values converted to int type.
    print(usr_data, type(usr_data[1]))
    # print(request.form.getlist("usr_data[]"))
    answer = util.get_prediction(usr_data)
    print(answer)
    response = jsonify(
        {"estimated_prediction": answer}
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(f"answer = {answer}\n\nresponse with header = {response}")
    return response


# @app.route("/relationship", methods=["POST"])
# def predict_relationship_future():
#     # This below needs to store the response that has come from POST of relationship.html
#     resp_arr = request.form["location"]

#     # answer = util.get_prediction(usr_data)

#     response = jsonify(
#         {"estimated_prediction": answer}
#     )
#     response.headers.add("Access-Control-Allow-Origin", "*")

#     return response


if __name__ == "__main__":
    print(f"\nStarting the Flask server for our wonderful predictor. Hurray!! \n\n")
    util.load_saved_models()
    app.run(debug=True)
