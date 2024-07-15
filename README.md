# UniEventos.com
O UniEventos.com é um portal de eventos, desenvolvido por <a href="https://www.linkedin.com/in/luiz-augusto-holanda/"><b>Luiz Augusto Holanda</b></a>, um estudante de Engenharia de Software. A plataforma foi criada como requisito para a seletiva de desenvolvedores da UniDev, demonstrando sua capacidade de criar soluções tecnológicas.</p>

## Apps
* authentication -> Abriga a authentificação do django, como as funções do signin, signup, signout e seus respectivos templates.
* unieventos -> Abriga a visualização de eventos, bem como a função de criá-los.

## Cores do site
| Tipo        | Hex | Amostra         
|-------------|--------------|-------------------------
|   Primária   | #10182F      | ![Amostra #10182F](https://via.placeholder.com/15/10182F/000000?text=+) 
|   Primária   | #233466      | ![Amostra #233466](https://via.placeholder.com/15/233466/000000?text=+) 
|  Secundária   | #009579      | ![Amostra #009579](https://via.placeholder.com/15/009579/000000?text=+) 
|  Secundária   | #DEDEDE      | ![Amostra #DEDEDE](https://via.placeholder.com/15/DEDEDE/000000?text=+) 
|  Secundária   | #FFFFFF      | ![Amostra #FFFFFF](https://via.placeholder.com/15/FFFFFF/000000?text=+) 

## Organização
#### django settings.py
* Foi utilizado diretórios especias para os arquivos 'static', criando uma pasta padrão e uma para cada app ('authentication/static' e 'unieventos/static').
* Foi utilizado uma configuração de pasta 'media' utilizada para armazenar as imagens dos eventos.
* Foi criado um diretório especial para obrigar os templates, tanto templates padrões quanto templates específicos de cada app (authentication/templates, unieventos/templates).
* Foi criado um arquivo.css para cada app.
* Foi utilizado o banco de dados padrão do Django (db.sqlite3).
* Foi definido uma url de redirecionamento após o login do app authentication para o app unieventos.

* <b>OBS:</b> Devido ao modo de autenticação do Django, a lógica de signin utilza o username e a senha cadrastados!

#### utilização de templates padrão
* base.html
* nav.html
* footer.html

## Clonar repositório (Visual Studio Code)
* <b>Primeiro passo:</b> Crie uma pasta aonde quiser
* <b>Segundo passo:</b> Abra-a no Vs code como um folder
* <b>Terceiro passo:</b> Clone o repositório: <i>git clone https://github.com/LUIZAUGUSTO1113/unieventos.com.git</i>
* <b>Quarto passo:</b> Abra o terminal dentro do Vs code e digite: <i>dir</i>
* <b>Quinto passo:</b> Agora digite: <i>cd unieventos.com</i>
* <b>Sexto passo:</b> Crie uma venv pelo terminal: <i>python -m venv .env</i>
* <b>Sétimo passo:</b> Ative a venv: <i>restante_do_seu_diretório\.env\Scripts\Activate.ps1</i>
* <b>Oitavo passo:</b> Instale o django: <i>pip install django</i>
* <b>Nono passo:</b> Desative a venv: <i>deactivate</i>
* <b>Décimo passo:</b> Inicie o site: <i>python manage.py runserver</i>

## Check-list
### authentication
#### funções (views.py)
* signup ✅
* signin ✅
* signout ✅
#
* urls ✅

### unieventos
#### modelo de bdo (models.py)
* Event - responsável pelo os eventos ✅
* Registration - responsável pelas inscrições do usuário ❌ - <b>NÃO DESENVOLVIDO</b>

#### funções (views.py)
* event_detail (detalhes do evrnto, nome, criador, data, descrição) ✅
* events (ver todos os eventos) ✅
* create_event (criar eventos com o usuário logado) ✅
* about (ver página sobre o UniEventos.com) ✅
* registration (se iscrever no evento) ❌ - <b>NÃO DESENVOLVIDO</b>
#
* urls ✅

## Considerações finais
O UniEventos.com, não está 100% concluído, está faltando o desenvolvimento da função em que o usuário poderá se inscrever nos eventos, bem como as regras para essa iscrição. Porém acredito que este atende praticamente maior parte das requisições do teste de desenvolvimento.
<br>
<b>OBS:</b> A versão atual do UniEventos.com é um <b>TESTE</b>
#### Algumas outras features também estão faltando: 
* função delete de eventos, utilizando as regras requisitadas. 
* uma página ou uma modal dedicada para o usuário, na qual contenha os eventos criados por este e também os eventos que este está incrito.
* mudar as urls do event_detail, de pk (primary key) para o nome dos eventos.
* possível uso do import de uma biblioteca na model Event, para tratar melhoro texto da descrição dos eventos.
* maior responsividade e maior polimeto.
* troca dos parâmetros da autenticação do Django, para realizar signin com e-mail.

## © 2024 1113, Inc.
