import telebot

CHAVE_API = "5551668537:AAGfCnynugaFSrFPF2LAh2q-dWccExa40Qc"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["opcao1"])
def responder(menssagem):
    info = """
    Deisiane (Deise) é uma progamadora
atualmente ela usa as linguagens Python, JavaScrip tambem usa HTML e CSS.
Tem 18 Anos e progama a 4 anos."""
    bot.send_message(menssagem.chat.id, info)


@bot.message_handler(commands=["opcao2"])
def responder(menssagem):
    redes = """
    GitHub: (LINK)
Instagram: (LINK)
Linkedin: (LINK)
E-mail: (LINK)
    """
    bot.send_message(menssagem.chat.id, redes)


@bot.message_handler(commands=["opcao3"])
def responder(menssagem):
    bot.send_message(menssagem.chat.id, "OK, aperte no link para continuar (LINK)")


@bot.message_handler(content_types=["text"])
def responder(menssagem):
#   print(menssagem)
    texto = f"""
Olá, {menssagem.chat.first_name}!
Escolha uma opção para continuar (CLIQUE NO INTEM!):

    /opcao1 mais informações sobre Deise
    /opcao2 ver redes sociais de Deise
    /opcao3 entrar em contato com Deise no WhatsApp
    
Responder qualquer outra coisa nao vai funcionar, caso queira algo mais entre em contato com Deise no WhatsApp"""
    bot.reply_to(menssagem, texto)


bot.polling()
