auto = {"aa":2}
print(auto.get("aa","<<"))
ada = 22
# print(@ada)
from pathlib import Path
CARPETA_DATA = Path("data")
ARCHIVO_POSTS = CARPETA_DATA / "posts.txt"
def preparar_archivos():
    CARPETA_DATA.mkdir(exist_ok=True)
BASE_DIR = Path(__file__).parent
CARPETA_DATA = BASE_DIR / "data"
ARCHIVO_POSTS = CARPETA_DATA / "posts.txt"
print(BASE_DIR)
print(ARCHIVO_POSTS)


# import json
# with open("posts.json", "r", encoding="utf-8") as archivo:
#     posts = json.load(archivo)
# nuevo_post = {
#     "id": 3,
#     "titulo": "Archivos JSON en Python",
#     "autor": "Marta",
#     "estado": "publicado"
# }
# posts.append(nuevo_post)
# with open("posts.json", "w", encoding="utf-8") as archivo:
#     json.dump(posts, archivo, indent=4, ensure_ascii=False)
# print("Nuevo post agregado correctamente.")

# import json
# try:
#     with open("posts.json", "r", encoding="utf-8") as archivo:
#         posts = json.load(archivo)
#     print("Archivo cargado correctamente.")
#     print(posts)
# except FileNotFoundError:
#     print("El archivo posts.json no existe.")
# except json.JSONDecodeError:
#     print("El archivo existe, pero no tiene un formato JSON válido.")

class Usuario:
    def __init__(self, username, email, nombre):
        self.username = username
        self.email = email
        self.nombre = nombre
    def mostrar_perfil(self):
        print("Usuario:", self.username)
        print("Nombre:", self.nombre)
        print("Email:", self.email)

usuario_1 = Usuario("ana_dev", "ana@email.com", "Ana")
usuario_1.mostrar_perfil()

class Post:
    def __init__(self, titulo, contenido, autor):
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.estado = "borrador"
    def publicar(self):
        self.estado = "publicado"
        print(f"El post '{self.titulo}' fue publicado.")
    def mostrar_resumen(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor.nombre)
        print("Estado:", self.estado)



post_1 = Post(
    "Introducción a Python",
    "En este post vamos a aprender los primeros pasos con Python.",
    usuario_1
)
post_1.mostrar_resumen()
post_1.publicar()
post_1.mostrar_resumen()


usuario_1 = Usuario("ana_dev", "ana@email.com", "Ana")
usuario_2 = Usuario("luis_py", "luis@email.com", "Luis")
post_1 = Post("Introducción a Python", "Contenido del primer post", usuario_1)
post_2 = Post("Listas en Python", "Contenido del segundo post", usuario_1)
post_3 = Post("HTML básico", "Contenido del tercer post", usuario_2)
posts = [post_1, post_2, post_3]
print("Posts escritos por Ana:")
for post in posts:
    if post.autor.username == "ana_dev":
        print("-", post.titulo)