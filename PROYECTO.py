from tkinter import W
import pandas as pd
import datetime as dt
ruta_Usuarios = 'Hospital.xlsx'
ruta_Passwords = 'USERS.xlsx'
ruta_Flujo = 'Horaentrada.xlsx'
workers = pd.read_excel(ruta_Passwords)
users = pd.read_excel(ruta_Usuarios)
RegisterDate = pd.read_excel(ruta_Flujo)

def columns(df):
    columnas = df.columns
    list_columnas = list(columnas)
    return list_columnas

def list_(df,nombre):
    filas = pd.unique(df[nombre])
    list_filas = list(filas)
    return list_filas

def _register():
    global users
    global User
    global workers
    print('El usuario {} no existe'.format(User))
    User_Now = input('Presione R si desea registrase: ')
    if User_Now == 'R':
        dict_checktime = {}
        dict_User = {}
        dict_userPassword = {}
        columnas_df = columns(users)
        for Datos in columnas_df:
            if Datos != 'ESTADO' and Datos != 'SUELDO':
                dict_User[Datos] = input(f'Inserta {Datos}: ')
                if Datos == 'NOMBRE':
                    dict_userPassword['NOMBRE'] = dict_User['NOMBRE']
                    dict_checktime['NOMBRE'] = dict_User['NOMBRE']
                    dict_userPassword['CONTRASEÑAS'] = input('Ingresa una contraseña: ')
                    RegisterDate = RegisterDate.append(dict_checktime,ignore_index=True)
                    workers = workers.append(dict_userPassword , ignore_index=True )
            else:
                break
        users = users.append(dict_User , ignore_index= True )
        workers.to_excel(ruta_Passwords ,index = False)
        users.to_excel(ruta_Usuarios ,index = False)
        print(workers)
        index = workers.index[workers['NOMBRE'] == dict_User['NOMBRE']]
        print(index)
        workers.at[index,'CONTRASEÑAS'] = input('Nueva contraseña: ')
        workers.to_excel(ruta_Passwords ,index = False)
        print(workers)
        _result = True
    else:
        _result = False
    return _result

def checktime():
    global User
    global RegisterDate
    houropen = dt.datetime.now()
    index = RegisterDate.index[RegisterDate['NOMBRE'] == User] 
    question  = input('Precione E para marcar su entrada\n Presione S para marcar su salida: ')
    if question == 'E':
        print(f'Su hora de entrada = {houropen}')
        RegisterDate.at[index,'Hora de Entrada'] = houropen
        RegisterDate.to_excel(ruta_Flujo ,index = False)
    elif question == 'S':
        print(f'Esta sera su hora de salida = {houropen}')
        RegisterDate.at[index,'Hora de Salida'] = houropen
        RegisterDate.to_excel(ruta_Flujo ,index = False)
    else: 
        print('Ingrese bien la clave')
    
    dict_RegisterDate = {}
    dict_RegisterDate['NOMBRE'] = User
    if User in list_(RegisterDate,'Nombre'):
        entry = dt.datetime.now()
        dict_RegisterDate['Hora de Entrada'] = entry
        
def pertain():
    global User
    #global add_New
    choose = input('Ingrese "E" Para Editar su Usuario\n Ingrese "M" para hora de Entrada o Salida: ')
    while choose == 'M':
        checktime()
        choose = input('Ingrese "E" Para Editar su Usuario\n Ingrese "M" para hora de Entrada o Salida: ')
    while choose == 'E':
        choose_value = input('Que deseas editar\n Ingrese "C" para el Correo\n Ingrese "D" para su direccion\n Ingrese "T" para su telefono\n Ingrese "P" para su Contraseña\n :  ')
        change_list = {'C':'CORREO','D':'DIRECCION','T':'TELEFONO','P':'CONTRASEÑA'}
        for x in change_list:
            if choose_value == x and choose_value != 'P':
                value_index = users.index[users['NOMBRE'] == User] 
                users.at[value_index,change_list[x]] = input('Nueva {}: '.format(change_list[x]))
                users.to_excel(ruta_Usuarios ,index = False)
                choose_value = input('Que deseas editar\n Ingrese "C" para el Correo\n Ingrese "D" para su direccion\n Ingrese "T" para su telefono\n Ingrese "P" para su Contraseña\n :  ')
            elif choose_value == 'P':
                value_index = workers.index[workers['NOMBRE'] == User] 
                workers.at[value_index,change_list[x]] = input('Nueva {}: '.format(change_list[x]))
                workers.to_excel(ruta_Usuarios ,index = False)
                choose_value = input('Que deseas editar\n Ingrese "C" para el Correo\n Ingrese "D" para su direccion\n Ingrese "T" para su telefono\n Ingrese "P" para su Contraseña\n :  ')
            elif choose_value == '':
                choose = input('Ingrese "E" Para Editar su Usuario\n Ingrese "M" para hora de Entrada o Salida: ')
            else:
                print('Esta opcion no la agreador el administrador o no existe')
                choose_value = input('Que deseas editar\n Ingrese "C" para el Correo\n Ingrese "D" para su direccion\n Ingrese "T" para su telefono\n Ingrese "P" para su Contraseña\n :  ')
    if choose == '':
        print('Volviendo al inicio......')
        User = input('Usuario: ')
        return User
        
def login():
    global User
    global users
    while User != '':
        if User in list_(workers,'NOMBRE'):
            pertain()
            Contraseña = input('Contraseña: ')
            if Contraseña in list_(workers,'CONTRASEÑAS'):
                #pertain()
                break            
        else: 
            _result2 = _register()
            if _result2 == True:
                User = input('Usuario: ')
            else:
                print('Finalizando programa')
                break
User = input('Usuario: ')
login()