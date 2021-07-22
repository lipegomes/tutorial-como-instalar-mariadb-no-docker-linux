# **Tutorial de configuração para desenvolver com MariaDB no Linux utilizando docker**

Este tutorial foi produzido por mim com intuito de ajudar as pessoas que estão iniciando no mundo de desenvolvimento a fim de aprender a configurar o banco de dados MariaDB em um container docker em um ambiente de desenvolvimento Linux.

## **1 - Instalação e Configuração do MariaDB no Linux**

Para instalação do docker em sua distribuição linux consulte a documentação oficial no link abaixo:

https://docs.docker.com/engine/install/

**1.1 - Criar container docker do MariaDB com a versão com a versão mais recente(latest):**

No link abaixo é possível obter informações sobre a imagem oficial do MariaDB no Docker Hub:

https://hub.docker.com/_/mariadb

```bash
docker run -p 127.0.0.1:3306:3306  --name dev-mariadb -e MARIADB_ROOT_PASSWORD=@#dev2021 -d mariadb:latest
```

**1.2 - Verificar se o MariaDB foi instalado no docker:**

```bash
docker ps -a
```

![Screenshot_20210721_183849.png](https://github.com/lipegomes/tutorial-como-instalar-mariadb-no-docker-linux/blob/main/assets/img/Screenshot_20210721_183849.png)


**1.3 - Executar o container com o MariaDB:**

Ao utilizar o comando docker ps -a é possível obter o CONTAINER ID, copie e cole no comando abaixo seu ID:

```bash
docker start <CONTAINER ID>
```

Ao colar o ID do seu container docker o comando ficará assim:

```bash
docker start bd584ba4e34d
```

**1.4 - Parar o funcionamento do container:**

```bash
docker stop dev-mariadb
```

ou

```bash
docker stop bd584ba4e34d
```

**1.5 - Iniciar o container:**

```bash
docker start dev-mariadb
```

ou

```bash
docker start bd584ba4e34d
```

**2 - Conectar e acessar o banco de dados pelo DBeaver:**

Para download do DBeaver acesse o link abaixo:

https://dbeaver.io/download/

- Ir em: Database > New Database Connection
- Conforme imagem abaixo, clique no icone do MariaDB e depois clique em next( botão na parte inferior).

  ![Screenshot_20210721_191013.png](https://github.com/lipegomes/tutorial-como-instalar-mariadb-no-docker-linux/blob/main/assets/img/Screenshot_20210721_191013.png)

- Confome imagem abaixo, use os seguintes valores:

  - Server Host: localhost
  - Database:
  - Username: root
  - Password(definido durante a instalação do container): @#dev2021

  ![Screenshot_20210721_191224.png](https://github.com/lipegomes/tutorial-como-instalar-mariadb-no-docker-linux/blob/main/assets/img/Screenshot_20210721_191224.png)

  - Clique em Test Connection para verificar se a configuração está correta e realizar uma conexão com sucesso.

  ![Screenshot_20210721_191256.png](https://github.com/lipegomes/tutorial-como-instalar-mariadb-no-docker-linux/blob/main/assets/img/Screenshot_20210721_191256.png)

- Agora o MariaDB está configurado no DBeaver para uso no Linux conforme imagem abaixo:

  ![Screenshot_20210721_191405.png](https://github.com/lipegomes/tutorial-como-instalar-mariadb-no-docker-linux/blob/main/assets/img/Screenshot_20210721_191405.png)

## **3 - Criar e acessar um banco de dados utilizando python**

**3.1 - Criar ambiente virtual:**

Requisitos:

- Necessário ter o python na versão 3.xx instalado em seu sistema operacional, para instalação acesseo link abaixo:

  https://www.python.org/

- Crie uma pasta com o nome desejado, abra o pasta criada no visual studio code e dentro dela crie o ambiente virtual conforme abaixo.

- Necessário ter o virtualenv instalado, para instalação acesse link abaixo:

  https://virtualenv.pypa.io/en/latest/installation.html

  Ou utilize o comando abaixo:

  ```
  pip install virtualenv
  ```

- Criar ambiente virtual do python:

  ```
  virtualenv venv
  ```

- Ativar ambiente virtual: 

  ```
  source venv/bin/activate
  ```

- Verificar se o path do python aponta para o ambiente virtual criado após a ativação:

  ```
  which python
  ```

  Conforme imagem abaixo é possível verificar que o path do python realmente aponta para o ambiente virtual, caso o 
  seu não aponte para a pasta do ambiente virtual, ative novamente o ambiente virtual.

  ![Screenshot_20210721_193824.png](https://github.com/lipegomes/tutorial-como-instalar-mariadb-no-docker-linux/blob/main/assets/img/Screenshot_20210721_193824.png)


- Se clonar o repositório, crie o ambiente virtual e instale o requirements.txt com o comando abaixo:

  ```
  pip install requirements.txt
  ```

**3.2 - Instalar o MySQL Connector como dependencia para o python ter acesso ao banco de dados a ser criado:**

```bash
pip install mysql-connector-python
```

**3.3 - Criar arquivo para acessar o MariaDB e criar banco de dados**

- Crie uma pasta src e dentro dela crie um arquivo chamado createdb.py

- Digite o código abaixo:

 ```python
from getpass import getpass
from mysql.connector import connect, Error

# Estabece conexão com o MariaDB
try:
    with connect(
        host="localhost",
        # username = root
        user=input("Digite o username: "),
        # password = @#dev2021
        password=getpass("Digite o password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE TUTORIAL_MARIADB"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)
  ```

- Agora digite os comando abaixo para acessar o MariaDB e criar um banco de dados:

  ``` python
  python src/createdb.py
  ```

  Conforme imagem abaixo digite o usuário(root) e a senha(@#dev2021):

  ![Screenshot_20210721_202117.png](https://github.com/lipegomes/tutorial-como-instalar-mariadb-no-docker-linux/blob/main/assets/img/Screenshot_20210721_202117.png)

- Abra o DBeaver, clique com botão direito do mouse sobre Databases no canto esquerda da tela. Vai abrir um menu, clique
em refresh. Conforme imagem abaixo é possível ver que o banco de dados foi criado:

  ![Screenshot_20210721_202520.png](https://github.com/lipegomes/tutorial-como-instalar-mariadb-no-docker-linux/blob/main/assets/img/Screenshot_20210721_202520.png)

**3.4 - Criar tabelas no banco de dados**

- Crie um arquivo chamado connect.py

- Digite o código abaixo:

```python
from getpass import getpass
from mysql.connector import connect, Error

try:
    # Estabece conexão com o MariaDB
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="TUTORIAL_MARIADB",
    ) as connection:
        # Cria tabelas no banco da dados TUTORIAL_MARIADB
        create_movies_table_query = """
        CREATE TABLE movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR(4),
            genre VARCHAR(100),
            rate INT
        )
        """
        create_reviewers_table_query = """
        CREATE TABLE reviewers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100)
        )
        """
        create_ratings_table_query = """
        CREATE TABLE ratings (
            movie_id INT,
            reviewer_id INT,
            rating DECIMAL(2,1),
            FOREIGN KEY(movie_id) REFERENCES movies(id),
            FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
            PRIMARY KEY(movie_id, reviewer_id)
        )
        """
        # Caso a conexão seja um sucesso as Queries serão executadas no banco de dados
        with connection.cursor() as cursor:
            cursor.execute(create_movies_table_query)
            cursor.execute(create_reviewers_table_query)
            cursor.execute(create_ratings_table_query)
            connection.commit()
except Error as e:
    print(e)

```

- Agora digite os comando abaixo para criar as tabelas no banco de dados:

  ``` python
  python src/connect.py
  ```

- Abra o DBeaver, clique com botão direito do mouse sobre Tables no canto esquerda da tela. Vai abrir um menu, clique
em refresh. Conforme imagem abaixo é possível ver que as tableas foram criadas no banco de dados:

![Screenshot_20210721_204057.png](https://github.com/lipegomes/tutorial-como-instalar-mariadb-no-docker-linux/blob/main/assets/img/Screenshot_20210721_204057.png)

**4 - Considerações finais:**

O objetivo desse tutorial não é fazer um CRUD(Create, Read, Update, Delete), mas sim aprender a utilizar MariaDB com Docker.
Se sinta a vontade para fazer um CRUD e criar seu próprio banco de dados.

###  Operational System:

- [Manjaro](https://manjaro.org/)

###  Programs Used:

- [MySQL Workbench](https://www.mysql.com/products/workbench/)
- [Dbeaver](https://dbeaver.io/)
- [Visual Studio Code](https://code.visualstudio.com/)

### Tools:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)

### Programming language:

- [Python](https://www.python.org/)

### Data Base in Docker Hub:

- [MySQL](https://hub.docker.com/_/mariadb)
