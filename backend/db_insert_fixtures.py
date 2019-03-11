import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
   connection = mysql.connector.connect(host='db',
                             database='api_db',
                             user='root',
                             password='myclave')
   sql_insert_query = "insert into `personaje` values(NULL, 'Jill', 'Valentine', 'valentine')"
   sql_insert_query = "insert into `personaje` values(NULL, 'Leon', 'Kenedy', 'leonevil')"
   cursor = connection.cursor()
   result  = cursor.execute(sql_insert_query)
   connection.commit()
   print ("Record inserted successfully")

except mysql.connector.Error as error :
    connection.rollback()
    print("Failed inserting record {}".format(error))

finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

