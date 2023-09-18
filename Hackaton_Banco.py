import myslq.connector
from mysql.conector import Error
import decimal from Decimal


class Banco:
    __init__(self):
    self.connection = self.conectarDB()
    self.cursor = self.connection.cursor()

    def conectarDB():
        try:
            connection = mysql.connector.connect(
                host:"localhost",
                user:"",
                password:"",
                database:"", )
            return connection
        except Error as e:
            print("Error de conexion base de datos",e)

    def cerrarConnection():
        self.connection.close()
        self.cursor.close()


    def crearCuenta(self, name, ap_p, ap_m, saldo):
        try:
            self.cursor.execute("SELECT nombre FROM cuentas WHERE %s", (name,))
            cuenta_ya_existe = self.cursor.fetchone()
            if cuenta_ya_existe:
                print("Ya exitse una cuenta sociada con el nombre del cliente")
            else: 
                self.cursor.execute("INSERT INTO cuentas"
                                    "(nombre, apellidoP, apellidoM, saldo)"
                                    "VALUES(%s,%s,%s,%s)", (name, ap_p, ap_m, saldo))

                self.cursor.commit()
                print(f'Cuenta crada con exito. EL número de cuenta es: ',self.cursor.lastrowid)    
        except:
            pass
            
    
    def consultarSaldo(self, idCuenta):

        try:
            try:    
                print("Ingresa el ID de la cuenta")
                id_cuenta = input()
                cursor = ("SELECT saldo from cuentas WHERE idC = ?" (id_cuenta,))
                saldo = cursor.fetchone()
                print("Tu saldo es: ")
                if saldo:
                    return saldo[0]
                else:
                    return None
            except: 
                print("Cuenta no encontrada")
        except:
            print("ID incorrecto, prueba otra vez")
    
    def hacer_depósito(self, idCuenta, monto):

        try:
            try:    
                cursor = ("UPDATE cuentas SET Saldo = Saldo + ? WHERE ID=?", (monto, idCuenta))
                self.connection.commit()
            except: 
                print("Cuenta no encontrada")
        except:
            print("ID incorrecto, prueba otra vez")

        
    def hacer_retiro(self, idCuenta, retiro):
        try:
            saldo = consultaSaldo()
            if (saldo and saldo>retiro):
                 self.cursor.execute("UPDATE saldo FROM cuentas WHERE ?", (idCuenta,))

            


