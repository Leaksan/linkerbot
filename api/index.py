from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ensemble de liens
LINKS = {
    "Gestion": {
        "Gestion des Fonctionnalités": "https://mariam-241.vercel.app/manage-feature-access",
            "Dashboard admin": "https://mariam-241.vercel.app/dash",
        "notif setter": "https://myranotif.vercel.app/",
    "Gestion des abonnés": "https://mariam-241.vercel.app/checkmode",
        "admin chats": "https://docfile-chatm2.hf.space/admin1",
        "admin dissertation": "https://docfile-testpdf.hf.space/admin1",
    "Gestion méthodologies": "https://docfile-mariam-metho.hf.space/gestion/",
    "Gestion Cours": "https://docfile-mariam-cours.hf.space/gestion/",
    "Gestion podcast": "https://flask-hello-world-seven-jade.vercel.app/gestion",
    "Dépôt GitHub Podcast": "https://github.com/Leaksan/Podcast-global-/tree/main",
    " Gen fiche de gym": "https://auto-ruby.vercel.app",
    "Cours de Philosophie pour gen type 1": "https://mariam-241.vercel.app/admin/philosophy/courses",
    
    },
    "Outils": {
    "Google AI Studio": "https://aistudio.google.com/app/prompts/new_chat",
    "Replit": "https://replit.com/login?source=home&goto=%2F~",
    "Claude AI": "https://claude.ai/new",
    "ChatGPT": "https://chatgpt.com",
    "Grok": "https://grok.com/chat/982dd977-71d3-4a64-a1dd-5b84a6557ac8",
    "DeepSeek Chat": "https://chat.deepseek.com",
    "Civitai": "https://civitai.com",
    "Kling AI": "https://klingai.com/global/image-to-video/frame-mode/274498562505890",
    "Mixamo": "https://www.mixamo.com/#/?limit=96&page=8",
    "Plask AI": "https://motion.plask.ai/scene/51061e0a-cca0-4ee1-8cff-abca44e381ee",
    "Nero AI Image Upscaler": "https://ai.nero.com/image-upscaler",
    "Convertio": "https://convertio.co/fr/",
    "Sketchfab": "https://sketchfab.com/carmenvillagra1972/likes",
    "iLoveIMG": "https://www.iloveimg.com/compress-image"
    },
    "Apprentissage": {
        "freeCodeCamp": "https://freecodecamp.org",
        "Coursera": "https://coursera.org",
        "YouTube": "https://youtube.com",
        "Udemy": "https://udemy.com",
        "Khan Academy": "https://khanacademy.org"
    },
    "Réseaux Sociaux": {
        "Twitter": "https://twitter.com",
        "LinkedIn": "https://linkedin.com",
        "Instagram": "https://instagram.com",
        "Reddit": "https://reddit.com",
        "Facebook": "https://facebook.com"
    },
    "Divertissement": {
        "Netflix": "https://netflix.com",
        "Spotify": "https://spotify.com",
        "Twitch": "https://twitch.tv",
        "Prime Video": "https://primevideo.com",
        "Disney+": "https://disneyplus.com"
    }
}

@app.route('/')
def index():
    """Page d'accueil affichant tous les liens"""
    return render_template('index.html', links=LINKS)

@app.route('/api/links')
def api_links():
    """API pour récupérer tous les liens en JSON"""
    return jsonify(LINKS)

@app.route('/category/<category_name>')
def category_links(category_name):
    """Afficher les liens d'une catégorie spécifique"""
    category_links = LINKS.get(category_name, {})
    return render_template('category.html', 
                         category_name=category_name, 
                         category_links=category_links)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




