from flask import Blueprint, Flask, jsonify, request

app = Flask(__name__)

# --- 1. SIMULAÇÃO DE PERSISTÊNCIA (models/database.py) ---
database_users = [
    {"id": 1, "name": "Ana Silva", "email": "ana.silva@email.com"},
    {"id": 2, "name": "Carlos Souza", "email": "carlos.souza@email.com"},
]


def get_next_id():
  if not database_users:
    return 1
  return database_users[-1]["id"] + 1


# --- 2. CONTROLADORES E ROTAS (controllers/userController.py & routes/userRoutes.py) ---
user_bp = Blueprint("user_bp", __name__)


# Listagem Geral (GET /users)
@user_bp.route("/users", methods=["GET"])
def get_users():
  return jsonify({"status": "success", "data": database_users}), 200


# Cadastro com Validação (POST /users)
@user_bp.route("/users", methods=["POST"])
def create_user():
  data = request.get_json()

  if not data or not data.get("name") or not data.get("email"):
    return (
        jsonify({
            "status": "error",
            "error": "Campos 'name' e 'email' são obrigatórios.",
        }),
        400,
    )

  new_user = {
      "id": get_next_id(),
      "name": data["name"],
      "email": data["email"],
  }

  database_users.append(new_user)

  return (
      jsonify({
          "status": "success",
          "message": "Usuário cadastrado com sucesso!",
          "data": new_user,
      }),
      201,
  )


# Busca Específica por ID (GET /users/<int:user_id>)
@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
  user = next((u for u in database_users if u["id"] == user_id), None)

  if not user:
    return (
        jsonify({
            "status": "error",
            "message": f"Usuário com ID {user_id} não encontrado.",
        }),
        404,
    )

  return jsonify({"status": "success", "data": user}), 200


# Atualização de Usuário (PUT /users/<int:user_id>)
@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
  user = next((u for u in database_users if u["id"] == user_id), None)

  if not user:
    return (
        jsonify({
            "status": "error",
            "message": f"Usuário com ID {user_id} não encontrado para atualização.",
        }),
        404,
    )

  data = request.get_json()

  if not data or not data.get("name") or not data.get("email"):
    return (
        jsonify({
            "status": "error",
            "message": "Campos 'name' e 'email' são obrigatórios para atualizar.",
        }),
        400,
    )

  user["name"] = data["name"]
  user["email"] = data["email"]

  return (
      jsonify({
          "status": "success",
          "message": "Usuário atualizado com sucesso!",
          "data": user,
      }),
      200,
  )


# Remoção de Usuário (DELETE /users/<int:user_id>)
@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
  user_index = next(
      (index for index, u in enumerate(database_users) if u["id"] == user_id),
      None,
  )

  if user_index is None:
    return (
        jsonify({
            "status": "error",
            "message": f"Usuário com ID {user_id} não encontrado para exclusão.",
        }),
        404,
    )

  deleted_user = database_users.pop(user_index)

  return (
      jsonify({
          "status": "success",
          "message": "Usuário removido com sucesso!",
          "data": deleted_user,
      }),
      200,
  )


# --- 3. REGISTRO DO BLUEPRINT E INICIALIZAÇÃO (app.py) ---
app.register_blueprint(user_bp)

if __name__ == "__main__":
  app.run(debug=True, port=5000)