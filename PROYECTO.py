from operator import index
import pandas as pd
#ruta_Usuarios = "USERS.xlsx"
#ruta_Datos = 'Hospital.xlsx'
#workers = pd.read_excel(ruta_Usuarios)
#users = pd.read_excel(ruta_Datos)
workers_columns = ['NOMBRE','CONTRASEÑAS']
users_columns = ['ID','DNI', 'NOMBRE', 'APELLIDO', 'EDAD', 'GENERO',
                'VACUNA COVID','DIRECCION','CORREO','TELEFONO', 'AREA DE TRABAJO','SUELDO', 'ESTADO']
workers = pd.DataFrame(columns = workers_columns)
users = pd.DataFrame(columns = users_columns)

excel2 = {}
df_excel2 = pd.DataFrame(excel2)
df_excel2.to_excel('Users2.xlsx', index = False)

writter = pd.ExcelWriter('Users2.xlsx')

def columns(df):
    columnas = df.columns
    list_columnas = list(columnas)
    return list_columnas

def list_(df,nombre):
    filas = pd.unique(df[nombre])
    list_filas = list(filas)
    return list_filas

def _register():
    global writter
    global users
    global User
    global workers
    print('El usuario {} no existe'.format(User))
    User_Now = input('Presione R si desea registrase: ')
    if User_Now == 'R':
        dict_User = {'ID':'' ,'DNI': '', 'NOMBRE':'' , 'APELLIDO':'' , 'EDAD':'' , 'GENERO':'',
                'VACUNA COVID':'' ,'DIRECCION':'' ,'CORREO':'' ,'TELEFONO':'' , 'AREA DE TRABAJO':'' ,'SUELDO': '', 'ESTADO':'' }
        dict_userPassword = {'NOMBRE':'' ,'CONTRASEÑAS':'' }
        columnas_df = columns(users)
        for Datos in columnas_df:
            if Datos != 'ESTADO' and Datos != 'SUELDO':
                dict_User[Datos]=(input(f'Inserta {Datos}: '))
                if Datos == 'NOMBRE':
                    dict_userPassword['NOMBRE'] = dict_User[Datos]
                    dict_userPassword['CONTRASEÑAS'] = (input('Ingresa una contraseña: '))
                    df_userPassword = pd.DataFrame.from_dict(dict_userPassword, orient='index')
                    df_userPassword.to_excel(writter, 'Usuarios y Contraseñas', index = False)
            else:
                break
        df_User = pd.DataFrame.from_dict(dict_User, orient='index')
        _result = True
        df_User.to_excel(writter,'Datos de usuarios', index = False)
        writter.save()
        writter.close()
        print(dict_User)
        print(dict_userPassword)
    else:
        _result = False
    return _result


def login():
    global users
    global User
    while User != '':
        if User in list_(workers,'NOMBRE'):
            print('HOLA')#pertain()
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

