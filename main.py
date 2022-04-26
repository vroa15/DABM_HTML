#-*- coding: utf-8 -*-

from turtle import color
from flask import Flask, render_template,request
import os
import random

app = Flask(__name__)

@app.route('/login')
def inicio():
    return  render_template('inicio.html')

@app.route('/componentes')
def componentes():
    return render_template('login.html')

@app.route('/validar', methods=["POST"])
def validar():
    if request.method == "POST":
        usuario = request.form['usuario']
        password = request.form['password']


        #Aqui es para verificar usuario y contraseña
        dir = os.path.dirname(__file__)
        ar = 'static/users.csv'
        route = os.path.join(dir,ar)

        f = open(route,'r')
        lineas = f.readlines()
        
        ban_user = 0
        for l in lineas:
            l = l.replace('\n', '')
            txt_user = l.split(';')
        
            
            if usuario == txt_user[0] and password == txt_user[1]:
                print('Usuario valido')
                ban_user = 1

                return render_template('menu.html', title='SISTEMA DE MONITOREO')
                
            elif usuario == txt_user[0] and password != txt_user[1]:
                print('Contraseña incorrecto')
                ban_user = 1
            
        if ban_user == 0:
            print('Usuario no existe')
        
        #Asumiendo que es correcta la validación
 
@app.route('/monitoreo')
def monitoreo():
    datos = getParametros()
    print(datos)

    #lectura = random.randint(0,50)
    #color=0

    lecturas = []
    for i in range(0, 100):
        lectura = random.randint(0,50)
        lecturas.append(lectura)

    colores = []
    for lectura in lecturas:
        color=0
        '''
        condicionales
        '''
        if int(datos[0][1]) <= lectura and int(datos[0][2]) >= lectura:
            color = 1

        if int(datos[1][1]) <= lectura and int(datos[1][2]) >= lectura:
            color = 2

        if int(datos[2][1]) <= lectura and int(datos[2][2]) >= lectura:
            color = 3
        colores.append(color)

    return render_template('monitor.html', datos=datos, lecturas=lecturas, colores=colores)

def getParametros():
    directorio = os.path.dirname(__file__)
    archivo = 'static/parametros.csv'
    ruta = os.path.join(directorio,archivo)

    f = open(ruta,'r')
    lineas = f.readlines()
    f.close()

    #creción matriz para pintar en mi interfaz
    datos = []
    for l in lineas:
        l = l.replace("\n","")
        l=l.split(";")
        datos.append(l)

    return datos

if __name__ == "__main__":
    app.run(debug=True)