from aluno import Aluno
from disciplina import Disciplina

aluno1 = Aluno("Paulo", "123456", "Ciência da Computação")

model_lin = Disciplina("Modelagem Linear Para Aprendizado de Máquina", "Rodolfo")
dsa = Disciplina("Data Structures and Algorithms", "Erick")

aluno1.matricular(model_lin)