import re

with open('src/database/manager.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix clean_old_data
clean_old = '''def clean_old_data(self, days=10):
        with self.get_connection('bionews_news_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""
                DELETE FROM noticias 
                WHERE fecha_scraping < NOW() - (INTERVAL '1 day' * %s)
            """, (days,))
            conn.commit()'''
content = re.sub(r'def clean_old_data\(self, days=10\):.*?conn\.commit\(\)', clean_old, content, flags=re.DOTALL)

get_table_data_fix = '''def get_table_data(self, table_name, limit=1000):
        """Obtiene todos los registros de una tabla especifica."""
        allowed = {
            'fiscalizaciones', 'medidas_provisionales', 'normativas',
            'pertinencias', 'programasDeCumplimiento', 'registroSanciones',
            'requerimientos', 'sancionatorios', 'Tribunales',
            'minsal_vigentes', 'minsal_resultados', 'mma_abiertas', 'mma_cerradas',
            'dga_consultas', 'sea_proyectos_evaluados'
        }
        if table_name not in allowed:
            raise ValueError(f"Tabla no permitida: {table_name}")
            
        db = 'bionews_legal_db'
        if table_name in ['minsal_vigentes', 'minsal_resultados', 'mma_abiertas', 'mma_cerradas', 'dga_consultas']:
            db = 'bionews_consultations_db'
        
        with self.get_connection(db) as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = %s
            """, (table_name.lower(),))
            columns = [col['column_name'] for col in cursor.fetchall()]
            
            order_by = ""
            if 'fecha_scraping' in columns:
                order_by = "ORDER BY fecha_scraping DESC"
            elif 'fecha' in columns:
                order_by = "ORDER BY fecha DESC"
            elif 'id' in columns:
                order_by = "ORDER BY id DESC"
                
            query = f"SELECT * FROM {table_name} {order_by} LIMIT %s"
            cursor.execute(query, (limit,))
            return cursor.fetchall()'''

content = re.sub(r'def get_table_data\(self, table_name, limit=1000\):.*?return cursor\.fetchall\(\)', get_table_data_fix, content, flags=re.DOTALL)

with open('src/database/manager.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Manager fixed")
