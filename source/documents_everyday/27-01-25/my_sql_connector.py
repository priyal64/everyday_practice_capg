import mysql.connector
def connect_db():
    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        database='mydatabase'
    )
    print('db connected')
    return connection
def main():
    connect_db()
main()