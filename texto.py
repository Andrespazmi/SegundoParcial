def leer():
    with open("invitados.txt", "r", encoding="UTF-8") as f:
        invitado = [linea[:-1] for linea in f]
        print(invitado)
        
def escribir():
    invitadosA=  ["Andres", "Francisco", "Victor", "Kevin", "Javier"]
    invitadosB= ["Valeria", "Alejandra", "Alexa", "", "Ariana"]

    with open("invitados.txt", "w", encoding="UTF-8") as f:
        for nombre in invitadosB:
            f.write(nombre)
            f.write("\n")

def run():
    escribir()
    leer()

if __name__ =="__main__":
    run()