import telebot

# REMPLACEZ PAR LE TOKEN DE VOTRE BOT (important !)
API_TOKEN = '7851962953:AAH6odQl01MjFLJCv6a1wutnstFDImypCZc' # Gardez votre token ici

bot = telebot.TeleBot(API_TOKEN)

# --- VOS LIENS DÉFINIS ICI ---
SITE_LINKS = {
    'gestion_podcast': "https://flask-hello-world-seven-jade.vercel.app/gestion",
    'upload_podcast': "https://github.com/Leaksan/Podcast-global-",
    'notif_bot': "https://t.me/NotificationmariamBot",
    'gestion_cours': "https://docfile-mariam-cours.hf.space/gestion/",
    'gestion_metho': "https://docfile-mariam-metho.hf.space/gestion",
    'gestion_philo': "https://mariam-241.vercel.app/admin/philosophy/courses",
    'gestion_abonnes': "https://mariam-241.vercel.app/checkmode",
    'dashboard': "https://mariam-241.vercel.app/dash",
}

# Génère la liste des commandes disponibles pour le décorateur et le message d'aide
AVAILABLE_COMMANDS = list(SITE_LINKS.keys())

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    help_text = "Bonjour ! Je suis votre bot de gestion de site Mariam.\n\n"
    help_text += "Voici les commandes disponibles pour obtenir des liens directs :\n"
    for cmd_name in AVAILABLE_COMMANDS:
        help_text += f"/{cmd_name}\n"
    help_text += "\nTapez l'une de ces commandes pour recevoir le lien correspondant."
    bot.reply_to(message, help_text)

@bot.message_handler(commands=AVAILABLE_COMMANDS)
def send_site_link(message):
    command = message.text[1:]  # Enlève le '/' au début de la commande
    if command in SITE_LINKS:
        link = SITE_LINKS[command]
        # Petite personnalisation du message de réponse
        # Vous pouvez ajouter une description plus détaillée ici si vous le souhaitez
        description = command.replace("_", " ").capitalize() # Ex: 'gestion_podcast' -> 'Gestion podcast'
        bot.reply_to(message, f"Voici le lien pour '{description}':\n{link}")
    else:
        # Ce cas ne devrait pas être atteint grâce au décorateur,
        # mais c'est une bonne pratique de le garder.
        bot.reply_to(message, "Désolé, je ne trouve pas de lien pour cette commande.")

# Gestionnaire pour les messages qui ne sont pas des commandes reconnues
@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.reply_to(message, "Je ne comprends pas cette commande. Tapez /help pour voir les commandes disponibles.")

if __name__ == '__main__':
    print("Bot Mariam en cours d'exécution...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Erreur lors du polling: {e}")
    finally:
        print("Arrêt du bot.")
