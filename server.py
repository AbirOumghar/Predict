from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


@app.route('/get_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'moiss': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_pruissance', methods=['GET', 'POST'])
def predict_home_price():
    mois = request.form['mois']
    puissance_electrique_maximale_appelee_en_KVA = float(request.form['puissance_electrique_maximale_appelee_en_KVA'])
    moyenne_saisonniere = float(request.form['moyenne_saisonniere'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(mois,puissance_electrique_maximale_appelee_en_KVA,moyenne_saisonniere)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()