import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import sklearn

app = Flask(__name__) #iniciar app flask
model = pickle.load(open('model.pkl', 'rb')) #Cargar modelo

@app.route('/')
def home():
    return render_template('index.html') #aqui se pone el html, es el diseño de la pagina web

@app.route('/predict',methods=['POST']) #obtener registro
def predict():
    '''
    For rendering results on HTML GUI
    '''
    colors = ["Azul","Verde","Rojo"] #los colores deben estar ordenados de acuerdo al valor numerico asignado en la base de datos, despues obtengo el valor
    ingreso = [float(x) for x in request.form.values()]
    final_features = [np.array(ingreso)] #crear arreglo
    prediction = model.predict(final_features) #predecir y guardar valor

    output = round(prediction[0])
#en el return regresa el resultado despues de enviar el valor muestreado
    return render_template('index.html', prediction_text='Led: {}'.format(colors[output]))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True) #correr la app en el puerto indicado
