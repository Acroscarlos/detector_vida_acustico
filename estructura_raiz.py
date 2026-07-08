import os

def generar_arbol_directorios(directorio, prefijo=""):
    # Carpetas que queremos ignorar para no saturar la terminal
    carpetas_ignoradas = {'.git', '__pycache__', 'node_modules', 'vendor', 'ESC_50', 'fold1', 'fold2', 'fold3', 'fold4', 'fold5', 'fold6', 'fold7', 'fold8', 'fold9', 'fold10', 'Noise_Ambient', 'Noise_FalsePositive', "Noise_Structural", 'Target_Rhythmic',  'Target_Voice', 'voz_espanol'}
    
    try:
        # Listar todo el contenido del directorio actual
        elementos = os.listdir(directorio)
    except PermissionError:
        print(prefijo + "├── 🚫 [Acceso Denegado]")
        return

    # Filtrar las carpetas que no queremos ver y ordenar alfabéticamente
    elementos = [e for e in elementos if e not in carpetas_ignoradas]
    elementos.sort()

    for i, elemento in enumerate(elementos):
        ruta_completa = os.path.join(directorio, elemento)
        es_ultimo = (i == len(elementos) - 1)
        
        # Símbolos para dibujar el árbol
        conector = "└── " if es_ultimo else "├── "
        
        if os.path.isdir(ruta_completa):
            print(prefijo + conector + "📂 " + elemento)
            # Extensión del prefijo para los "hijos" de esta carpeta
            extension = "    " if es_ultimo else "│   "
            # Llamada recursiva para entrar a la subcarpeta
            generar_arbol_directorios(ruta_completa, prefijo + extension)
        else:
            print(prefijo + conector + "📄 " + elemento)

if __name__ == "__main__":
    # La ruta exacta que nos indicaste
    ruta_raiz = r"C:\Users\carlo\Documents\detector_vida_acustico\detector_vida_acustico"
    
    print("="*60)
    print(f"📊 ESCANEANDO ESTRUCTURA DE DIRECTORIOS")
    print("="*60)
    
    if os.path.exists(ruta_raiz):
        # Imprimir la carpeta raíz (base)
        print(f"📂 {os.path.basename(ruta_raiz)}")
        # Iniciar la magia recursiva
        generar_arbol_directorios(ruta_raiz)
    else:
        print(f"❌ Error: La ruta no existe. Por favor verifica:\n{ruta_raiz}")
    
    print("\n" + "="*60)
    print("✅ Escaneo finalizado.")