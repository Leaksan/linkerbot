from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dictionnaire des liens intégré directement dans le code
LINKS = {
    "Gestion": {
        "Gestion des Fonctionnalités": "https://mariam-241.vercel.app/manage-feature-access",
    "Gestionnaire Fichiers (Métho)": "https://docfile-mariam-metho.hf.space/gestion/",
    "Tableau de Bord": "https://mariam-241.vercel.app/dash",
    "Mode de Vérification": "https://mariam-241.vercel.app/checkmode",
    "Gestion App Flask (Test)": "https://flask-hello-world-seven-jade.vercel.app/gestion",
    "Dépôt GitHub (Podcast Global)": "https://github.com/Leaksan/Podcast-global-/tree/main",
    "Application Auto-Ruby": "https://auto-ruby.vercel.app",
    "Admin des Cours de Philosophie": "https://mariam-241.vercel.app/admin/philosophy/courses",
    "Gestionnaire Fichiers (Cours)": "https://docfile-mariam-cours.hf.space/gestion/"
    },
    "Outils": {
        "Figma": "https://figma.com",
        "Notion": "https://notion.so",
        "Trello": "https://trello.com",
        "Slack": "https://slack.com",
        "Discord": "https://discord.com"
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
