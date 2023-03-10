import sys
import pandas as pd
from PySide6.QtWidgets import QApplication,QMessageBox,QTableWidgetItem,QFileDialog,QMainWindow
from PySide6.QtGui  import QIcon
from getmac import get_mac_address as gma
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from ui_main import Ui_MainWindow
import uuid
import asyncio
# Use a service account.
cred = credentials.Certificate('config.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
user_mac = gma()
user_data = {}
user_ingresos = []
users_salidas = []
users_horasp = []
users_diasp = []
users_almuerzosI = []
users_almuerzosS = []
doc_ref = db.collection(u'empleados').document(user_mac)

try:
    doc = doc_ref.get()
    if doc.exists:
        user_data = doc.to_dict()
        user_ingresos = user_data["ingresos"]
        users_salidas = user_data["salidas"]
        users_horasp = user_data["horas_permiso"]
        users_diasp = user_data["dias_permiso"]
        users_almuerzosI = user_data["almuerzo_ingresos"]
        users_almuerzosS = user_data["almuerzo_salidas"]
    else:
        print(u'No such document!')
        doc_ref = db.collection(u'empleados').document(user_mac)
        user_data = {
        u'apellido': u'indefinido',
        u'nombre': u'indefinido',
        u'ingresos': [],
        u'salidas': [],
        u'horas_permiso': [],
        u'dias_permiso': [],
        u'almuerzo_salidas': [],
        u'almuerzo_ingresos': []
        }
        doc_ref.set(user_data)
except Exception as e:
    print(e)

   
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('ico.ico'))
        #variables de inicio
      
        #botones para cambiar de vista
        self.ui.dash_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.DashBoardView))
        self.ui.config_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ConfigView))
        self.ui.report_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ReportView))
        self.ui.extras_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.PermisosView))
        self.ui.almuerzo_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.AlmuerzosView))
        self.ui.btnExcel.clicked.connect(lambda: self.generarExcel())
        self.ui.btnNames.clicked.connect(lambda: self.updateNames())
        self.ui.macLabel.setText(user_mac)
        self.ui.lastnameLabel.setText(user_data['apellido'])
        self.ui.nameLabel.setText(user_data['nombre'])
        self.ui.lastTxt.setText(user_data['apellido'])
        self.ui.nameTxt.setText(user_data['nombre'])
        self.ui.exit_btn.clicked.connect(lambda: sys.exit(-1) )
        #botones para registrar ingresos y salidas
        self.ui.registrar_btn.clicked.connect(lambda: self.registrar_fecha())
        self.ui.registrar_btn_2.clicked.connect(lambda: self.registrarAlmuerzo())
        #botnes de la vista dias y horas permiso
        self.ui.btnDia.clicked.connect(lambda: self.RegistrarDiasPermiso())
        self.ui.btnHorasPermiso.clicked.connect(lambda: self.RegistrarHorasPermiso())
        #funciones para mapear
        self.mapTablaIngresos(user_ingresos)
        self.mapTableSalidas(users_salidas)
        self.mapTableDiasP(users_diasp)
        self.mapTableHorasP(users_horasp)
        self.mapTablaIngresosAlmuerzo(users_almuerzosI)
        self.mapTableSalidasAlmuerzos(users_almuerzosS)
    def mapTableDiasP(self,data):
        self.ui.tablaDias.clear()
        columns = ['Fecha','Motivo']
        self.ui.tablaDias.setHorizontalHeaderLabels(columns)
        row = 0
        for e in data:
            self.ui.tablaDias.insertRow(row) 
            self.ui.tablaDias.setItem(row, 0, QTableWidgetItem(str(e['dia'])))
            self.ui.tablaDias.setItem(row, 1, QTableWidgetItem(str(e['motivo'])))
            row += 1
    def mapTableHorasP(self,data):
        self.ui.tablaHoras.clear()
        columns = ['Salida','Reingreso','Motivo']
        self.ui.tablaHoras.setHorizontalHeaderLabels(columns)
        row = 0
        for e in data:
            self.ui.tablaHoras.insertRow(row)   
            self.ui.tablaHoras.setItem(row, 0, QTableWidgetItem(str(e['hora_salida'])))
            self.ui.tablaHoras.setItem(row, 1, QTableWidgetItem(str(e['hora_reingreso'])))
            self.ui.tablaHoras.setItem(row, 2, QTableWidgetItem(str(e['motivo'])))
            row += 1
    def mapTablaIngresos(self,data):
        self.ui.tableIngresos.clear()
        columns = ['Fecha','Hora','Comentario']
        self.ui.tableIngresos.setHorizontalHeaderLabels(columns)
        row = 0
        for e in data:
            self.ui.tableIngresos.insertRow(row)
            self.ui.tableIngresos.setItem(row, 0, QTableWidgetItem(str(e['fecha'])))
            self.ui.tableIngresos.setItem(row, 1, QTableWidgetItem(str(e['hora'])))
            self.ui.tableIngresos.setItem(row, 2, QTableWidgetItem(str(e['comentario'])))
            row += 1
    def mapTablaIngresosAlmuerzo(self,data):
        self.ui.tableIngresos_2.clear()
        columns = ['Fecha','Hora','Comentario']
        self.ui.tableIngresos_2.setHorizontalHeaderLabels(columns)
        row = 0
        for e in data:
            self.ui.tableIngresos_2.insertRow(row)
            self.ui.tableIngresos_2.setItem(row, 0, QTableWidgetItem(str(e['fecha'])))
            self.ui.tableIngresos_2.setItem(row, 1, QTableWidgetItem(str(e['hora'])))
            self.ui.tableIngresos_2.setItem(row, 2, QTableWidgetItem(str(e['comentario'])))
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
        columns = ['Fecha','Hora','Comentario']
        self.ui.tableSalidas.setHorizontalHeaderLabels(columns)
        row = 0
        for e in data:
            self.ui.tableSalidas.insertRow(row)
            self.ui.tableSalidas.setItem(row, 0, QTableWidgetItem(str(e['fecha'])))
            self.ui.tableSalidas.setItem(row, 1, QTableWidgetItem(str(e['hora'])))
            self.ui.tableSalidas.setItem(row, 2, QTableWidgetItem(str(e['comentario'])))
            row += 1
    def mapTableSalidasAlmuerzos(self,data):
        self.ui.tableSalidas_2.clear()
        columns = ['Fecha','Hora','Comentario']
        self.ui.tableSalidas_2.setHorizontalHeaderLabels(columns)
        row = 0
        for e in data:
            self.ui.tableSalidas_2.insertRow(row)
            self.ui.tableSalidas_2.setItem(row, 0, QTableWidgetItem(str(e['fecha'])))
            self.ui.tableSalidas_2.setItem(row, 1, QTableWidgetItem(str(e['hora'])))
            self.ui.tableSalidas_2.setItem(row, 2, QTableWidgetItem(str(e['comentario'])))
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
            if comentario == "":
                comentario = "ninguno"
            data_firebase = {"fecha":fecha,"hora":hora,"mac":mac,"comentario":comentario,"tipo":firebase_puntero,'id':str(uuid.uuid4())}
            if ingreso:
                user_ingresos.insert(0, data_firebase)
                print(user_ingresos)
                estructure_firebase = {firebase_db:user_ingresos}
                flag = self.updateFirebase(estructure_firebase)
                if flag:
                    self.mapTablaIngresos(user_ingresos)
                else: 
                    pass
                
            else:
                users_salidas.insert(0, data_firebase)
                estructure_firebase = {firebase_db:users_salidas}
                flag = self.updateFirebase(estructure_firebase)
                if flag:
                    self.mapTableSalidas(users_salidas)
                else: 
                    pass
          
            self.ui.comentario.setText("")


        else:
            print("se cancelo")
        
    def generarExcel(self):
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
                df_datosp = pd.DataFrame(data=datos_personales,index=[0])
                df_almuerzosI = pd.DataFrame(data=user_data['almuerzo_ingresos'])
                df_almuerzosS = pd.DataFrame(data=user_data['almuerzo_salidas'])
                df_diasp = pd.DataFrame(data=user_data['dias_permiso'])
                df_horasp = pd.DataFrame(data=user_data['horas_permiso'])
                print(df_datosp)
                dialog = QFileDialog().getSaveFileName(
                caption='Save File As',
                    dir='{}-{}'.format(fecha,hora),
                    selectedFilter="Excel Files (*.xlsx)"
                )
                dir = dialog[0]+".xlsx"
                print(dir)
                with pd.ExcelWriter(dir) as writer:
                    df_ingresos.to_excel(writer, sheet_name='Ingresos')
                    df_salidas.to_excel(writer, sheet_name='Salidas')
                    df_datosp.to_excel(writer, sheet_name='Datos Personales')
                    df_almuerzosI.to_excel(writer, sheet_name='Ingresos del Almuerzo')
                    df_almuerzosS.to_excel(writer, sheet_name='Salidas del Almuerzo')
                    df_diasp.to_excel(writer, sheet_name='Dias Permiso')
                    df_horasp.to_excel(writer, sheet_name='Horas Permiso')
            else:
                print(u'No such document!')
        except:
            QMessageBox.critical(None,'Error!',"Algo sucedio mal intente nuevamente!", QMessageBox.Abort)
    def RegistrarHorasPermiso(self):
        tiempo = datetime.today()
        motivo_hora = self.ui.motivoHora.text()
        fecha = str(tiempo.year)+'-'+str(tiempo.month)+'-'+str(tiempo.day)
        if motivo_hora == "":
            motivo_hora = "ninguno"
        hora_salida = self.ui.timeSalida.time()
        hora_reingreso  = self.ui.timeReingreso.time()
        time_formated_salida = hora_salida.toString(self.ui.timeSalida.displayFormat())
        time_formated_re = hora_reingreso.toString(self.ui.timeReingreso.displayFormat())
        newHoraPermiso = {'hora_salida':time_formated_salida,'fecha':fecha,'hora_reingreso':time_formated_re,'motivo':motivo_hora,'id':str(uuid.uuid4())}
        msgBox = QMessageBox()
        msgBox.setText("Se va a registrar el dia como {}-{}".format(newHoraPermiso['hora_salida'],newHoraPermiso['hora_reingreso']))
        msgBox.setInformativeText("Estas seguro de continuar?")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Cancel)
        ret = msgBox.exec()
        if ret == QMessageBox.Ok:
            users_horasp.insert(0,newHoraPermiso)
            estructure_firebase = {'horas_permiso':users_horasp}
            flag = self.updateFirebase(estructure_firebase)
            if flag:
                self.mapTableHorasP(users_horasp)
                self.ui.motivoHora.setText("")
            else: 
                pass
        

    def RegistrarDiasPermiso(self):
        motivo_dia = self.ui.motivoDia.text()
        dia = self.ui.timeDia.date()
        time_formated_dia = dia.toString(self.ui.timeDia.displayFormat())
       
        if motivo_dia == "":
            motivo_dia = "ninguno"
        newDiaPermiso = {'dia':time_formated_dia,'motivo':motivo_dia,'id':str(uuid.uuid4())}
        msgBox = QMessageBox()
        msgBox.setText("Se va a registrar el dia como {}-{}".format(newDiaPermiso['dia'],newDiaPermiso['motivo']))
        msgBox.setInformativeText("Estas seguro de continuar?")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Cancel)
        ret = msgBox.exec()
        if ret == QMessageBox.Ok:
            users_diasp.insert(0,newDiaPermiso)
            estructure_firebase = {'dias_permiso':users_diasp}
            flag = self.updateFirebase(estructure_firebase)
            if flag:
                self.mapTableDiasP(users_diasp)
                self.ui.motivoDia.setText("")
            else: 
                pass
    def registrarAlmuerzo(self):
        ingreso = self.ui.radIngreso_2.isChecked()
        if ingreso:
            firebase_puntero = "ingreso"
            firebase_db = "almuerzo_ingresos"
        else:
            firebase_puntero = "salida"
            firebase_db = "almuerzo_salidas"
        msgBox = QMessageBox()
        msgBox.setText("Se va a registrar el almuerzo como {}".format(firebase_puntero))
        msgBox.setInformativeText("Estas seguro de continuar?")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Cancel)
        ret = msgBox.exec()
        if ret == QMessageBox.Ok:
            tiempo = datetime.today()
            fecha = str(tiempo.year)+'-'+str(tiempo.month)+'-'+str(tiempo.day)
            hora = str(tiempo.hour)+':'+str(tiempo.minute)+':'+str(tiempo.second)
            mac = gma()
            comentario = self.ui.comentarioAlmuerzo.text()
            if comentario == "":
                comentario = "ninguno"
          
                

            data_firebase = {"fecha":fecha,"hora":hora,"mac":mac,"comentario":comentario,"tipo":firebase_puntero,'id':str(uuid.uuid4())}
            if ingreso:
                users_almuerzosI.insert(0, data_firebase)
                print(user_ingresos)
                estructure_firebase = {firebase_db:users_almuerzosI}
                flag = self.updateFirebase(estructure_firebase)
                if flag:
                    self.mapTablaIngresosAlmuerzo(users_almuerzosI)
                else: 
                    pass
                
            else:
                users_almuerzosS.insert(0, data_firebase)
                estructure_firebase = {firebase_db:users_almuerzosS}
                flag = self.updateFirebase(estructure_firebase)
                if flag:
                    self.mapTableSalidasAlmuerzos(users_almuerzosS)
                else: 
                    pass
          
            self.ui.comentario.setText("")


        else:
            print("se cancelo")
    def updateFirebase(self,datos):
        try:
            doc_ref = db.collection(u'empleados').document(user_mac)
            doc_ref.update(datos)
            return True
        except Exception as e:
            print(e)
            QMessageBox.critical(None,'Error!',"Algo sucedio mal intente nuevamente!", QMessageBox.Abort)
            return False

       
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
