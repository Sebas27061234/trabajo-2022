from operator import index
import pandas as pd
import datetime as dt
ruta_Usuarios = 'Hospital.xlsx'
users = pd.read_excel(ruta_Usuarios)

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
    print('El usuario {} no existe'.format(User))
    User_Now = input('Presione R si desea registrase: ')
    if User_Now == 'R':
        dict_User = {}
        columnas_df = columns(users)
        for Datos in columnas_df:
            if Datos != 'ESTADO' and Datos != 'SUELDO' and Datos != 'Hora de Entrada' and Datos != 'Hora de Salida':
                dict_User[Datos] = input(f'Inserta {Datos}: ')
            continue
        users = users.append(dict_User , ignore_index= True )
        users.to_excel(ruta_Usuarios ,index = False)
        _result = True
    else:
        _result = False
    return _result

def checktime():
    global users
    global User
    houropen = dt.datetime.now()
    index = users.index[users['NOMBRE'] == User] 
    question  = input('Precione E para marcar su entrada\n Presione S para marcar su salida: ')
    if question == 'E':
        print(f'Su hora de entrada = {houropen}')
        users.at[index,'Hora de Entrada'] = houropen
        users.to_excel(ruta_Usuarios,index = False)
    elif question == 'S':
        print(f'Esta sera su hora de salida = {houropen}')
        users.at[index,'Hora de Salida'] = houropen
        users.to_excel(ruta_Usuarios ,index = False)
    else: 
        print('Ingrese bien la clave')
    return True
        
def pertain():
    global User
    global users
    #global add_New
    choose = input('Ingrese "E" Para Editar su Usuario\n Ingrese "M" para hora de Entrada o Salida\n Si quiere volver al inicio no ingrese nada\n: ')
    while choose == 'M':
        checktime()
        choose = input('Ingrese "E" Para Editar su Usuario\n Ingrese "M" para hora de Entrada o Salida: ')
    while choose == 'E':
        choose_value = input('Que deseas editar\n Ingrese "C" para el Correo\n Ingrese "P" para su direccion\n Ingrese "T" para su telefono\n Ingrese "P" para su Contraseña\n :  ')
        change_list = {'C':'CORREO','D':'DIRECCION','T':'TELEFONO','P':'CONTRASEÑA'}
        while choose_value in list(change_list.keys()):
            if choose_value != '':
                value_index = users.index[users['NOMBRE'] == User] 
                users.at[value_index,change_list[choose_value]] = input('Nueva {}: '.format(change_list[choose_value]))
                users.to_excel(ruta_Usuarios ,index = False) 
                choose_value = input('Que deseas editar\n Ingrese "C" para el Correo\n Ingrese "D" para su direccion\n Ingrese "T" para su telefono\n Ingrese "P" para su Contraseña\n :  ')
        if choose_value == '':
            choose = input('La informacion que desea editar no ha sido habilitada o no existe.\nIngrese M si desea salir de editar usuario: ')
    if choose == '':
        print('Volviendo al inicio......')
        User = input('Usuario: ')
        return User
        
def login():
    global User
    global users
    while User != '':
        if User in list_(users,'NOMBRE'):
                pertain()
        else: 
            _result2 = _register()
            if _result2 == True:
                User = input('Usuario: ')
            else:
                print('Finalizando programa')
                break

User = input('Usuario: ')
login()
