
import pandas as pd
from time import time
import json

def dataFrame(courses):
    ''' Solo carga la columnas de cabecera del archivo
    '''
    # Cabecera
    courses_head = {}
    for course in courses:
        courses_head[course] = []

    #create empty dataframe
    df_marks = pd.DataFrame(courses_head)
    # print('Original DataFrame\n------------------ taking grade')
    # print(df_marks)
    return df_marks

def diccionario (data_read):
    ''' Carga todos los datos de los usuarios a un diccionario de diccionarios
    data = {
    'MHx/PC130442623': {
        ' HarvardX/CB22x/2013_Spring': 0,
        'OTRO/2014_Spring': 1.5
    },
    'MHx/PC130442567': {
        ' HarvardX/CB22x/2013_Spring': 0
    } 
    '''
    dicc = {}
    # for index, row in ten_users.iterrows():
    for index, row in data_read.iterrows():
        # print(row['userid_DI'], row['c2'])
        userid_DI  = row['userid_DI']
        if userid_DI in dicc:
            dicc[userid_DI][row['course_id']] = row['grade']
            # print ('Encontrado : ', userid_DI)
        else:
            dicc[userid_DI] = {}
            dicc[userid_DI][row['course_id']] = row['grade']

                # tmp_rating = {}
        # dicc[row['userid_DI']][row['course_id']] = row['grade']

    return dicc

def busqueda(df_marks, courses, data):
    ''' Realiza un filtro de los grados
    Ej: Si el grade es un ' ', un numero , o no llevo ese curso
    Y lo guarda en un archivo
    '''
    file = open("file.csv", "w")
    dict_items = data.items()

    # first_n = list(dict_items)[:1000]


    # for key, values in first_n:
    #     print ('hola ' ,key)
    for course in courses:
        # print ('hola ' ,key)
        file.write( ','+course )

    file.write( '\n' )

    # ten_users = users[:1000]
    print('lenght dictionary: ', len(dict_items))

    t= 0
    
    for user, values in dict_items:
    # for user, values in first_n:
        grade = ''
        row = ''
        # # new_row = {}
        if((t % 5000) == 0):
            print (t, user)
        # file.write( user )
        row = user
        # print (values)
        # val_user = data[user]
        min_course = 0
        for course in courses:
            
            if course in values:             # val_user
                grade = data[user][course]
            else:
                grade = -2                      # No llevo el curso

            if (grade == ' '):
                grade = -1
            if( float(grade) >= 0):
                min_course +=1
            row += ','+str(grade)

            # # new_row[course] = grade

        #append row to the dataframe
        # # new_row = pd.Series(data=new_row, name=user)

        # df_marks = df_marks.append(new_row, ignore_index=True)
        # # df_marks = df_marks.append(new_row, ignore_index=False)
        row += '\n'
        
        if(min_course >= 4):                # CANTIDAD DE CURSOS MINIMOS

            file.write( row )

        t+=1
    
    print ('Archivo guardado con exito!')
    return 1

def tiempo_ejecucion(tiempo_final, tiempo_inicial):
    tiempo_ejecucion = tiempo_final - tiempo_inicial

    return tiempo_ejecucion

if __name__ == '__main__':

    data =  {}
    # software carpentry url for data_read data
    data_read_csv = 'HXPC13_DI_v3_11-13-2019.csv'
    # load the data with pd.read_csv
    data_read = pd.read_csv(data_read_csv)
    data_read = data_read.fillna(value=-1)              # lo llevo pero dejo vacio el grade

    courses = data_read['course_id'].unique()
    # users = data_read['userid_DI'].unique().tolist()

    
    
    df_marks = dataFrame(courses)

    tiempo_inicial = time() 
    # n_users = data_read[:10]
    data = diccionario(data_read)
    print('El usuario buscado', data['MHxPC130451711'])
    tiempo_final = time() 

    print ('El tiempo de diccionario fue: ',tiempo_ejecucion(tiempo_final, tiempo_inicial)) #En segundos


    tiempo_inicial = time() 
    dataFrameFilled = busqueda(df_marks, courses , data)
    tiempo_final = time() 

    
    print ('El tiempo de ejecucion fue: ',tiempo_ejecucion(tiempo_final, tiempo_inicial )) #En segundos


    # dataFrameFilled.to_csv('Untitled.csv')
