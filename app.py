from flask import Flask, render_template, request, abort
from flask_mail import Mail, Message
import json

app = Flask(__name__)


app.config.from_file("config.json", load=json.load)


mail = Mail(app)


sections = [
    {"name": "sobre", "title": "Homailson Lopes", "content": "sobre.html"},
    {"name": "portfolio", "title": "Portfolio", "content": "portfolio.html"},
    {"name": "contato", "title": "Contato", "content": "contato.html"}
]

projetos = [
    {"id": "projeto1", "nome": "Barbearia Dom Manolo",
        "imagem": "project1.jpg"},
    # {"id": "projeto2", "nome": "Vaga de Projeto",
    #  "imagem": "project2.jpg"},
    # {"id": "projeto3", "nome": "Vaga de Projeto",
    #  "imagem": "project3.jpg"},
    # {"id": "projeto4", "nome": "Vaga de Projeto",
    #  "imagem": "project4.jpg"},
    # {"id": "projeto5", "nome": "Vaga de Projeto",
    #  "imagem": "project5.jpg"},
    # {"id": "projeto6", "nome": "Vaga de Projeto",
    #  "imagem": "project6.jpg"}
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        assunto = request.form.get("assunto")
        mensagem = request.form.get("mensagem")

        msg = Message(assunto,
                      sender=email,
                      recipients=[app.config.get("MAIL_USERNAME")]
                      )

        msg.body = f"Mensagem de: {nome}\n{mensagem}"

        mail.send(msg)

    return render_template("index.html", sections=sections, projetos=projetos)


@app.route("/<string:projeto_id>")
def projects(projeto_id: str):
    projeto_gen = (p for p in projetos if p['id'] == projeto_id)
    projeto = next(projeto_gen, None)
    if projeto:
        return render_template(f"projects/{projeto_id}.html", projeto=projeto)
    else:
        abort(404)


@app.errorhandler(404)
def not_found_error(e):
    return render_template('404.html'), 404
