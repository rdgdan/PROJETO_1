Markdown# API Connect - MVP Backend

> **Desenvolvido por:** Danilo Araújo (rdgdan)  
> **Repositório:** [https://github.com/rdgdan/PROJETO_1](https://github.com/rdgdan/PROJETO_1)

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
   git clone [https://github.com/rdgdan/PROJETO_1.git](https://github.com/rdgdan/PROJETO_1.git)
   cd PROJETO_1
Crie e ative um Ambiente Virtual (Opcional, mas recomendado):Windows:Bashpython -m venv venv
venv\Scripts\activate
Linux / macOS:Bashpython3 -m venv venv
source venv/bin/activate
Instale as dependências:Bashpip install flask
Execute a aplicação:Bashpython script.py
O servidor estará rodando em: http://127.0.0.1:5000📋 Tabela de Referência de EndpointsMétodoEndpointStatus SucessoDescriçãoExemplo de Payload (Body)GET/users200 OKRetorna a listagem de todos os usuários cadastrados.NenhumPOST/users201 CreatedCadastra um novo usuário (Exige name e email).{"name": "Maria Silva", "email": "maria@email.com"}GET/users/<id>200 OKRetorna os detalhes de um usuário específico pelo ID.NenhumPUT/users/<id>200 OKAtualiza os dados de um usuário já existente.{"name": "Maria Silva", "email": "novo@email.com"}DELETE/users/<id>200 OKRemove permanentemente um usuário da base de dados.Nenhum🛡️ Padrões de Resposta e ErrosA API utiliza o padrão de envelopamento JSON para todas as respostas HTTP:1. Sucesso ao Criar Usuário (Status 201 Created)JSON{
  "status": "success",
  "message": "Usuário cadastrado com sucesso!",
  "data": {
    "id": 1,
    "name": "Maria Silva",
    "email": "maria@email.com"
  }
}
2. Erro de Validação (Status 400 Bad Request)Ocorre quando algum campo obrigatório (name ou email) não é enviado no payload:JSON{
  "status": "error",
  "error": "Campos 'name' e 'email' são obrigatórios."
}
3. Registro Não Encontrado (Status 404 Not Found)Ocorre ao buscar, atualizar ou deletar um ID que não existe na base:JSON{
  "status": "error",
  "message": "Usuário com ID 999 não encontrado."
}

---

### Como atualizar no GitHub depois de colar no VS Code:

Depois que você colar no arquivo `README.md` e salvar no VS Code, abra o terminal e rode estes 3 comandos rápidos para subir a versão completa:

```bash
git add README.md
git commit -m "Documentacao completa do README"
git push origin main