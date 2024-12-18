# PostAPI

Uma API para gerenciar posts com funcionalidades de autenticação, votação e consultas personalizadas. Esta API foi construída utilizando Python com o framework FastAPI, integrado com um banco de dados relacional e implementando autenticação via JWT.

## Funcionalidades

1. **Autenticação**:
   - Registro e login de usuários.
   - Geração e validação de tokens JWT para autenticação.

2. **Gerenciamento de Posts**:
   - Criação de novos posts.
   - Recuperação de posts com suporte a pesquisa, paginação e contagem de votos.

3. **Sistema de Votação**:
   - Usuários podem votar em posts.
   - Contagem total de votos retornada junto aos dados do post.

## Estrutura do Projeto

- **models**: Define os modelos do banco de dados.
- **schemas**: Define as classes Pydantic usadas para validação e serialização dos dados.
- **routers**: Contém as rotas para os endpoints da API.
- **main.py**: Arquivo principal para iniciar a aplicação FastAPI.

## Instalação

### Pré-requisitos
- Python 3.9 ou superior
- Gerenciador de pacotes `pip`

### Passos

1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` baseado no exemplo fornecido (`.env.example`).
   - Insira as credenciais e configurações necessárias no arquivo `.env`.

5. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

## Endpoints Principais

### **Autenticação**
- `POST /users/`: Registro de usuários.
- `POST /login/`: Login de usuários.

### **Posts**
- `GET /posts/`: Recupera todos os posts com suporte a pesquisa e paginação.
- `POST /posts/`: Cria um novo post.
- `GET /posts/{id}/`: Recupera detalhes de um post específico.

### **Votos**
- `POST /vote/`: Registra ou remove um voto em um post.

## Esquemas de Dados

### **Usuário**
- `UserCreate`: Email e senha para registro.
- `UserOut`: Informações do usuário sem dados sensíveis.

### **Post**
- `PostBase`: Título, conteúdo e status de publicação.
- `PostOut`: Post com contagem de votos.

### **Voto**
- `Vote`: ID do post e direção do voto (1 para adicionar, 0 para remover).

## Tecnologias Utilizadas

- **FastAPI**: Framework principal para criação da API.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **Pydantic**: Validação e serialização de dados.
- **JWT**: Autenticação baseada em tokens.

## Melhorias Futuras

- Adicionar testes automatizados.
- Implementar ordenação de posts por critérios como popularidade ou data.
- Suporte a comentários em posts.
- Rate limiting para evitar abuso de endpoints.

## Contribuição

Contribuições são bem-vindas! Por favor, crie uma branch para sua feature ou correção e envie um Pull Request com as alterações.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Crie, explore e gerencie seus posts com a PostAPI! 🎉
