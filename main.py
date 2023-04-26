from models import *

#michael_scott = Personagem("Michael Scott", "Gerente Regional", 45, "Scranton", "That's what she said!")
#michael_scott.imprimir_info()

pam_beesly = Funcionario("Pam Beesly", "Recepcionista")
michael_scott = Gerente("Michael Scott", "Gerente Regional", "Scranton")

def imprimir_cargo(funcionario):
    print("Cargo:", funcionario.cargo)	

imprimir_cargo(pam_beesly)
imprimir_cargo(michael_scott)

episodio = Episodio(numero=1, titulo="Pilot", diretor="Ken Kwapis", temporada=1)

