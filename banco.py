import mysql.connector
from mysql.connector import Error
from decimal import Decimal

class Banco:
    def __init__(self):
        self.connection = self.conectarBD()
        self.cursor = self.connection.cursor()

    def conectarBD(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="minihack",
                password="$Banco",
                database="simulador"
            )
            return conexion
        except Error as e:
            print("Error al conectar con la base de datos. ", e)
            return None

    def cerrar_conexion(self):
        self.connection.close
        self.cursor.close

    def crear_cuenta(self, nombre_cliente, saldo):
        try:
            self.cursor.execute("SELECT * FROM cuentas WHERE NombreCliente = %s", (nombre_cliente,))
            cuenta_existente = self.cursor.fetchone()
            if cuenta_existente:
                print(f"Ya existe una cuenta para el nombre {nombre_cliente}.")
            else:
                self.cursor.execute("INSERT INTO cuentas (NombreCliente,Saldo) VALUES (%s,%s)", (nombre_cliente,saldo))
                self.connection.commit()
                print("Cuenta creada con exito. El numero de cuenta es: ", self.cursor.lastrowid)
        except Error as e:
            print("Error al crear la cuenta ",e)

    def consultar_saldo(self, id_cuenta):
        try:
            self.cursor.execute("SELECT Saldo FROM cuentas WHERE ID_Cuenta = %s", (id_cuenta,))
            saldo = self.cursor.fetchone()
            if saldo:
                print(f"El saldo de la cuenta {id_cuenta} es: ${saldo[0]:.2f}")
            else:
                print("Cuenta no encontrada. ")
        except Error as e:
            print("Error al consultar saldo ",e)
 

    def hacer_deposito(self, id_cuenta, monto):
        try:
            self.cursor.execute("SELECT Saldo FROM cuentas WHERE ID_Cuenta = %s",(id_cuenta,))
            saldo = self.cursor.fetchone()
            if saldo:
                nuevo_saldo = saldo[0] + monto
                self.cursor.execute("UPDATE cuentas SET Saldo = %s WHERE ID_Cuenta = %s",(nuevo_saldo,id_cuenta))
                self.connection.commit()
                self.registrar_transaccion(id_cuenta, "Deposito", monto)
                print(f"Deposito de ${monto:.2f} realizado en la cuenta {id_cuenta} ")
            else:
                print("Cuenta no encontrada")
        except Error as e:
            print("Error al realizar deposito ",e)

    def hacer_retiro(self, id_cuenta, monto):
        try:
            self.cursor.execute("SELECT Saldo FROM cuentas WHERE ID_Cuenta = %s",(id_cuenta,))
            saldo = self.cursor.fetchone()
            if saldo:
                if saldo[0] >= monto:
                    nuevo_saldo = saldo[0] - monto
                    self.cursor.execute("UPDATE cuentas SET Saldo = %s WHERE ID_Cuenta = %s",(nuevo_saldo,id_cuenta))
                    self.connection.commit()
                    self.registrar_transaccion(id_cuenta, "Retiro", monto)
                    print(f"Retiro de ${monto:.2f} realizado en la cuenta {id_cuenta} ")
                else:
                    print("Saldo insuficiente para realizar retiro.")
            else:
                print("Cuenta no encontrada")
        except Error as e:
            print("Error al realizar retiro ",e)

    def ver_transacciones(self, id_cuenta):
        try:
            self.cursor.execute("SELECT * FROM transacciones WHERE ID_Cuenta = %s",(id_cuenta,))
            transacciones = self.cursor.fetchall()
            if transacciones:
                print(f"\n Historial de transacciones de la cuenta {id_cuenta}:")
                for transaccion in transacciones:
                    print(f"ID: {transaccion[0]}, Tipo: {transaccion[2]}, Monto: {transaccion[3]}, Fecha: {transaccion[4]}")
            else:
                print("No hay transacciones para esta cuenta.")        
        except Error as e:
           print("Error al consultar el historial de transacciones ",e)


    def registrar_transaccion(self, id_cuenta, tipo, monto):
        try:
            self.cursor.execute("INSERT INTO transacciones (ID_Cuenta, Tipo, Monto) VALUES (%s,%s,%s)", (id_cuenta,tipo,monto))
            self.connection.commit()
        except Error as e:
            print("Error al registrar la transaccion")

    def transferir_fondos(self,id_cuenta_origen, id_cuenta_destino, monto):
        if self.hacer_retiro(id_cuenta_origen, monto):
            self.hacer_deposito(id_cuenta_destino, monto)
            self.registrar_transaccion(id_cuenta_origen, "Retiro", monto)
            self.registrar_transaccion(id_cuenta_destino, "Deposito", monto)
            print("Transferencia exitos, favor de consultar su saldo")
            return True
        else:
            return False

    def opciones():
        print('''
        
    ---------WELCOME---------------------------
        1- Crear cuenta
        2- Consultar saldo en cuenta
        3- Hacer un deposito
        4- Hacer retiros
        5- Hacer transferencia
        6- Historial de transacciones
        7- Salir
    ------------------------------------------
        ''')
        while True:
            centinela = input("Elija la opcion de su preferencia: ")
            if centinela in ["1", "2", "3", "4", "5", "6", "7"]:
                return centinela
            print("[!] Opcion no valida, reintente\n")
    
    def acciones(centinela):
        if centinela == "1":
            id_cuenta=int(input("Ingrese su Numero de Cuenta: "))
            saldo_inicial=Decimal(input("Ingrese el saldo inicial: "))
            banco.crear_cuenta(nombre_cliente,saldo_inicial)
        elif centinela == "2":
            id_cuenta=int(input("Ingrese ID de la Cuenta: "))
            banco.consultar_saldo(id_cuenta)
        elif centinela == "3":
            id_cuenta=int(input("Ingrese ID de la Cuenta: "))
            monto=Decimal(input("Ingrese el monto a depositar: "))
            banco.hacer_deposito(id_cuenta,monto)
        elif centinela == "4":
            id_cuenta=int(input("Ingrese ID de la Cuenta: "))
            monto=Decimal(input("Ingrese el monto a retirar: "))
            banco.hacer_retiro(id_cuenta,monto)
        elif centinela == "5":
            id_origen=int(input("Ingrese ID de la Cuenta de origen: "))
            id_destino=int(input("Ingrese ID de la Cuenta de destino: "))
            monto=Decimal(input("Ingrese el monto a depositar: "))
            banco.transferir_fondos(id_origen,id_destino,monto)
        elif centinela == "6":
            id_cuenta=int(input("Ingrese ID de la Cuenta: "))
            monto=Decimal(input("Ingrese el monto a depositar: "))
            banco.hacer_deposito(id_cuenta,monto)
        elif centinela == "7":
            print("Gracias por participar!")
    opt = opciones()
    acciones(opt)
