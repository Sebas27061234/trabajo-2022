import pandas as pd
import datetime as dt
ruta_Usuarios = "USERS.xlsx"
ruta_Datos = 'Hospital.xlsx'
workers = pd.read_excel(ruta_Usuarios)
users = pd.read_excel(ruta_Datos)

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
        dicc_User = {}
        dict_userPassword = {}
        columnas_df = columns(users)
        for Datos in columnas_df:
            if Datos != 'ESTADO' and Datos != 'SUELDO':
                dicc_User[Datos] = input(f'Inserta {Datos}: ')
                if Datos == 'NOMBRE':
                    dict_userPassword['NOMBRE'] = dicc_User['NOMBRE']
                    dict_userPassword['CONTRASEÑAS'] = input('Ingresa una contraseña: ')
                    workers = workers.append(dict_userPassword , ignore_index=True )
            else:
                break
        users = users.append(dicc_User , ignore_index= True )
        _result = True
    else:
        _result = False
    return _result

def HoraTurno():
     horaEntrada = dt.datetime.now()
     

#def pertain(User):
    
    


def login():
    global users
    while User != '':
        if User in list_(workers,'NOMBRE'):
            #pertain(User)
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
