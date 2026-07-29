from BaseDatos.MySqlManager import MySqlManager


class General_Paciente_Service:

    @staticmethod
    def obtener_nota_evolucion_pactiene(db: MySqlManager, list_id_paciente_consultorio: list):
        try:
            with db.obtener_cursor() as cursor:
                sql_select_nota_evolucion = """
                    SELECT
                    ne.nota_evolucion AS 'Nota_Evolucion'
                    FROM Paciente p
                    INNER JOIN Nota_Evolucion ne ON ne.id_paciente  = p.id_paciente
                    WHERE p.id_paciente  = %s AND p.id_consultorio = %s ;

                    """
                cursor.execute(sql_select_nota_evolucion, list_id_paciente_consultorio)
                resultado_nota_evolucion = cursor.fetchall()
                return resultado_nota_evolucion if resultado_nota_evolucion else None
        except Exception as e:
            print(f"Error critico: {e}")
            return None


