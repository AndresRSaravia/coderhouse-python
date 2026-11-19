import os

# Carpetas y extensiones que sí queremos incluir
EXCLUIR_DIRS = {'venv', '__pycache__', '.git', 'migrations'}
EXTENSIONES = {'.py', '.html', '.json', '.txt'}

with open('proyecto_completo.txt', 'w', encoding='utf-8') as salida:
    for raiz, dirs, archivos in os.walk('.'):
        # Filtrar carpetas ignoradas
        dirs[:] = [d for d in dirs if d not in EXCLUIR_DIRS]
        for archivo in sorted(archivos):
            if archivo == 'exportar.py' or archivo == 'proyecto_completo.txt':
                continue
            if any(archivo.endswith(ext) for ext in EXTENSIONES):
                ruta = os.path.join(raiz, archivo)
                salida.write(f"\n{'='*60}\nARCHIVO: {ruta}\n{'='*60}\n")
                try:
                    with open(ruta, 'r', encoding='utf-8') as f:
                        salida.write(f.read() + "\n")
                except Exception as e:
                    salida.write(f"[Error leyendo archivo: {e}]\n")

print("Listo: se generó 'proyecto_completo.txt'")