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
        '''sql=f"SELECT * FROM reservas WHERE id = LIKE '%busqueda%'"
        con=mysql.connect()
        cur=con.cursor()
        cur.execute(sql)
        resultado =cur.fetchone()
        con.commit()
        return render_templates("mostrador.html1", reserva1=resultado)'''
        return ("señor usuario has accedido por numero de reserva")
    elif cedula == True:
         '''sql=f"SELECT * FROM cedula WHERE id = LIKE '%busqueda%'"
        con=mysql.connect()
        cur=con.cursor()
        cur.execute(sql)
        resultado =cur.fetchone()
        con.commit()
        return render_templates("mostrador2.html", reserva2=resultado)'''
         return ("señor usuario has acedido por numero de cedula")
    else:
        return ("señor usuario asegurese de como digito sus datos su acceso fue denegado")
    

if __name__ == '__main__':
    aplicacion.run(debug=True)
