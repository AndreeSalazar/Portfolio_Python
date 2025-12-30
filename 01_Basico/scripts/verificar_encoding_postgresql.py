"""
Verificar encoding de PostgreSQL y solucionar problemas de codificación
"""

import psycopg2
from psycopg2 import sql

def verificar_encoding():
    """Verifica el encoding de la base de datos PostgreSQL"""
    
    print("=" * 70)
    print("VERIFICANDO ENCODING DE POSTGRESQL")
    print("=" * 70)
    
    try:
        # Conectar sin especificar encoding primero
        conn = psycopg2.connect(
            host='localhost',
            database='retail_analysis_basico',
            user='postgres',
            password='123456'
        )
        
        cur = conn.cursor()
        
        # Verificar encoding del servidor
        cur.execute("SHOW server_encoding;")
        server_encoding = cur.fetchone()[0]
        print(f"\n[1] Server encoding: {server_encoding}")
        
        # Verificar encoding del cliente
        cur.execute("SHOW client_encoding;")
        client_encoding = cur.fetchone()[0]
        print(f"[2] Client encoding: {client_encoding}")
        
        # Verificar encoding de la base de datos
        cur.execute("""
            SELECT datname, pg_encoding_to_char(encoding) 
            FROM pg_database 
            WHERE datname = 'retail_analysis_basico';
        """)
        db_info = cur.fetchone()
        if db_info:
            print(f"[3] Database encoding: {db_info[1]}")
        
        # Verificar si hay datos con problemas
        try:
            cur.execute("SELECT COUNT(*) FROM ventas;")
            count = cur.fetchone()[0]
            print(f"[4] Registros en ventas: {count}")
            
            # Intentar leer un registro problemático
            cur.execute("SELECT * FROM ventas LIMIT 1;")
            row = cur.fetchone()
            print(f"[5] Primer registro leído correctamente")
        except UnicodeDecodeError as e:
            print(f"[5] ❌ Error al leer datos: {e}")
            print("   Los datos tienen encoding incorrecto")
        
        cur.close()
        conn.close()
        
        print("\n" + "=" * 70)
        print("RECOMENDACIONES:")
        print("=" * 70)
        
        if server_encoding.lower() != 'utf8':
            print("⚠️  El servidor no usa UTF-8")
            print("   Considera recrear la BD con UTF-8")
        
        if db_info and db_info[1].lower() != 'utf8':
            print("⚠️  La base de datos no usa UTF-8")
            print("   Necesitas recrear la BD con UTF-8")
        
        return server_encoding, client_encoding, db_info[1] if db_info else None
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return None, None, None


if __name__ == "__main__":
    verificar_encoding()

