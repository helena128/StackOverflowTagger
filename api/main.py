from flask import Flask, request, jsonify
import joblib
import traceback

from text_processor import TextPreprocessor

app = Flask(__name__)

model = None


@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"


@app.route('/predict', methods=['POST'])
def predict():
    if model:
        try:
            json_ = request.json
            print(json_)
            title = TextPreprocessor.clean_text(json_['title'])
            body = TextPreprocessor.clean_text(json_['body'])

            query = title + ' ' + body
            prediction = model.predict([query])[0]

            return jsonify({
                'title': title,
                'body': body,
                'prediction': str(prediction)})

        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return 'No model here to use'


if __name__ == '__main__':
    print('Start init text preprocessor')
    # TextPreprocessor.init()
    print('Text preprocessor initialized')

    print('Start model loading')
    model = joblib.load('model.pkl')
    print('Model loaded')
    app.run(debug=True, port=8080)