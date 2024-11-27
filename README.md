oi deem pip install -r requirements.txt
baixar extensao de pdf no vscode 
se mesmo assim aparecer que elas não foram baixadas:

criar ambiente virtual usando python -m venv venv (esse segundo venv é só o nome do ambiente, pode ser qualquer coisa) no terminal
ativar o ambiente usando venv\Scripts\Activate.bat no terminal
dar ctrl + shift + p no vscode
procurar python: select interpreters ou algo parecido
selecionar o ambiente que vc acabou de criar e ativar
rodar no terminal pip install -r requirements.txt e rodar o codigo ebaa

mudanças desse código pro do professor:
nao precisa baixar aquele webdrriver podre - só precisa do webdriver_manager
o xpath da cotação tava errado, selecionava o 1(dolar) ao inves do valor atual em reais então tive que mudar
