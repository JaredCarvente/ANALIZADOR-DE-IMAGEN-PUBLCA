#THIS MODULE CONTAIN ALL FUNCTIONS NEEDED TO INTERACT WITH THE DATABASE

import psycopg2

def insert_new_candidate(cand_name,political_parties,conn):
    
    cur = conn.cursor()
    
    #SET THE QUERY TO INSERT THE CANDIDATE´S NAME
    insert_query = '''INSERT INTO candidate (c_name) VALUES (%s) ON CONFLICT (c_name) DO NOTHING; '''
    
    '''La cláusula ON CONFLICT es una característica específica de PostgreSQL y algunos otros sistemas de gestión 
    de bases de datos que permite controlar cómo se manejan los conflictos en una sentencia INSERT. Esta cláusula se utiliza para 
    definir el comportamiento que debe seguirse en caso de que una inserción genere un conflicto con restricciones de clave única o 
    restricciones de clave principal en una tabla.
    La cláusula ON CONFLICT se utiliza en combinación con una sentencia INSERT para especificar lo que debe suceder si se intenta insertar un 
    registro que entra en conflicto con registros existentes en la tabla. Los conflictos suelen ocurrir cuando intentas insertar un valor en una 
    columna que debe ser única y ya existe un valor igual en esa columna.'''


    # DEFINE THE VALUES TO BE INSERTED
    valores = (cand_name,)

    '''El motivo de usar (valor,) en lugar de simplemente valor se debe a que la función cur.execute de psycopg2 espera una secuencia 
    (como una tupla) de valores, incluso si solo estás insertando un valor. Para indicar que estás pasando un solo valor como una secuencia, 
    debes utilizar una coma después del valor, como (valor,). Esto crea una tupla con un solo elemento.
    Es decir, (valor,) es una tupla que contiene valor. Esta es la sintaxis requerida por psycopg2 para que pueda manejar los valores de
      manera segura. Si omites la coma y usas solo valor, psycopg2 podría interpretarlo de manera incorrecta.
    Así que, en resumen, se utiliza (valor,) para asegurarse de que psycopg2 interprete correctamente el valor como una tupla 
    con un solo elemento.'''
    
    # EXECUTE THE QUERY
    cur.execute(insert_query, valores)

    # COMMIT IS USED TO CONFIRM THE TRANSACTION 
    conn.commit()

    #QUERY TO INSERT THE CANDIDATES´S POLITICAL PARTIES IF NOT REGISTERED YET
    insert_query="INSERT INTO political_party (p_name) VALUES (%s) ON CONFLICT (p_name) DO NOTHING;"
    values=[]
    for party in political_parties:
        values.append((party,))
    #https://www.geeksforgeeks.org/python-psycopg2-insert-multiple-rows-with-one-query/
    cur.executemany(insert_query,values)
    conn.commit()

    #RELATE THE PREVIOUSLY REGISTERED PARTIES TO THE CANDIDATE
    update_candidate_party(cand_name,political_parties,conn)
    # Cierra el cursor y la conexión
    cur.close()


def update_candidate_party(candidate_name,political_party,conn):
    cur=conn.cursor()

    #GET CANDIDATE AND POLITICAL PARTIES ID´S
    cur.execute(f"SELECT party_id FROM political_party WHERE p_name IN {political_party}")
    parties_list=cur.fetchall()
    cur.execute(f"SELECT cand_id FROM candidate WHERE c_name ='{candidate_name}'")
    candidate_id=cur.fetchone()

    #RELATE CANDIDATE AND PARTIES THROUGH THEIR ID´S 
    update_list=[]
    for party in parties_list:
        update_list.append((candidate_id[0],party[0]))
    cur.executemany("INSERT INTO candidate_party (cand_id,party_id) VALUES (%s,%s)", update_list)
    conn.commit()


def get_candidate_id(candidate_name):
    conn=connect_to_db()
    cur=conn.cursor()
    cur.execute(f"SELECT cand_id FROM candidate WHERE c_name ='{candidate_name}'")
    candidate_id=cur.fetchone()[0]
    cur.close()
    conn.close()
    return candidate_id


def connect_to_db():

    conn = psycopg2.connect(
    dbname="political_analysis",
    user="postgres",
    password="sedena2023",
    host="localhost"  # THIS CAN BE CHANGED TO THE NAME OF THE DATA CONTAINING SERVER 
    )
    return conn

def upload_tweets(tweets_dict,candidate_name):
    conn=connect_to_db()
    cur=conn.cursor()
    query="INSERT INTO post(post_id,cand_id,author_id,collection_date,p_text,p_likes) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (post_id) DO NOTHING"
    values=tweets_dict[candidate_name]
    cur.executemany(query,values)
    conn.commit()
    cur.close()
    conn.close()

def check_if_candidate_in_db(*args):
    availability_status={} #THIS IS A DICTIONARY CONTAINING THE NAMES OF THE CANDIDATES,IF WILL HOLD A TRUE OR FALSE IN CASE OF BEING ON THE DATABASE OR NOT, RESPECTIVELY.  
    conn=connect_to_db()
    with conn.cursor() as cur:
        for name in args:
            name=name.upper()
            query=f"SELECT c_name FROM candidate WHERE c_name='{name}'"
            cur.execute(query)
            result=cur.fetchone()
            if result is not None:
                availability_status[name]=True
            else:
                availability_status[name]=False
                print(f"{name} is not in the database yet")

    conn.close()
    return availability_status

