import mysql.connector


def get_db():
    return mysql.connector.connect(
        host='informatica.iesquevedo.es',
        port=3333,
        ssl_disabled=False,
        ssl_verify_cert=False,
        ssl_verify_identity=False,
        user='root',
        password='1asir',
        database='mleyes'
    ) 