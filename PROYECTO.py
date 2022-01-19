import pandas as pd
import datetime as dt
ruta_Usuarios = 'Hospital.xlsx'
ruta_Passwords = 'USERS.xlsx'
ruta_Flujo = 'Horaentrada.xlsx'
workers = pd.read_excel(ruta_Passwords)
users = pd.read_excel(ruta_Usuarios)
RegisterDate = pd.read_excel(ruta_Flujo)

def overwrite_xlsx(df,dict,ruta):
    df = df.append(dict, ignore_index=True)
    df.to_excel(ruta, index = False)

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
            else:
                break
        overwrite_xlsx(users,dicc_User,ruta_Usuarios)
        overwrite_xlsx(workers,dict_userPassword,ruta_Passwords)
        _result = True
    else:
        _result = False
    return _result

def HoraTurno():
    global RegisterDate
    global User
    dict_RegisterDate = {}
    dict_RegisterDate['NOMBRE'] = User
    _filer = RegisterDate.loc(RegisterDate['NOMBRE'] == User)
    overwrite_xlsx(RegisterDate,dict_RegisterDate,ruta_Flujo)
    if 

        entry = dt.datetime.now()
        dict_RegisterDate['Hora de Entrada'] = f'{entry}'
    elif _filer[1] != '':
        timeExit = dt.datetime.now()
        dict_RegisterDate['Hora de Salida'] = f'{timeExit}'
    overwrite_xlsx(RegisterDate,dict_RegisterDate,ruta_Flujo)

#def pertain(User):
    
    #NombreFecha = NombreFecha.append(dict, ignore_index = True)

def login():
    global User
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
    
#User = input('Usuario: ')
y = RegisterDate.loc[RegisterDate['NOMBRE'] == 'Jean']
y = list(y)
print(y)
print(list(RegisterDate['Hora de Entrada']))