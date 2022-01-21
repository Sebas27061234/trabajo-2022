import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import webbrowser
import seaborn as sns
ruta_Usuarios = 'Hospital.xlsx'
ruta_UsuariosAdmin = 'CONTROLCENTER.xlsx'
users = pd.read_excel(ruta_Usuarios)
admin = pd.read_excel(ruta_UsuariosAdmin)
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
        columnas_df = columns(users)
        for Datos in columnas_df:
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

def look_User():
    global users
    list_columns = columns(users)
    filtroWoker =input('Ingrese "C" para filtrar por columna\nIngrese "N" por trabajador: ') 
    if filtroWoker == 'C':
        list__columns = []
        print('Escoja una columna {}'.format(list_columns))
        columna = input('Nombre de la Columna: ')
        if columna in list_columns:
            list__columns.append(columna)
            one_User = pd.unique(users[columna])
            _Data = pd.DataFrame(one_User,columns= list__columns)
            format_html(_Data,'Tablaone')
    elif filtroWoker == 'N':
        nameWoker = input('Ingrese Nombre: ')
        one_User = users.loc[users['NOMBRE'] == nameWoker ]
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
        # make data
        x = list_G
        especialidad = especialidad
        colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(x)))

        # plot
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
        ci="sd", palette="dark", alpha=.6, height=6
    )
    g.despine(left=True)
    g.set_axis_labels("Trabajadores", "Sueldo")
    g.legend.set_title("")
    plt.show()

def SueldoXEspecialida():
    list_G = users['SUELDO AL MES'].tolist()
    especialidad = users['ESPECIALIDAD'].tolist()
    plt.style.use('_mpl-gallery-nogrid')
    # make data
    x = list_G
    especialidad = especialidad
    colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(x)))

    # plot
    fig, ax = plt.subplots()
    ax.pie(x, labels=especialidad,autopct="%0.1f %%",radius=1)

    plt.show()

def DosisXEdad():
    edad = users['EDAD'].tolist()
    dosis = users['DOSIS DE VACUNA COVID'].tolist()
    plt.style.use('_mpl-gallery-nogrid')
    # make data
    x = dosis
    edad = edad
    #ploty
    fig, ax = plt.subplots()
    ax.pie(x, labels=edad,autopct="%0.1f %%",radius=1)

    plt.show()



def analisisDatos():
    pregunt = input('')
    if pregunt == '':
        PromSueldoG()


def _admin():
    global _password
    global User
    global pregunt
    global users
    pregunt = input('Ingrese "O" si desea ver solo la informacion de un solo trabaajor\nIngrese "V" si desea ver toda la informacion de los trabajodores\nIngrese "E" si desea editar la informacion de los trabajodores\n Ingrese "A" si desea analizar: ')
    if pregunt == 'V':
        format_html(users,'Tabla')
    elif pregunt == 'E':
        edit_Users()
    elif pregunt == 'A':
        analisisDatos()
    elif pregunt == 'O':
        look_User()
    elif pregunt == '':
        print('Clave no correcta.....\nRetornando a INICIO....')
        User = input('Usuario: ')
        _password = input('Ingresa tu Contraseña: ')
        return login()

def login():
    global _password
    global passwordRegistration
    global User
    global users
    index_User = users.index[users['NOMBRE'] == User]
    while User != '':
        if User in list_(users,'NOMBRE') and _password == users.at[index_User[0],'CONTRASEÑAS']:
            pertain()
        elif User in list_(admin,'NOMBRE') and _password == admin.at[0,'CONTRASEÑAS']:
            _admin()
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
            else:
                print('Contraseña Incorrecta\nFinalizando Programa....')
                break
    if User == '':
        print('Programa terminado')
        

User = input('Usuario: ')
if User != '':
    _password = input('Ingresa tu Contraseña: ')
login()
