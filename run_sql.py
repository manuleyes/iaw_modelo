import mysql.connector

# Conectar sin especificar BD primero
conn = mysql.connector.connect(
    host='informatica.iesquevedo.es',
    port=3333,
    ssl_disabled=False,
    ssl_verify_cert=False,
    ssl_verify_identity=False,
    user='root',
    password='1asir'
)

cursor = conn.cursor()

# Leer y ejecutar el SQL
with open('alumnos.sql', 'r') as f:
    sql_script = f.read()
    
# Ejecutar cada comando del script
for statement in sql_script.split(';'):
    statement = statement.strip()
    if statement:
        cursor.execute(statement)
        
conn.commit()
cursor.close()
conn.close()

print("Base de datos creada correctamente!")
