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
    elif centinela >"7":
        print("No valido")
opt = opciones()
acciones(opt)
