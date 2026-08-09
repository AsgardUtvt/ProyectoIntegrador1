from BaseDatos.MySqlManager import MySqlManager


class General_Menu_Service:


    @staticmethod
    def datos_grafica_medicamentos(db: MySqlManager, rango_fechas_med: list):
        try:
            with db.obtener_cursor() as cursor:
                sql_obtener_medicamentos = """
SELECT
       m.`medicamento_name` AS EJEX,
       COUNT(m.medicamento_name) AS EJEY
FROM `Receta` r
INNER JOIN `Receta_Medicamento` rm ON rm.`id_receta` = r.`id_receta`
INNER JOIN `Medicamento` m ON m.`id_medicamento` = rm.`id_medicamento`
WHERE m.id_consultorio = %s AND r.receta_date BETWEEN %s AND %s
GROUP BY m.`id_medicamento`, m.`medicamento_name`
ORDER BY EJEY ;
                """
                cursor.execute(sql_obtener_medicamentos, rango_fechas_med)
                resultados_obtener_medicametos = cursor.fetchall()
                print(f"def datos_grafica_medicamentos: {resultados_obtener_medicametos}")
                return resultados_obtener_medicametos if resultados_obtener_medicametos else ()
        except Exception as e:
            print(f"Error {e}")
            return ()


    @staticmethod
    def datos_grafica_citas(db: MySqlManager, rango_fechas_cit: list):
        """ Mandar id_conultorio, y rango_de_fechas """
        try:
            with db.obtener_cursor() as cursor:
                slq_obtener_citas = """
SELECT DATE(`cita_date`) AS EJEX,
       COUNT(*) AS EJEY
FROM `Cita` c
WHERE c.id_consultorio = %s AND cita_date BETWEEN %s AND %s
GROUP BY DATE(`cita_date`)
ORDER BY EJEX;
                """
                cursor.execute(slq_obtener_citas, rango_fechas_cit)
                resultados_obtener_citas = cursor.fetchall()
                print(f"def datos_grafica_citas: {resultados_obtener_citas}")
                return resultados_obtener_citas if resultados_obtener_citas else ()
        except Exception as e:
            print(f"Error {e}")
            return ()
