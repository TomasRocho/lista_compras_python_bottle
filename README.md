# Sistema Acadêmico - FCTE

## Descrição do Projeto

Desenvolvimento de um sistema de criação de lista de compras. 

Listas personalizadas por usuário contendo controle de mercados e produtos, valores médios de produtos e valor total de uma lista de compra.

Desenvolvido em Python e Bottle para ambiente web.

É dividido em dois projetos: Backend(API rest) e Frontend.

Utiliza além do Bottle, a biblioteca Beaker.Middleware para controle de variáveis de Sessão no Frontend e a biblioteca Requests para fazer a chamadas de API do FrontEnd para o BackEnd. 

O Backend implementa uma API Rest, armazenando os dados através do banco SQLite. As rotas estão definidas nos controllers e utilizam os 4 comandos básicos do padrão Rest: get, post, delete e put, sempre devolvendo dados em formato JSON.

Os atributos do diagrama de classes estão implementados em classes Python na pasta "models".

Os métodos do diagrama de classes estão implementados em classes Python na pasta "services".

O Frontend é responsável por responder com páginas HTML às rotas requisitadas no browser.

Praticamente toda a lógica de negócios está implementada no Backend.

Além do Bottle, Middleware e Requests, a aplicação também utiliza outras bibliotecas internas do Python, tais como: json, os, datetime, SQLite3 entre outras.

O Frontend utiliza toda a formatação html através de CSS, sendo JavaScript utilizado apenas em um pequeno trecho da aplicação (para mostrar os valores médio dos produtos).

O enunciado do trabalho pode ser encontrado aqui:
- [Trabalho Final](https://github.com/lboaventura25/OO-T06_2025.1_UnB_FCTE/tree/main/trabalhos/epf)



## Dados do Aluno

- **Nome completo:** Tomás Garcia Rocho
- **Matrícula:** 242024988
- **Curso:** Engenharias
- **Turma:** FGA0158 -ORIENTAÇÃO A OBJETOS- T06

---

## Instruções para Compilação e Execução

1. **Compilação:**  
    * Após a instalação do interpretador Python, e do gerenciador de ambiente virtual (venv) é necessário criar e ativar o ambiente virtual e nele instalar as bibliotecas Bottle, beaker.middleware e requests.

    * python3 -m venv myenv (criação do ambiente virtual myenv)

    * source myenv/bin/activate (ativação do ambiente virtual myenv)
    
    * pip install bottle

    * pip install beaker

    * pip install requests

2. **Execução:**  
    * Backend: ir para a pasta Backend e executar python3 app.py (ou python app.py) - por default roda na porta 8080. Não esquecer que o ambiente virtual myenv deve estar ativo.
 
    * Frontend: ir para a pasta Frontend e executar python3 app.py (ou python app.py) - por default roda na porta 8081. Não esquecer que o ambiente virtual myenv deve estar ativo.

    * Abrir o browser no endereço http://localhost/8081

    * Como dados de testes são criados, utilizar os usuarios usuarionormal@unb.br ou usuarioadministrador@unb.br, ambos com senha "segredo"

3. **Diagrama de Classes:**
    ![DiagramaClasses.png](DiagramaClasses.png)

## Contato

- [tomasgarciarocho@gmail.com]
