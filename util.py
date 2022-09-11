import pickle
import json
import numpy as np

__moiss = None
__data_columns = None
__model = None

def get_estimated_price(mois,moyenne_saisonniere,puissance_electrique_maximale_appelee_en_KVA):
    try:
        loc_index = __data_columns.index(mois.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = moyenne_saisonniere
    x[1] = puissance_electrique_maximale_appelee_en_KVA
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],1)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __moiss
    with open("./artifacts/columnspec.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __moiss = __data_columns[4:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/predictionpec.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __moiss

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('janvier',117, 117))
    print(get_estimated_price('fevrier',124, 117))
    print(get_estimated_price('mars',118,117))
    print(get_estimated_price('avril',112, 117))
    print(get_estimated_price('mai',233, 117))
    print(get_estimated_price('juin',244, 271))
    print(get_estimated_price('juillet',286, 271))
    print(get_estimated_price('aout',324, 271))
    print(get_estimated_price('septembre',283, 271))
    print(get_estimated_price('octobre',242, 117))
    print(get_estimated_price('novembre',131, 117))










