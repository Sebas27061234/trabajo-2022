from csv import list_dialects
from pydoc import doc
import pandas as pd
import datetime as dt
import webbrowser
ruta_Usuarios = 'Hospital.xlsx'
ruta_UsuariosAdmin = 'CONTROLCENTER.xlsx'
ruta_patients = 'Base_datos_pacientes.xlsx'
ruta_reception = 'Reception.xlsx'
users = pd.read_excel(ruta_Usuarios)
admin = pd.read_excel(ruta_UsuariosAdmin)
patients = pd.read_excel(ruta_patients)
reception = pd.read_excel(ruta_reception)
passwordRegistration = 'PythonBasico2022pedrorotta'

def columns(df):
    columnas = df.columns
    list_columnas = list(columnas)
    return list_columnas

def list_(df,nombre):
    filas = pd.unique(df[nombre])
    list_filas = list(filas)
    return list_filas

def format_html(df):
    df.to_html('Tabla.html',index=None,header=True)
    webbrowser.open('Tabla.html', new=0, autoraise=True)

def _reception():
    global users
    global patients
    dict_patients = {}
    _patients = input('Ingrese "S" para agregar un nuevo paciente\nIngrese "C" para crear una cita medica\n..De ENTER si quiere retornar: ')
    if _patients == 'S':
        columnas_df = columns(patients)
        for Datos in columnas_df:
            if Datos != 'MEDICO' and Datos != 'ESPECIALIDAD' and Datos !='FECHA' and Datos !='HORA CITA':
                dict_patients[Datos] = input(f'Inserta {Datos}: ')
        patients = patients.append(dict_patients,ignore_index=True)
        _patients = input('De ENTER si quiere retornar: ')
    elif _patients == 'C':
        DNI = int(input('Ingrese DNI del Paciente: '))
        columnas_df = columns(patients)
        if DNI in list_(patients,'DNI'):
            lis_t = []
            for Datos in columnas_df:
                if Datos =='FECHA' or Datos =='HORA CITA':
                    dict_patients[Datos] = input(f'Inserta {Datos}: ')
                elif  Datos == 'ESPECIALIDAD':
                    _index = patients.index[patients['DNI'] == DNI]
                    list_Espec = list_(users,'ESPECIALIDAD')
                    print('Solo hay doctores especializados en = {}'.format(list_Espec))
                    espec = input('Que especializacion desea: ')
                    Doct_ = users.loc[users['ESPECIALIDAD'] == f'{espec}']
                    print(Doct_)
                    #lis_doc = list_(Doct_,'MEDICO')
                    #print('Estos son doctores que hay en especialización {}'.format(lis_doc))
                    doc = input('Cual doctor: ')
                    lis_t.append(doc)
                    patients.at[int(_index[0]),'ESPECIALIDAD'] = espec
                    patients.at[int(_index[0]),'MEDICO'] = doc
                    patients.to_excel(ruta_patients,index = False) 
    elif _patients == '':
        User = input('Usuario: ')
        if User != '':
            _password = input('Ingresa tu Contraseña: ')
        return login()
    patients.to_excel(ruta_patients,index=False)

def _register():
    global users
    global User
    User_Now = input('Presione R si desea registrase: ')
    if User_Now == 'R':
        dict_User = {}
        columnas_df = columns(users)
        for Datos in columnas_df:
            if Datos != 'ESTADO' and Datos != 'SUELDO' and Datos != 'Hora de Entrada' and Datos != 'Hora de Salida' and Datos != 'MEDICO':
                dict_User[Datos] = input(f'Inserta {Datos}: ')
            elif Datos == 'MEDICO':
                dict_User[Datos] = 'Dr.' + ' '+ dict_User['NOMBRE'] +' ' + dict_User['APELLIDO']
            continue
        users = users.append(dict_User , ignore_index= True )
        users.to_excel(ruta_Usuarios ,index = False)
        _result = True
    else:
        _result = False
    return _result

def checktime():
    global choose
    global users
    global User
    houropen = dt.datetime.now()
    index = users.index[users['NOMBRE'] == User] 
    question  = input('Precione E para marcar su entrada\n Presione S para marcar su salida: ')
    if question == 'E':
        print(f'Su hora de entrada = {houropen}')
        users.at[index[0],'Hora de Entrada'] = houropen
        users.to_excel(ruta_Usuarios,index = False)
    elif question == 'S'and users.at[index[0],'Hora de Entrada'] != '':
        print(f'Esta sera su hora de salida = {houropen}')
        users.at[index[0],'Hora de Salida'] = houropen
        users.to_excel(ruta_Usuarios ,index = False)
    else: 
        print('No ha ingresado la hora de entrada o a ingresado mal la clave')
    choose = input('Ingrese "E" Para Editar su Usuario\n Ingrese "M" para hora de Entrada o Salida\n Si quiere volver al inicio no ingrese nada\n: ')
    return choose

def editar():
    global choose
    choose_value = input('Que deseas editar\n Ingrese "C" para el Correo\n Ingrese "P" para su direccion\n Ingrese "T" para su telefono\n Ingrese "P" para su Contraseña\n :  ')
    change_list = {'C':'CORREO','D':'DIRECCION','T':'TELEFONO','P':'CONTRASEÑAS'}
    while choose_value in list(change_list.keys()):
        if choose_value != '':
            value_index = users.index[users['NOMBRE'] == User] 
            users.at[value_index,change_list[choose_value]] = input('Nueva {}: '.format(change_list[choose_value]))
            users.to_excel(ruta_Usuarios ,index = False) 
            choose_value = input('Que deseas editar\n Ingrese "C" para el Correo\n Ingrese "D" para su direccion\n Ingrese "T" para su telefono\n Ingrese "P" para su Contraseña\n :  ')
        elif choose_value == '':
            choose = input('La informacion que desea editar no ha sido habilitada o no existe.\nIngrese M si desea salir de editar usuario: ')
    return choose
        
def pertain():
    global _password
    global User
    global users
    global choose
    #global add_New
    choose = input('Ingrese "E" Para Editar su Usuario\n Ingrese "M" para hora de Entrada o Salida\n Si quiere volver al inicio no ingrese nada\n: ')
    if choose == 'M':
        checktime()
    elif choose == 'E':
        editar()
    elif choose == '':
        print('Volviendo al inicio......')
        User = input('Usuario: ')
        if User != '':
            _password = input('Ingresa tu Contraseña: ')
    return login()

def edit_Users():
    global pregunt
    global users
    nombre = input('Ingrese nombre del usuario: ')
    if nombre != '':
        list_modfi = columns(users)[10:13]
        print('Esta es la lista de los datos que solo puede modificar {}'.format(list_modfi))
        gg = input(f'Que columna desea modificar: ')
        while gg in list_modfi:
            if gg != '':
                value_index = users.index[users['NOMBRE'] == nombre] 
                users.at[value_index[0],gg] = input('Nueva {}: '.format(gg))
                users.to_excel(ruta_Usuarios ,index = False) 
                gg = input(f'Que columna desea modificar: ')
            elif gg == '':
                    pregunt = input('Ingrese "V" si desea ver toda la informacion de los trabajodores\nIngrese "E" si desea editar la informacion de los trabajodores\n Ingrese "A" si desea analizar: ')
        return pregunt

def format_html(df):
    df.to_html('Tabla.html',index=None,header=True)  
    file = open('Tabla.html', 'a')
    content = '''
    <head>
        <link rel="stylesheet" href="estilos.css">
    </head>'''
    file.write(content)
    file.close()
    webbrowser.open('Tabla.html',new=0, autoraise=True)

def analisisDatos():
    print('hola')

def _admin():
    global _password
    global User
    global pregunt
    global users
    pregunt = input('Ingrese "V" si desea ver toda la informacion de los trabajodores\nIngrese "E" si desea editar la informacion de los trabajodores\n Ingrese "A" si desea analizar: ')
    if pregunt == 'V':
        format_html(users)
    elif pregunt == 'E':
        edit_Users()
    elif pregunt == 'A':
        analisisDatos()
    elif pregunt == '':
        print('Clave no correcta.....\nRetornando a INICIO....')
        User = input('Usuario: ')
        _password = input('Ingresa tu Contraseña: ')
        return login()

def login():
    global reception
    global _password
    global passwordRegistration
    global User
    global users
    index_User = users.index[users['NOMBRE'] == User]
    index_User2 = reception.index[reception['NOMBRE'] == User]
    while User != '':
        if User in list_(users,'NOMBRE') and _password == users.at[index_User[0],'CONTRASEÑAS']:
            pertain()
        elif User in list_(admin,'NOMBRE') and _password == admin.at[0,'CONTRASEÑAS']:
            _admin()
        elif User in list_(reception, 'NOMBRE') and _password == reception.at[index_User2[0],'CONTRASEÑAS']:
            _reception()
        else:
            print('Para registrarse como trabajador ingrese la contraseña que le ha proporcinado la empresa')
            password2 = input('Contraseña: ')
            if password2 == passwordRegistration:
                _result2 = _register()
                if _result2 == True:
                    User = input('Usuario: ')
                    _password = input('Ingresa tu Contraseña: ')
                else:
                    print('Finalizando programa')
            elif password2 != '':
                print('Contraseña Incorrecta\nFinalizando Programa....')
    if User == '':
        print('Programa terminado')
        

#User = input('Usuario: ')
#if User != '':
#    _password = input('Ingresa tu Contraseña: ')
#login()
#
_reception()