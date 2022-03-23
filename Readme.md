# pyGithub
## Dependências
* python 3.6 ou superior
* ibm-watson 
  * pip install --upgrade "ibm-watson>=5.3.0"
* pyContractions ->utilizando uma versão com uma mudança na dependência 
  * pip install git+https://github.com/fabriciosouza21/pycontractions.git
* java 8 java version ->  8.0.322-zulu 
* docker e docker-compose
  * https://docs.docker.com/engine/install/ 
  * https://docs.docker.com/compose/install/

## Alimentar o banco de dados
### Após instalar as dependências do docker
  * python3 init_db.py
### No diretório do docker
  * docker-compose up --build
### Criando Token do GitHub
 * https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
