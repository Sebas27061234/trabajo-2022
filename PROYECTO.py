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
        workers.to_excel(ruta_Passwords ,index = False)
        users.to_excel(ruta_Usuarios ,index = False)
        print(workers)
        workers.at[1,'CONTRASEÑAS'] = input('Nueva contraseña: ')
        workers.to_excel(ruta_Passwords ,index = False)
        print(workers)
        _result = True
    else:
        _result = False
    return _result

def HoraTurno():
    global RegisterDate
    global User
    dict_RegisterDate = {}
    dict_RegisterDate['NOMBRE'] = User
    if User in list_(RegisterDate,'Nombre'):
        entry = dt.datetime.now()
        dict_RegisterDate['Hora de Entrada'] = entry
        

     

#def pertain():
    #NombreFecha = NombreFecha.append(dict, ignore_index = True)


def login():
    global User
    global users
    while User != '':
        if User in list_(workers,'NOMBRE'):
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
