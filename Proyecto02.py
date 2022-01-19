import pandas as pd
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
                    dict_userPassword[Datos] = input('Ingresa una contraseña: ')
                    workers.append(dict_userPassword , ignore_index=True)
                    workers.to_excel()
            else:
                break
        users.append(dicc_User , ignore_index= True )
        _result = True
        users.to_excel()
    else:
        _result = False
    workers.to_excel("USERS.xlsx",index=False)
    users.to_excel('Hospital.xlsx',index=False)
    return _result



def login():
    global users
    global User
    while User != '':
        if User in list_(workers,'NOMBRE'):
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