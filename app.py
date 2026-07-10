import os
from functools import wraps

from flask import Flask, flash, redirect, render_template, request, session, url_for

import db
import jogo

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "chave-de-desenvolvimento-trocar-em-producao")


def carregar_personagens_usuario(usuario_id):
    return [jogo.Personagem(*linha) for linha in db.carregar_personagens(usuario_id)]


def login_requerido(rota):
    @wraps(rota)
    def rota_protegida(*args, **kwargs):
        if not session.get("usuario_id"):
            return redirect(url_for("login"))
        return rota(*args, **kwargs)

    return rota_protegida


@app.route("/")
def index():
    if session.get("usuario_id"):
        return redirect(url_for("personagens"))
    return redirect(url_for("login"))


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        username = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "")
        if not username or not senha:
            flash("Preencha usuário e senha.")
            return render_template("cadastro.html")
        try:
            usuario_id = db.registrar_usuario(username, senha)
        except ValueError as erro:
            flash(str(erro))
            return render_template("cadastro.html")
        session.clear()
        session["usuario_id"] = usuario_id
        return redirect(url_for("personagens"))
    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "")
        usuario_id = db.autenticar_usuario(username, senha)
        if usuario_id is None:
            flash("Usuário ou senha inválidos.")
            return render_template("login.html")
        session.clear()
        session["usuario_id"] = usuario_id
        return redirect(url_for("personagens"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/instrucoes")
def instrucoes():
    return render_template("instrucoes.html")


@app.route("/personagens")
@login_requerido
def personagens():
    lista = carregar_personagens_usuario(session["usuario_id"])
    return render_template("personagens.html", personagens=list(enumerate(lista)))


@app.route("/personagens/resetar", methods=["POST"])
@login_requerido
def resetar():
    db.resetar_personagens(session["usuario_id"])
    session.pop("batalha", None)
    flash("Progresso resetado para os valores iniciais.")
    return redirect(url_for("personagens"))


@app.route("/batalha/iniciar", methods=["POST"])
@login_requerido
def iniciar_batalha():
    lista = carregar_personagens_usuario(session["usuario_id"])
    try:
        jogador_idx = int(request.form["jogador"])
    except (KeyError, ValueError):
        flash("Escolha inválida.")
        return redirect(url_for("personagens"))

    if not (0 <= jogador_idx < len(lista)) or lista[jogador_idx].vida <= 0:
        flash("Escolha inválida: o personagem precisa estar vivo.")
        return redirect(url_for("personagens"))

    cpu = jogo.gerar_cpu(excluir_nome=lista[jogador_idx].nome)

    session["batalha"] = {
        "jogador_idx": jogador_idx,
        "cpu": vars(cpu),
        "rodada": 0,
        "empate": 0,
        "vez_cpu": 0,
        "vez_jogador": 0,
        "aguardando_pocao": False,
        "mensagens": [],
    }
    return redirect(url_for("batalha"))


@app.route("/batalha")
@login_requerido
def batalha():
    estado = session.get("batalha")
    if not estado:
        return redirect(url_for("personagens"))
    lista = carregar_personagens_usuario(session["usuario_id"])
    jogador = lista[estado["jogador_idx"]]
    cpu = jogo.Personagem(**estado["cpu"])
    return render_template("batalha.html", jogador=jogador, cpu=cpu, estado=estado)


@app.route("/batalha/jogar", methods=["POST"])
@login_requerido
def jogar():
    estado = session.get("batalha")
    if not estado:
        return redirect(url_for("personagens"))

    try:
        jogada = int(request.form["jogada"])
    except (KeyError, ValueError):
        flash("Jogada inválida.")
        return redirect(url_for("batalha"))
    if jogada not in (1, 2, 3):
        flash("Jogada inválida.")
        return redirect(url_for("batalha"))

    lista = carregar_personagens_usuario(session["usuario_id"])
    jogador = lista[estado["jogador_idx"]]
    cpu = jogo.Personagem(**estado["cpu"])

    contadores = {
        "empate": estado["empate"],
        "vez_cpu": estado["vez_cpu"],
        "vez_jogador": estado["vez_jogador"],
    }
    estado["rodada"] += 1
    resultado = jogo.jogar_rodada(jogador, cpu, jogada, contadores)
    estado["empate"] = contadores["empate"]
    estado["vez_cpu"] = contadores["vez_cpu"]
    estado["vez_jogador"] = contadores["vez_jogador"]
    estado["mensagens"] = resultado["mensagens"]
    estado["cpu"] = vars(cpu)

    # Só o personagem do jogador é salvo: a CPU tem status próprio e efêmero,
    # nunca persistido no banco do usuário logado.
    db.salvar_personagens(session["usuario_id"], [jogador])

    if resultado["morreu"]:
        estado["aguardando_pocao"] = False
        session["batalha"] = estado
        return redirect(url_for("resultado"))

    estado["aguardando_pocao"] = resultado["pode_pocao"]
    session["batalha"] = estado
    return redirect(url_for("batalha"))


@app.route("/batalha/pocao", methods=["POST"])
@login_requerido
def pocao():
    estado = session.get("batalha")
    if not estado:
        return redirect(url_for("personagens"))

    usar = request.form.get("usar") == "sim"
    lista = carregar_personagens_usuario(session["usuario_id"])
    jogador = lista[estado["jogador_idx"]]
    cpu = jogo.Personagem(**estado["cpu"])

    mensagens = []
    if usar and jogo.pode_usar_pocao(jogador, cpu):
        jogo.usar_pocao(jogador)
        mensagens.append(f"Vida {jogador.nome}: {jogador.vida}")
        mensagens.append(f"{jogador.nome} tem {jogador.pocao} poções")
        db.salvar_personagens(session["usuario_id"], [jogador])

    estado["aguardando_pocao"] = False
    estado["mensagens"] = mensagens
    session["batalha"] = estado
    return redirect(url_for("batalha"))


@app.route("/batalha/resultado")
@login_requerido
def resultado():
    estado = session.get("batalha")
    if not estado:
        return redirect(url_for("personagens"))

    lista = carregar_personagens_usuario(session["usuario_id"])
    jogador = lista[estado["jogador_idx"]]
    cpu = jogo.Personagem(**estado["cpu"])

    if jogador.vida <= 0:
        vencedor, perdedor = cpu, jogador
        jogador.vitoria = 0
    else:
        vencedor, perdedor = jogador, cpu
        jogador.vitoria += 1

    # Só o personagem do jogador sobe de nível e é salvo — a CPU é descartada
    # ao fim da batalha, seu resultado não deve afetar o roster do usuário.
    mensagens_nivel = jogo.subir_nivel([jogador])
    db.salvar_personagens(session["usuario_id"], [jogador])

    rodadas = estado["rodada"]
    session.pop("batalha", None)

    return render_template(
        "resultado.html",
        vencedor=vencedor,
        perdedor=perdedor,
        rodadas=rodadas,
        mensagens_nivel=mensagens_nivel,
    )


if __name__ == "__main__":
    db.inicializar_schema()
    app.run(debug=True)
