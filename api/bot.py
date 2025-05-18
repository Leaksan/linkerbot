import telebot
import os
from flask import Flask, request # Importez Flask

# --- VOS CONFIGURATIONS ---
API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN') # Récupérer depuis les variables d'environnement
if not API_TOKEN:
    raise ValueError("La variable d'environnement TELEGRAM_API_TOKEN n'est pas définie!")

WEBHOOK_URL_PATH = f"/webhook/{API_TOKEN}" # Chemin secret pour le webhook
# L'URL complète sera https://VOTRE_DOMAINE_VERCEL.vercel.app/webhook/VOTRE_TOKEN

bot = telebot.TeleBot(API_TOKEN, threaded=False) # threaded=False est important pour les webhooks simples
app = Flask(__name__) # Initialisez Flask

# --- DÉFINISSEZ VOS LIENS ICI ---
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
    command = message.text[1:]
    if command in SITE_LINKS:
        link = SITE_LINKS[command]
        description = command.replace("_", " ").capitalize()
        bot.reply_to(message, f"Voici le lien pour '{description}':\n{link}")
    else:
        bot.reply_to(message, "Désolé, je ne trouve pas de lien pour cette commande.")

@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.reply_to(message, "Je ne comprends pas cette commande. Tapez /help pour voir les commandes disponibles.")

# --- PARTIE WEBHOOK POUR VERSEL ---
# Endpoint pour que Telegram envoie les mises à jour
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    else:
        return 'Requête invalide', 403

# Endpoint optionnel pour définir le webhook (vous pouvez aussi le faire manuellement)
@app.route('/set_webhook')
def set_webhook_route():
    # Note: L'URL publique doit être celle de votre déploiement Vercel
    # Vous devrez la remplacer par la vraie URL après le premier déploiement
    # ou la définir dynamiquement si possible (plus complexe)
    # Pour l'instant, vous devrez probablement définir le webhook manuellement après le déploiement.
    public_url = os.environ.get('VERCEL_URL') # Vercel définit cette variable
    if public_url:
        full_webhook_url = f"https://{public_url}{WEBHOOK_URL_PATH}"
        bot.remove_webhook() # Important pour éviter les conflits
        bot.set_webhook(url=full_webhook_url)
        return f"Webhook configuré à {full_webhook_url}", 200
    return "VERCEL_URL non définie. Configurez le webhook manuellement.", 500

@app.route('/') # Route de base pour vérifier que l'app tourne
def index():
    return "Bot Telegram en cours d'exécution avec Flask!", 200

# Pas besoin de bot.polling() ni de if __name__ == '__main__': pour Vercel
# Vercel utilisera un serveur WSGI (comme Gunicorn) pour exécuter `app`
