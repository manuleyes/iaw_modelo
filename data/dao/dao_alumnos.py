from data.modelo.database import get_db


class DaoAlumnos:

    def get_all(self) -> list:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()
        cursor.close()
        db.close()
        return alumnos

    def get_aprobados(self) -> list:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM alumnos WHERE nota1 >= 5 AND nota2 >= 5 AND nota3 >= 5"
        )
        alumnos = cursor.fetchall()
        cursor.close()
        db.close()
        return alumnos

    def filtrar_por_media(self, numero: float) -> list:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM alumnos WHERE (nota1 + nota2 + nota3) / 3 > %s",
            (numero,)
        )
        alumnos = cursor.fetchall()
        cursor.close()
        db.close()
        return alumnos

    def cambiar_nombre(self, alumno_id: int, nuevo_nombre: str) -> int:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE alumnos SET nombre = %s "
            "WHERE id = %s AND nota1 >= 5 AND nota2 >= 5 AND nota3 >= 5",
            (nuevo_nombre, alumno_id)
        )
        db.commit()
        filas = cursor.rowcount
        cursor.close()
        db.close()
        return filas

    def actualizar_notas(self, alumno_id: int, nota1: float, nota2: float, nota3: float):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE alumnos SET nota1 = %s, nota2 = %s, nota3 = %s WHERE id = %s",
            (nota1, nota2, nota3, alumno_id)
        )
        db.commit()
        cursor.close()
        db.close()

    def borrar(self, alumno_id: int) -> str:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT nombre FROM alumnos WHERE id = %s", (alumno_id,))
        alumno = cursor.fetchone()
        nombre = alumno["nombre"] if alumno else "Alumno"
        cursor.execute("DELETE FROM alumnos WHERE id = %s", (alumno_id,))
        db.commit()
        cursor.close()
        db.close()
        return nombre
