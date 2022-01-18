import pandas as pd
excel2 = {}
df_excel2 = pd.DataFrame(excel2)
df_excel2.to_excel('Users2.xlsx', index = False)

writter = pd.ExcelWriter('Users2.xlsx')

sa_dict = {'nombre' : ['a','z','c'], 'Apellido' : ['a','b','d']}
sa_df = pd.DataFrame(sa_dict)
sa_dict['nombre'] = 'S'
sa_df.to_excel(writter, 'Usuarios y Contraseñas', index = False)
writter.save()
writter.close()
print(sa_dict['nombre'])