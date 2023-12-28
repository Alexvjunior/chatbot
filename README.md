# ChatBot com OpenAI GPT-3.5-turbo

Este projeto implementa um ChatBot utilizando a poderosa API GPT-3.5-turbo da OpenAI. O ChatBot é capaz de compreender mensagens dos usuários, manter o contexto da conversa e fornecer respostas inteligentes. Além disso, foi adicionada uma lógica para respostas automáticas e contextuais, proporcionando uma experiência mais personalizada e interativa.

## **Requisitos**
- python3

## **Instruções de Execução**

1. Clone o repositório.

2. Navegue até o diretório do projeto:
```bash
cd chatbot
```

3. Execute o programa utilizando Makefile ou Crie e ative um virtual environment:
```bash
make run
```
```bash
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```


## **Qualidade de Código e Segurança**

Para garantir a qualidade do código e aprimorar a segurança, as seguintes ferramentas estão integradas ao projeto:

### isort

[isort](https://pycqa.github.io/isort/) é uma utilidade Python que ordena os imports em ordem alfabética e os separa automaticamente em seções.

Para executar o isort e formatar automaticamente seus imports, utilize o seguinte comando:

```bash
isort .
```


### flake8

flake8 é um linter de código que verifica o código Python quanto a estilo e erros de programação.

Para executar o flake8 e verificar o seu código, utilize o seguinte comando:
```bash
flake8 *.py
```
Ou
```bash
make lint
```

### safety

safety é uma ferramenta de linha de comando que verifica suas dependências Python em busca de vulnerabilidades de segurança conhecidas.

Para executar o safety e verificar vulnerabilidades, utilize o seguinte comando:
```bash
safety check
or
make security
```
