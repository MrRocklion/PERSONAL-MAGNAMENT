import sys
import rc_icons
import pandas as pd
import requests
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QMessageBox,QTableWidgetItem,QFileDialog
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui  import QIcon
from getmac import get_mac_address as gma
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('config.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
user_mac = gma()
user_data = {}
user_ingresos = []
users_salidas = []
doc_ref = db.collection(u'empleados').document(user_mac)
import requests
try:
    request = requests.get("http://www.google.com", timeout=5)
except (requests.ConnectionError, requests.Timeout):
    user_data = {
        u'apellido': u'sin conexion',
        u'nombre': u'sin conexion',
        u'ingresos': [],
        u'salidas': []
        }
    user_ingresos = user_data["ingresos"]
    users_salidas = user_data["salidas"]
    print("Sin conexión a internet.")
else:
    doc = doc_ref.get()
    if doc.exists:
        user_data = doc.to_dict()
        user_ingresos = user_data["ingresos"]
        users_salidas = user_data["salidas"]
        print(user_data)
    else:
        print(u'No such document!')
        doc_ref = db.collection(u'empleados').document(user_mac)
        user_data = {
        u'apellido': u'indefinido',
        u'nombre': u'indefinido',
        u'ingresos': [],
        u'salidas': []
        }
        user_ingresos = user_data["ingresos"]
        users_salidas = user_data["salidas"]
        doc_ref.set(user_data)

def generarExcel():
    print("se genera excel")
    
    try:
        doc_ref = db.collection(u'empleados').document(user_mac)
        doc = doc_ref.get()
        if doc.exists:
            tiempo = datetime.today()
            fecha = str(tiempo.year)+'-'+str(tiempo.month)+'-'+str(tiempo.day)
            hora = str(tiempo.hour)+'-'+str(tiempo.minute)+'-'+str(tiempo.second)
            user_data = doc.to_dict()
            df_ingresos = pd.DataFrame(data=user_data['ingresos'])
            df_salidas = pd.DataFrame(data=user_data['salidas'])
            datos_personales = {'nombres':user_data['nombre'],"apellidos":user_data['apellido']}
            print(datos_personales)
            df_datosp = pd.DataFrame(data=datos_personales,index=[0])
            dialog = QFileDialog().getSaveFileName(
            caption='Save File As',
                dir='{}-{}'.format(fecha,hora),
                selectedFilter="Excel Files (*.xlsx)"
            )
            dir = dialog[0]+".xlsx"
            print(dir)
            writer = pd.ExcelWriter(dir, engine='xlsxwriter')
            df_ingresos.to_excel(writer, sheet_name='Ingresos')
            df_salidas.to_excel(writer, sheet_name='Salidas')
            df_datosp.to_excel(writer, sheet_name='Datos Personales')
            writer.close()
        else:
            print(u'No such document!')
    except:
        QMessageBox.critical(None,'Error!',"Algo sucedio mal intente nuevamente!", QMessageBox.Abort)

   
def registrar_fecha():

    ingreso = window.radIngreso.isChecked()
    if ingreso:
        firebase_puntero = "ingreso"
        firebase_db = "ingresos"
    else:
        firebase_puntero = "salida"
        firebase_db = "salidas"
    msgBox = QMessageBox()
    msgBox.setText("Se va a registrar como {}".format(firebase_puntero))
    msgBox.setInformativeText("Estas seguro de continuar?")

    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.setDefaultButton(QMessageBox.Cancel)
    ret = msgBox.exec()
    if ret == QMessageBox.Ok:
        tiempo = datetime.today()
        fecha = str(tiempo.year)+'-'+str(tiempo.month)+'-'+str(tiempo.day)
        hora = str(tiempo.hour)+':'+str(tiempo.minute)+':'+str(tiempo.second)
        mac = gma()
        comentario = window.comentario.text()

        data_firebase = {"fecha":fecha,"hora":hora,"mac":mac,"comentario":comentario,"tipo":firebase_puntero}
        if ingreso:
            user_ingresos.insert(0, data_firebase)
            estructure_firebase = {firebase_db:user_ingresos}
            window.tableIngresos.clear()
            mapTablaIngresos(user_ingresos)
        else:
            users_salidas.insert(0, data_firebase)
            estructure_firebase = {firebase_db:users_salidas}
            mapTableSalidas(users_salidas)
        try:
            doc_ref = db.collection(u'empleados').document(mac)
            doc_ref.update(estructure_firebase)
        except:
            print("error al enviar datos")
        window.comentario.setText("")


    else:
        print("se cancelo")

def updateNames():
    lastaname = window.lastTxt.text()
    name = window.nameTxt.text()
    newDatos = {'apellido':lastaname,'nombre':name}
    doc_ref = db.collection(u'empleados').document(user_mac)
    doc_ref.update(newDatos)
    window.lastnameLabel.setText(lastaname)
    window.nameLabel.setText(name)

def mapTableSalidas(data):
    window.tableSalidas.clear()
    columns = ['#','Fecha','Hora','Comentario']
    window.tableSalidas.setHorizontalHeaderLabels(columns)
    row = 0
    for e in data:
        window.tableSalidas.insertRow(row)
        window.tableSalidas.setItem(row, 0, QTableWidgetItem(str(row + 1)))
        window.tableSalidas.setItem(row, 1, QTableWidgetItem(str(e['fecha'])))
        window.tableSalidas.setItem(row, 2, QTableWidgetItem(str(e['hora'])))
        window.tableSalidas.setItem(row, 3, QTableWidgetItem(str(e['comentario'])))
        row += 1
def mapTablaIngresos(data):
    window.tableIngresos.clear()
    columns = ['#','Fecha','Hora','Comentario']
    window.tableIngresos.setHorizontalHeaderLabels(columns)
    row = 0
    for e in data:
        window.tableIngresos.insertRow(row)
        window.tableIngresos.setItem(row, 0, QTableWidgetItem(str(row+1)))
        window.tableIngresos.setItem(row, 1, QTableWidgetItem(str(e['fecha'])))
        window.tableIngresos.setItem(row, 2, QTableWidgetItem(str(e['hora'])))
        window.tableIngresos.setItem(row, 3, QTableWidgetItem(str(e['comentario'])))
        row += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)

       
    ui_file_name = "main.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    window.report_btn.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.ReportView))
    window.dash_btn.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.DashBoardView))
    window.config_btn.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.ConfigView))
    window.btnExcel.clicked.connect(lambda: generarExcel())
    window.btnNames.clicked.connect(lambda: updateNames())
    window.macLabel.setText(user_mac)
    window.lastnameLabel.setText(user_data['apellido'])
    window.nameLabel.setText(user_data['nombre'])
    window.lastTxt.setText(user_data['apellido'])
    window.nameTxt.setText(user_data['nombre'])
    window.exit_btn.clicked.connect(lambda: sys.exit(-1) )
    window.registrar_btn.clicked.connect(lambda: registrar_fecha())
    window.tableIngresos.setColumnWidth(0,20)
    window.tableSalidas.setColumnWidth(0, 20)
    mapTablaIngresos(user_ingresos)
    mapTableSalidas(users_salidas)

    ui_file.close()
    if not window:
        sys.exit(-1)
    window.show()
    sys.exit(app.exec())