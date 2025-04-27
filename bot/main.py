from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Agora você pode acessar o token usando os.getenv
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Mensagens iniciais
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_first_name = update.effective_user.first_name
    reply_keyboard = [['Jogos', 'Campeonato', 'Eventos']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text(
        f"Olá {user_first_name}! \n"
        "Eu sou o Furico, seu guia pelo mundo insano da FURIA!\n"
        "O que você quer saber hoje? 😎",
        reply_markup=markup
    )

# Comando /help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Aqui estão os comandos disponíveis para você interagir comigo:\n\n"
        "/start - Inicia a conversa e te apresenta ao Furico.\n"
        "/jogos - Mostra os jogos de hoje da FURIA.\n"
        "/ranking - Mostra o ranking de fãs (em breve!).\n"
        "/furico - Fala sobre o mascote Furico.\n"
        "/eventos - Informa sobre os próximos eventos da FURIA.\n"
        "/campeonato - Mostra o campeonato atual em que a FURIA está participando.\n"
        "Basta clicar nos botões ou digitar um comando para saber mais! 😉"
    )

# Comandos
async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🏆 Hoje temos FURIA vs (NOME DO TIME). Bora dar show! 🔥")

async def ranking(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🏅 Ranking de fãs em construção! Em breve você poderá ver quem é torcedor raiz!")

async def furico(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("😎 Eu sou o Furico, a pantera mais braba do CS! Tá pronto pra torcer com a gente?")

async def eventos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("📅 O próximo evento será um Meet & Greet no dia (DIA DO EVENTO)! Não fique de fora!")

async def campeonato(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🎯 Estamos jogando o (NOME DO CAMPEONATO)! Vamos meter bala! 🔫")

# Resposta para mensagens do teclado personalizado
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    if text == "jogos":
        await jogos(update, context)
    elif text == "campeonato":
        await campeonato(update, context)
    elif text == "eventos":
        await eventos(update, context)
    else:
        await update.message.reply_text("Não entendi... 😅 Manda um comando ou escolhe uma opção!")

# Função principal
def main() -> None:
    # Não há necessidade de redefinir o TOKEN aqui, pois ele já foi carregado com o dotenv
    app = ApplicationBuilder().token(TOKEN).build()

    # Adiciona os handlers para os comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))  # Comando /help
    app.add_handler(CommandHandler("jogos", jogos))
    app.add_handler(CommandHandler("ranking", ranking))
    app.add_handler(CommandHandler("furico", furico))
    app.add_handler(CommandHandler("eventos", eventos))
    app.add_handler(CommandHandler("campeonato", campeonato))

    # Adiciona o handler para mensagens gerais, fora dos comandos específicos
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot Furico rodando... 🦊")
    app.run_polling()

if __name__ == "__main__":
    main()

