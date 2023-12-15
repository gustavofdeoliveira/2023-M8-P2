# 2023-M8-P2

## Como rodar

1. Na pasta raiz, acesse o terminal e rode os comandos.
2. `cd src && chmod +x setup.sh`
3. Agora rode o comando: `zsh setup.sh`. Um terminal do x terminal deve abrir, digite a senha e o ollama sera executado, após ser execudo, pode fechar o terminal.
4. Vamos criar uma `venv` para ajudar no nosso ambiente de dev. Rode o comando `python -m venv .`. Isso permitira a criação de alguns arquivos dentro da pasta.
5. Agora, o próximo passo é instalar o `bark` para a geração de áudio. No terminal ainda, rode o comando `pip install git+https://github.com/suno-ai/bark.git`. Espere a instalação terminar.
6. Por fim, vamos instalar as dependências diretas do projeto, sendo assim, no terminal execute o comando `pip install -r requirements. txt`.
7. Antes de executar, abra o arquivo `main.py`, vá para a linha 31 e descomente ela, e na linha 35 comente ela. Agora é só rodar o projeto.
8. Ainda na pasta `src`, rode o comando `python main.py`.
9. Agora é só mandar algum prompt pela interface do terminal
   

## Nota

O código gerado para a prova, não foi possível testar já que o ollama, não roda no meu computador do Inteli. Durante as ponderadas desenvolvidas, a maioria foram feitas com OpenAI por esse motivo e avisado para o professor de programação do modulo. 