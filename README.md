# Sistema-De-Gestao-Web
Aqui, nós desenvolvemos um exemplo de sistema web para armazenar dados pessoais.

***

Neste sistema, vamos registar, listar, editar ou excluir qualquer filme, série, anime ou desenho já assistido.

***
Para rodar este projeto, além de clonar este repositório, você deve criar um ambiente virtual Python.

***

### Como criar um ambiente virtual Python?

* Clone o projeto no seu computador.

* Dentro desse repositório, abra o seu terminal.

* Rode: o seguinte comando:
```
python -m venv virtualenvironment
```
   * Obs1: Não precisa escrever _virtualenvironment_. Escolha o nome que quiser desde que não deixe espaços.

   * Obs2: Se você estiver no Windows e nunca iniciou um ambiente virtual, pode receber uma mensagem de erro, como **não pode ser carregado porque a execução de scripts foi desabilitada neste sistema.**. Neste caso, faço o seguinte:
      
      1. Feche o terminal.

      1. Execute-o novamente, mas como admnistrador.

      1. Execute o seguinte comando: 
      ```
      Set-ExecutionPolicy
      ```

      1. Em seguida, execute: 
      ```
      Remote Signed
      
      ```
    Feito isso, tente criar um novo ambiente virtual e o Windows deve permite que ele seja ativado. É uma política de segurança que impede a ativação.

* Depois de criar o ambiente, precisamos ativá-lo. Então rode o comando:

```
.\virtualenvironment\Scripts\activate
```
Obs: Se você escolheu outro nome para o ambiente virtual, coloque-o no lugar de _virtualenvironment_.

Pronto! Seu ambiente virtual está criado e ativado.

***

### E agora?

Precisamos de duas bibliotecas para rodar este projeto.

Dentro da pasta do projeto, com o ambiente virtual criado e ativado, execute:
```
pip install django
```

Em seguida, execute:

```
pip install crispy-bootstrap5
```

Feito isso, você deve ser capaz de rodar o projeto.