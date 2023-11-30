from flask import Flask,render_template,request
import re


aplicacion= Flask(__name__)


@aplicacion.route("/")
def index():
    return render_template("/panel.html")

@aplicacion.route("/buscadorReserva", methods=['POST'])
def buscadorReserva():
    patron = r'^\d[a-zA-Z]{2}\d{2}[a-fA-F]$'
    busqueda=request.form['num_reserva']
    cedula=busqueda.isnumeric()
    if re.match(patron, busqueda):
        return ("señor usuario has accedido por numero de reserva")
    elif cedula == True:
        return ("señor usuario has acedido por numero de cedula")
    else:
        return ("señor usuario asegurese de como digito sus datos su acceso fue denegado")
    

if __name__ == '__main__':
    aplicacion.run(debug=True)
