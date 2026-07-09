import hashlib
import os
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "street_of_treta.db"

ITERACOES_HASH = 260_000

# Valores de base de um personagem recém-criado (nível 1), reaproveitados por
# Street_of_Treta.py tanto para semear/resetar quanto para as fórmulas por nível.
VIDA_BASE = 50
ATACK_BASE = 5
POCAO_BASE = 2
NIVEL_INICIAL = 1
VITORIA_INICIAL = 0

ROSTER_PADRAO = [
    "Bill", "C2", "Jumpsbare", "Lucyfilho", "Átomo", "Alien", "BLUEman",
    "Xerife Maluvido", "Árvore", "Dracoman", "Gigante", "Martin Prudente",
    "Demonio Rubro", "Morte",
]


def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def inicializar_schema():
    with conectar() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                senha_hash TEXT NOT NULL,
                senha_salt TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS personagens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
                nome TEXT NOT NULL,
                vida INTEGER NOT NULL,
                pocao INTEGER NOT NULL,
                atack INTEGER NOT NULL,
                nivel INTEGER NOT NULL,
                vitoria INTEGER NOT NULL,
                UNIQUE(usuario_id, nome)
            )
        """)


def _hash_senha(senha, salt):
    return hashlib.pbkdf2_hmac("sha256", senha.encode("utf8"), salt, ITERACOES_HASH).hex()


def registrar_usuario(username, senha):
    salt = os.urandom(16)
    senha_hash = _hash_senha(senha, salt)
    with conectar() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios (username, senha_hash, senha_salt) VALUES (?, ?, ?)",
                (username, senha_hash, salt.hex()),
            )
        except sqlite3.IntegrityError:
            raise ValueError("Esse nome de usuário já existe.")
        usuario_id = cursor.lastrowid
        cursor.executemany(
            "INSERT INTO personagens (usuario_id, nome, vida, pocao, atack, nivel, vitoria) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            [
                (usuario_id, nome, VIDA_BASE, POCAO_BASE, ATACK_BASE, NIVEL_INICIAL, VITORIA_INICIAL)
                for nome in ROSTER_PADRAO
            ],
        )
        return usuario_id


def autenticar_usuario(username, senha):
    with conectar() as conn:
        linha = conn.execute(
            "SELECT id, senha_hash, senha_salt FROM usuarios WHERE username = ?",
            (username,),
        ).fetchone()
    if linha is None:
        return None
    usuario_id, senha_hash, senha_salt = linha
    if _hash_senha(senha, bytes.fromhex(senha_salt)) != senha_hash:
        return None
    return usuario_id


def carregar_personagens(usuario_id):
    with conectar() as conn:
        linhas = conn.execute(
            "SELECT nome, vida, pocao, atack, nivel, vitoria FROM personagens "
            "WHERE usuario_id = ? ORDER BY id",
            (usuario_id,),
        ).fetchall()
    return linhas


def salvar_personagens(usuario_id, personagens):
    with conectar() as conn:
        conn.executemany(
            "UPDATE personagens SET vida = ?, pocao = ?, atack = ?, nivel = ?, vitoria = ? "
            "WHERE usuario_id = ? AND nome = ?",
            [
                (p.vida, p.pocao, p.atack, p.nivel, p.vitoria, usuario_id, p.nome)
                for p in personagens
            ],
        )


def resetar_personagens(usuario_id):
    with conectar() as conn:
        conn.execute(
            "UPDATE personagens SET vida = ?, pocao = ?, atack = ?, nivel = ?, vitoria = ? "
            "WHERE usuario_id = ?",
            (VIDA_BASE, POCAO_BASE, ATACK_BASE, NIVEL_INICIAL, VITORIA_INICIAL, usuario_id),
        )
