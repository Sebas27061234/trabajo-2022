import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import webbrowser
from pyparsing import col
import seaborn as sns
ruta_Usuarios = 'Hospital.xlsx'
ruta_UsuariosAdmin = 'CONTROLCENTER.xlsx'
ruta_Patients = 'Base_datos_pacientes.xlsx'
ruta_reception = 'RECEPCION.xlsx'
users = pd.read_excel(ruta_Usuarios)
admin = pd.read_excel(ruta_UsuariosAdmin)
reception = pd.read_excel(ruta_Patients)
receptionUser = pd.read_excel(ruta_reception)
passwordRegistration = 'PythonBasico2022pedrorotta'

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
    User_Now = input('Presione R si desea registrase: ')
    if User_Now == 'R':
        dict_User = {}
        columnas_list = columns(users)
        for Datos in columnas_list:
            if Datos != 'ESTADO' and Datos != 'SUELDO AL MES' and Datos != 'Hora de Entrada' and Datos != 'Hora de Salida' and Datos != 'MEDICO':
                dict_User[Datos] = input(f'Inserta {Datos}: ')
            elif Datos == 'MEDICO':
                dict_User[Datos] = 'Dr' + ' '+ dict_User['NOMBRE'] +' ' + dict_User['APELLIDO']
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

def addPatients():
    global User
    global _password
    global reception
    global users
    NombreExistencia = input('Ingrese el nombre del paciente\nENTER para regresar a inicio: ')
    list_NombreExistencia = list_(reception,'NOMBRE')
    if NombreExistencia in list_NombreExistencia:
        print('El paciente ya esta registrado')
        df_PacienteUnico = reception.loc[reception['NOMBRE']== NombreExistencia]
        format_html(df_PacienteUnico,'PACIENTE')
    elif NombreExistencia not in list_NombreExistencia and NombreExistencia !='':
        pregunt = input('Inserte "E" para agregar un nuevo usuario\nENTER para volver a inicio: ')
        if pregunt == 'E':
            dict_newPatients = {}
            columnas_list = columns(reception)
            for Datos in columnas_list:
                if Datos != 'FECHA DE INGRESO':
                    _dato = input(f'Inserta {Datos}: ')
                    if _dato != '':
                        dict_newPatients[Datos] = _dato
                    elif _dato == '':
                        print('No has ingresado nada ingrese de nuevo')
                        _dato = input(f'Inserta {Datos}: ')
                elif Datos == 'FECHA DE INGRESO':
                    hourdate = dt.datetime.now()
                    print(f'Su hora de entrada = {hourdate}')
                    dict_newPatients[Datos] = hourdate
            reception = reception.append(dict_newPatients , ignore_index= True )
            reception.to_excel(ruta_Patients ,index = False)
        elif pregunt == '':
            User = input('Usuario: ')
            if User != '':
                _password = input('Ingresa tu Contraseña: ')
            return login()
    else:
        User = input('Usuario: ')
        if User != '':
             _password = input('Ingresa tu Contraseña: ')
        return login()

def editar():
    global User
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
                pregunt = input('Ingrese "O" si desea ver solo la informacion de un solo trabaajor\nIngrese "V" si desea ver toda la informacion de los trabajodores\nIngrese "E" si desea editar la informacion de los trabajodores\n Ingrese "A" si desea analizar: ')
        return pregunt

def format_html(df,x):
    df.to_html(f'{x}.html',index=None,header=True)  
    file = open(f'{x}.html', 'a')
    content = '''
    <head>
        <link rel="stylesheet" href="estilos.css">
    </head>'''
    file.write(content)
    file.close()
    webbrowser.open(f'{x}.html',new=0, autoraise=True)

def addreception():
    global receptionUser
    Columnas = columns(receptionUser)
    dict_NewRegister = {}
    for Datos in Columnas:
        dict_NewRegister[Datos]= input(f'Inserta {Datos}: ')
    receptionUser = receptionUser.append(dict_NewRegister,ignore_index=True) 
    receptionUser.to_excel(ruta_reception,index=False)  

def look_User():
    global users
    list_columns = columns(users)
    filtroWorker =input('Ingrese "C" para filtrar por columna\nIngrese "N" por trabajador: ') 
    if filtroWorker == 'C':
        list__columns = []
        print('Escoja una columna {}'.format(list_columns))
        columna = input('Nombre de la Columna: ')
        if columna in list_columns:
            list__columns.append(columna)
            one_User = pd.unique(users[columna])
            _Data = pd.DataFrame(one_User,columns= list__columns)
            format_html(_Data,'Tablaone')
    elif filtroWorker == 'N':
        nameWorker = input('Ingrese Nombre: ')
        one_User = users.loc[users['NOMBRE'] == nameWorker ]
        format_html(one_User,'Tablaone')

def EdadXSueldo():
    list_G = users['SUELDO AL MES'].tolist()
    edad = users['EDAD'].tolist()
    tamaño = 50*np.array(edad)
    fig,ax2 = plt.subplots()
    ax2.scatter(edad,list_G,s=tamaño,alpha=0.5, cmap='viridis')
    plt.xlabel('EDAD')
    plt.ylabel('SUELDO')
    plt.title('Edad por Sueldo')
    plt.show()

def GeneroXEdad():
        list_G = users['SUELDO AL MES'].tolist()
        especialidad = users['ESPECIALIDAD'].tolist()
        plt.style.use('_mpl-gallery-nogrid')
        x = list_G
        especialidad = especialidad
        colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(x)))
        fig, ax = plt.subplots()
        ax.pie(x, labels=especialidad,autopct="%0.1f %%",radius=1)
        plt.show()

def PromSueldoG():
    list_G = users['SUELDO AL MES'].tolist()
    promedioG = np.mean(list_G)
    sns.set_theme(style="whitegrid")
    g = sns.PairGrid(users, y_vars="SUELDO AL MES",
                    x_vars=["GENERO (Masculino/Femenino) "],
                    height=5, aspect=.5)
    g.map(sns.pointplot, scale=1.3, errwidth=4, color="xkcd:plum")
    g.set(ylim=(promedioG-1000, promedioG+1000))
    sns.despine(fig=g.fig, left=True)
    plt.show()

def SueldoxTrabajador():
    sns.set_theme(style="whitegrid")
    g = sns.catplot(
        data=users, kind="bar",
        x="NOMBRE", y="SUELDO AL MES", hue="GENERO (Masculino/Femenino) ",
        ci="sd", palette="dark", alpha=.6, height=6)
    g.despine(left=True)
    g.set_axis_labels("Trabajadores", "Sueldo")
    g.legend.set_title("")
    plt.show()

def SueldoXEspecialida():
    list_G = users['SUELDO AL MES'].tolist()
    especialidad = users['ESPECIALIDAD'].tolist()
    plt.style.use('_mpl-gallery-nogrid')
    x = list_G
    especialidad = especialidad
    colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(x)))
    fig, ax = plt.subplots()
    ax.pie(x, labels=especialidad,autopct="%0.1f %%",radius=1)
    plt.show()

def DosisXEdad():
    edad = users['EDAD'].tolist()
    dosis = users['DOSIS DE VACUNA COVID'].tolist()
    plt.style.use('_mpl-gallery-nogrid')
    x = dosis
    edad = edad
    fig, ax = plt.subplots()
    ax.pie(x, labels=edad,autopct="%0.1f %%",radius=1)
    plt.show()

def analisisDatos():
    pregunt = input('')
    if pregunt == '':
        PromSueldoG()

def analisisDatosWorkers():
    pregunt = input('')
    if pregunt == (''):
        x=3

def _admin():
    global receptionUser
    global reception
    global _password
    global User
    global pregunt
    global users
    pregunt = input('Ingrese "O" si desea ver solo la informacion de un trabajador\nIngrese "V" si desea ver toda la informacion\nIngrese "E" si desea editar la informacion\nIngrese "A" si desea analizar datos\nENTER para cerrar seccion: ')
    if pregunt == 'V':
        infoUser = input('Ingrese "T" para ver toda la informacion de los trabajadores\nIngrese "P" para ver toda la informacion de los Pacientes\nIngrese "R" para ver todos los ususarios de recepcion: ')
        if infoUser == 'T':
            format_html(users,'Tabla')
        elif infoUser == 'P':
            format_html(reception,'TablaPacientes')
        elif infoUser == 'R':
            format_html(receptionUser,'TablarRecepcion')
    elif pregunt == 'E':
        pregunt_3 = input('Inserte "U" para editar informacion de un trabajador\nInserte "R" para agregar una nueva recepcion: ')
        if pregunt_3 == 'U':
            edit_Users()
        elif pregunt_3 == 'R':
             addreception()
    elif pregunt == 'A':
        pregunt_2 = input('Ingrese "P" para analizar datos de los pacientes\nIngrese "T" si desea analizar datos de los trabajadores: ')
        if pregunt_2 == 'T':
            analisisDatos()
        elif pregunt_2 == 'P':
            analisisDatosWorkers()
    elif pregunt == 'O':
        look_User()
    elif pregunt == '':
        print('Retornando a INICIO....')
        User = input('Usuario: ')
        _password = input('Ingresa tu Contraseña: ')
        return login()

def login():
    global receptionUser
    global _password
    global passwordRegistration
    global User
    global users
    index_User = users.index[users['NOMBRE'] == User]
    index_Userr = receptionUser.index[receptionUser['NOMBRE'] == User]
    while User != '':
        if User in list_(users,'NOMBRE') and _password == users.at[index_User[0],'CONTRASEÑAS']:
            pertain()
        elif User in list_(admin,'NOMBRE') and _password == admin.at[0,'CONTRASEÑAS']:
            _admin()
        elif User in list_(receptionUser,'NOMBRE') and _password == receptionUser.at[index_Userr[0],'CONTRASEÑAS']:
            addPatients()
        elif User not in list_(users,'NOMBRE') and User not in list_(admin,'NOMBRE') and User not in list_(receptionUser,'NOMBRE'):
            print('Para registrarse como trabajador ingrese la contraseña que le ha proporcinado la empresa')
            password2 = input('Contraseña: ')
            if password2 == passwordRegistration:
                _result2 = _register()
                if _result2 == True:
                    User = input('Usuario: ')
                    _password = input('Ingresa tu Contraseña: ')
                else:
                    print('Finalizando programa')
            else:
                print('Contraseña Incorrecta\nFinalizando Programa....')
                break
        else:
            print('Contraseña Incorrecta\nFinalizando Programa....')
            break
    if User == '':
        print('Programa terminado')
        

User = input('Usuario: ')
if User != '':
    _password = input('Ingresa tu Contraseña: ')
login()
