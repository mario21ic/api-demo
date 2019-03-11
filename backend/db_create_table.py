import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
   connection = mysql.connector.connect(host='db',
                             database='api_db',
                             user='root',
                             password='myclave')
   sql_insert_query = "CREATE TABLE personaje (id INT AUTO_INCREMENT, first_name VARCHAR(200) NOT NULL, last_name VARCHAR(200) NOT NULL, twitter VARCHAR(20) NULL, PRIMARY KEY (id)) ENGINE=INNODB"
   cursor = connection.cursor()
   result  = cursor.execute(sql_insert_query)
   connection.commit()
   print ("Record inserted successfully")

except mysql.connector.Error as error :
    connection.rollback() #rollback if any exception occured
    print("Failed inserting record {}".format(error))

finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

