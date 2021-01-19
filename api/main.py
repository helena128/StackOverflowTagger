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
    def run_model(model, X, k):
        import numpy as np

        all_probs = model.predict_proba(X)
        topk_idx = np.argpartition(y, -k)[:, :-k-1:-1]
        topk_classes = model.classes_[topk_idx]
        topk_probs = np.array([all_probs[n, idx]
                               for n, idx in enumerate(topk_idx)])
        return [
            [{'class': c, 'probability': p}
             for p, c in sorted(zip(probs, classes), reverse=True)]
            for classes, probs in zip(topk_classes, topk_probs)]

    if model:
        try:
            json_ = request.json
            print(json_)
            title = TextPreprocessor.clean_text(json_['title'])
            body = TextPreprocessor.clean_text(json_['body'])
            k = json_.get('k', 3)

            query = title + ' ' + body
            prediction = run_model(model, [query], k)[0]

            return jsonify({
                'title': title,
                'body': body,
                'prediction': prediction})

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
