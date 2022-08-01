import mysql.connector


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='Hadar21358',
                                         database='wellnesslife')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    # CREATE, UPDATE, DELETE
    if query_type == 'commit':
        connection.commit()
        return_value = True

    # READ
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value
