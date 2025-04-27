🦊 Furia CS eSports Bot - "Furico"
Um bot interativo no Telegram feito para fãs da FURIA de CS:GO!
Ele traz novidades, resultados, interações divertidas com o mascote "Furico" e muito mais.

📋 Planejamento do Projeto
🎯 Objetivo
Criar um chat para fãs da FURIA CS:GO acompanharem e interagirem com o time de forma divertida e em tempo real.

📚 Funcionalidades Iniciais (MVP)
- **/start**: Inicia a conversa e apresenta o Furico, o mascote da FURIA.
- **/help**: Exibe a lista de comandos disponíveis para interagir com o bot.
- **/jogos**: Mostra os jogos programados para o dia da FURIA.
- **/ranking**: Mostra o ranking de fãs (em breve!).
- **/furico**: Fala sobre o mascote Furico.
- **/eventos**: Informa sobre os próximos eventos da FURIA.
- **/campeonato**: Mostra os campeonatos atuais em que a FURIA está participando.
- **/rankingvalve**: Mostra o ranking da Valve (atualmente, a FURIA está em 11° lugar!).
- **/outrosjogosfuria**: Exibe informações sobre os outros jogos da FURIA, como **League of Legends** e **Valorant**.

### Exemplo de Interação

1. Ao iniciar o bot com o comando `/start`, o bot irá pedir que você escolha uma opção (Jogos, Campeonato, Eventos, Ranking Valve, Outros Jogos da FURIA).
2. Você pode clicar nas opções disponíveis ou digitar um comando para obter mais informações.
3. O comando `/outrosjogosfuria` vai exibir informações sobre os outros jogos da FURIA, como **CBLOL** para **League of Legends** e **VCT** para **Valorant**.


🛠️ Base de Dados
Banco de dados: SQLite (leve e simples para início).

Armazena:

Pontuação dos fãs baseada em interações.

Histórico básico de interações (se necessário).

🦊 Tom de Voz do Mascote "Furico"
Estilo: Engraçado, leve e brincalhão.

Puxa conversa de forma divertida.

Faz piadas sobre adversários, motiva os torcedores e cria apelidos carinhosos para os usuários.

🔥 Fluxo Inicial de Conversa
plaintext
Copiar
Editar
Usuário inicia o bot ➔

Bot Furico:
"Olá (NOME DA PESSOA)! 🦊
Eu sou o Furico, seu guia pelo mundo insano da FURIA! 
O que você quer saber hoje? 😎"

[Opções para o usuário]
- Jogos
- Campeonato
- Eventos

Usuário escolhe "Jogos" ➔

Bot Furico:
"Claro! 🏆 Hoje temos FURIA vs (NOME DO TIME). Bora dar show! 🔥"

Usuário escolhe "Campeonato" ➔

Bot Furico:
"Estamos jogando o (NOME DO CAMPEONATO) e vamos meter bala! 🔫 Quer ver outra coisa?"

Usuário escolhe "Eventos" ➔

Bot Furico:
"Nosso próximo evento será um Meet & Greet no dia (DIA DO EVENTO)! Não fique de fora!"

🚀 Tecnologias Utilizadas
Python 3.11
python-telegram-bot
SQLite





