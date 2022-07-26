# Dashboard do datalogger

Para rodar o projeto na sua máquina para o desenvolvimento é nessário seguir os seguintes passos.

## Instalar as dependências do projeto:
No projeto existe o arquivo requirements.txt , nele estão as dependências nessárias para rodar o projeto na sua máquina.
```bash
pip install -r requirements.txt
```

## Variáveis de ambiente:
Como medida de segurança mínima para o desenvolvimento do projeto, as variáveis de ambiente referente a conexão com o banco de dados, não estão hardcoded, estão definidas no arquivo .env, que deve ser copiado para o diretório raiz do projeto.

O arquivo .env deve conter as seguintes variáveis:

```
SQLALCHEMY_DATABASE_URI=database_model://user:password@host:port/database
```

### é nessário entrar em contato com os administradores do projeto para ter acesso ao .env

## Rodar o projeto:
Para rodar o projeto, basta executar o comando:
```bash
python3 wsgi.py
```

## Deploy:
Para manter um padrão de projeto, seguimos os passos a baixo para publicar alterações no projeto no GitHub.

1. Verificar se o repositório local esta atualizado com o repositório do GitHub.
2. Criar uma branch nova localmente, com a sigla DMDC-< contagem de branchs >.
3. Enviar todas as alterações na sua branch para o GitHub.
4. Criar uma Pull Request para o repositório do GitHub para que os desenvolvedores possam testar a sua branch.

## links uteis:
- [Como cirar um branch com GIT]('https://www.atlassian.com/br/git/tutorials/using-branches/git-checkout#:~:text=O%20comando%20git%20branch%20pode,para%20mudar%20para%20esse%20branch.')
- [Como criar uma PullRequest]('https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request')
- [Como criar uma branch com VsCode]('https://imasters.com.br/desenvolvimento/use-git-com-interface-grafica-visual-studio-code-e-aumente-sua-produtividade#:~:text=Para%20ter%20acesso%20a%20mais,excluir%20branch%2C%20publicar%2C%20etc.')

