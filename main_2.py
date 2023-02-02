import sys
import rc_icons
import pandas as pd
import requests
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QMessageBox,QTableWidgetItem,QFileDialog,QMainWindow
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui  import QIcon
from getmac import get_mac_address as gma
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Ui_MainWindow import Ui_MainWindow
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
    request = requests.get("http://www.google.com", timeout=1)
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

   
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        #self.ui.dash_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.DashBoardView))
        #self.ui.config_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ConfigView))
        #self.ui.btnExcel.clicked.connect(lambda: self.generarExcel())
        self.ui.btnNames.clicked.connect(lambda: self.updateNames())
        self.ui.macLabel.setText(user_mac)
        self.ui.lastnameLabel.setText(user_data['apellido'])
        self.ui.nameLabel.setText(user_data['nombre'])
        self.ui.lastTxt.setText(user_data['apellido'])
        self.ui.nameTxt.setText(user_data['nombre'])
        self.ui.exit_btn.clicked.connect(lambda: sys.exit(-1) )
        self.ui.registrar_btn.clicked.connect(lambda: self.registrar_fecha())
        self.ui.tableIngresos.setColumnWidth(0,20)
        self.ui.tableSalidas.setColumnWidth(0, 20)
        # self.mapTablaIngresos(user_ingresos)
        # self.mapTableSalidas(users_salidas)
    def mapTablaIngresos(self,data):
        self.ui.tableIngresos.clear()
        columns = ['#','Fecha','Hora','Comentario']
        self.ui.tableIngresos.setHorizontalHeaderLabels(columns)
        row = 0
        for e in data:
            self.ui.tableIngresos.insertRow(row)
            self.ui.tableIngresos.setItem(row, 0, QTableWidgetItem(str(row+1)))
            self.ui.tableIngresos.setItem(row, 1, QTableWidgetItem(str(e['fecha'])))
            self.ui.tableIngresos.setItem(row, 2, QTableWidgetItem(str(e['hora'])))
            self.ui.tableIngresos.setItem(row, 3, QTableWidgetItem(str(e['comentario'])))
            row += 1
    def updateNames(self):
        lastaname = self.ui.lastTxt.text()
        name = self.ui.nameTxt.text()
        newDatos = {'apellido':lastaname,'nombre':name}
        doc_ref = db.collection(u'empleados').document(user_mac)
        doc_ref.update(newDatos)
        self.ui.lastnameLabel.setText(lastaname)
        self.ui.nameLabel.setText(name)
    def mapTableSalidas(self,data):
        self.ui.tableSalidas.clear()
        columns = ['#','Fecha','Hora','Comentario']
        self.ui.tableSalidas.setHorizontalHeaderLabels(columns)
        row = 0
        for e in data:
            self.ui.tableSalidas.insertRow(row)
            self.ui.tableSalidas.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.ui.tableSalidas.setItem(row, 1, QTableWidgetItem(str(e['fecha'])))
            self.ui.tableSalidas.setItem(row, 2, QTableWidgetItem(str(e['hora'])))
            self.ui.tableSalidas.setItem(row, 3, QTableWidgetItem(str(e['comentario'])))
            row += 1
    def registrar_fecha(self):
        ingreso = self.ui.radIngreso.isChecked()
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
            comentario = self.ui.comentario.text()

            data_firebase = {"fecha":fecha,"hora":hora,"mac":mac,"comentario":comentario,"tipo":firebase_puntero}
            if ingreso:
                user_ingresos.insert(0, data_firebase)
                estructure_firebase = {firebase_db:user_ingresos}
                self.ui.tableIngresos.clear()
                self.mapTablaIngresos(user_ingresos)
            else:
                users_salidas.insert(0, data_firebase)
                estructure_firebase = {firebase_db:users_salidas}
                self.mapTableSalidas(users_salidas)
            try:
                doc_ref = db.collection(u'empleados').document(mac)
                doc_ref.update(estructure_firebase)
            except:
                print("error al enviar datos")
            self.ui.comentario.setText("")


        else:
            print("se cancelo")
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
