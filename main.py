from models import *

#michael_scott = Personagem("Michael Scott", "Gerente Regional", 45, "Scranton", "That's what she said!")
#michael_scott.imprimir_info()

pam_beesly = Funcionario("Pam Beesly", "Recepcionista")
michael_scott = Gerente("Michael Scott", "Gerente Regional", "Scranton")

print(pam_beesly.get_nome())

