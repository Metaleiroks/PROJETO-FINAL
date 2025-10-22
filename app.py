#API SENAI
from flask import Flask 
from core.aluno.aluno_controller import aluno_controller
from core.usuario.usuario_controller import controller as usuario_controller
from core.professor.professor_controller import controller as professor_controller
from core.materias.materias_controller import controller as materias_controller

app = Flask(__name__)

#registro das controllers
app.register_blueprint(aluno_controller)
app.register_blueprint(usuario_controller)
app.register_blueprint(professor_controller)
app.register_blueprint(materias_controller)

if __name__ == '__main__':
    app.run(debug=True)

