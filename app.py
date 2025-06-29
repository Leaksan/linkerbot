from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'votre-cle-secrete-ici'  # Changez cette clé !

# Fichier pour stocker les liens
LINKS_FILE = 'links.json'

def load_links():
    """Charge les liens depuis le fichier JSON"""
    if os.path.exists(LINKS_FILE):
        try:
            with open(LINKS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_links(links):
    """Sauvegarde les liens dans le fichier JSON"""
    with open(LINKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(links, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """Page d'accueil affichant tous les liens"""
    links = load_links()
    return render_template('index.html', links=links)

@app.route('/admin')
def admin():
    """Page d'administration pour gérer les liens"""
    links = load_links()
    return render_template('admin.html', links=links)

@app.route('/add_link', methods=['POST'])
def add_link():
    """Ajouter un nouveau lien"""
    title = request.form.get('title', '').strip()
    url = request.form.get('url', '').strip()
    description = request.form.get('description', '').strip()
    category = request.form.get('category', '').strip()
    
    if not title or not url:
        flash('Le titre et l\'URL sont obligatoires', 'error')
        return redirect(url_for('admin'))
    
    # Ajouter http:// si pas de protocole
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    links = load_links()
    new_link = {
        'id': len(links) + 1,
        'title': title,
        'url': url,
        'description': description,
        'category': category,
        'created_at': datetime.now().isoformat()
    }
    
    links.append(new_link)
    save_links(links)
    
    flash('Lien ajouté avec succès !', 'success')
    return redirect(url_for('admin'))

@app.route('/delete_link/<int:link_id>')
def delete_link(link_id):
    """Supprimer un lien"""
    links = load_links()
    links = [link for link in links if link['id'] != link_id]
    save_links(links)
    
    flash('Lien supprimé avec succès !', 'success')
    return redirect(url_for('admin'))

@app.route('/edit_link/<int:link_id>', methods=['GET', 'POST'])
def edit_link(link_id):
    """Modifier un lien"""
    links = load_links()
    link = next((l for l in links if l['id'] == link_id), None)
    
    if not link:
        flash('Lien non trouvé', 'error')
        return redirect(url_for('admin'))
    
    if request.method == 'POST':
        link['title'] = request.form.get('title', '').strip()
        link['url'] = request.form.get('url', '').strip()
        link['description'] = request.form.get('description', '').strip()
        link['category'] = request.form.get('category', '').strip()
        
        if not link['url'].startswith(('http://', 'https://')):
            link['url'] = 'https://' + link['url']
        
        save_links(links)
        flash('Lien modifié avec succès !', 'success')
        return redirect(url_for('admin'))
    
    return render_template('edit_link.html', link=link)

@app.route('/api/links')
def api_links():
    """API pour récupérer tous les liens en JSON"""
    links = load_links()
    return jsonify(links)

if __name__ == '__main__':
    # Créer le fichier de liens s'il n'existe pas
    if not os.path.exists(LINKS_FILE):
        save_links([])
    
    app.run(debug=True, host='0.0.0.0', port=5000)