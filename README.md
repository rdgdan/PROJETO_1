# API Connect - MVP Backend

> **Desenvolvido por:** Danilo Araújo (rdgdan)
> **Repositório:** (https://github.com/rdgdan/PROJETO_1)

---

## 📌 Objetivo da API

A **API Connect** foi desenvolvida para atender às demandas de integração e gestão de usuários de uma startup em fase de crescimento. O sistema atua como um Produto Mínimo Viável (MVP) focado em agilidade arquitetural e robustez, fornecendo um CRUD completo para o gerenciamento de cadastros com persistência simulada em memória, validação rigorosa de dados de entrada e padronização estrita de respostas em formato JSON.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.x**
* **Flask** (Microframework web)
* **Git & GitHub** (Versionamento de código)
* **Thunder Client / Postman** (Testes e validação de endpoints)

---

## ⚙️ Passo a Passo para Execução Local

Siga os passos abaixo para clonar e rodar a aplicação na sua máquina de desenvolvimento:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rdgdan/PROJETO_1.git
   cd PROJETO_1
   ```

2. **Crie e ative um Ambiente Virtual** (Opcional, mas recomendado):

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Linux / macOS:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install flask
   ```

4. **Execute a aplicação:**
   ```bash
   python script.py
   ```

5. O servidor estará rodando em: `http://127.0.0.1:5000`

---

## 📋 Tabela de Referência de Endpoints

| Método | Endpoint | Status Sucesso | Descrição | Exemplo de Payload (Body) |
|--------|----------|----------------|-----------|---------------------------|
| GET | `/users` | 200 OK | Retorna a listagem de todos os usuários cadastrados. | Nenhum |
| POST | `/users` | 201 Created | Cadastra um novo usuário (exige `name` e `email`). | `{"name": "Maria Silva", "email": "maria@email.com"}` |
| GET | `/users/<id>` | 200 OK | Retorna os detalhes de um usuário específico pelo ID. | Nenhum |
| PUT | `/users/<id>` | 200 OK | Atualiza os dados de um usuário já existente. | `{"name": "Maria Silva", "email": "novo@email.com"}` |
| DELETE | `/users/<id>` | 200 OK | Remove permanentemente um usuário da base de dados. | Nenhum |

---

## 🛡️ Padrões de Resposta e Erros

A API utiliza o padrão de envelopamento JSON para todas as respostas HTTP:

### 1. Sucesso ao Criar Usuário (Status 201 Created)

```json
{
  "status": "success",
  "message": "Usuário cadastrado com sucesso!",
  "data": {
    "id": 1,
    "name": "Maria Silva",
    "email": "maria@email.com"
  }
}
```

### 2. Erro de Validação (Status 400 Bad Request)

Ocorre quando algum campo obrigatório (`name` ou `email`) não é enviado no payload:

```json
{
  "status": "error",
  "error": "Campos 'name' e 'email' são obrigatórios."
}
```

### 3. Registro Não Encontrado (Status 404 Not Found)

Ocorre ao buscar, atualizar ou deletar um ID que não existe na base:

```json
{
  "status": "error",
  "message": "Usuário com ID 999 não encontrado."
}
```