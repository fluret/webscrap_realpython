import requests
from bs4 import BeautifulSoup
import os

# URL de l'article
url = "https://realpython.com/primer-on-python-decorators/"

# Récupérer le contenu de la page
response = requests.get(url)
response.encoding = 'utf-8'  # Spécifier l'encodage
soup = BeautifulSoup(response.content, 'html.parser')

# Créer un dossier pour les fichiers .py
os.makedirs('code_blocks', exist_ok=True)

# Fonction pour convertir le HTML en LaTeX
def html_to_latex(soup):
    latex_content = []
    code_block_counter = 1

    for element in soup.find_all(['p', 'h1', 'h2', 'ul', 'ol', 'div']):
        if element.name == 'p':
            latex_content.append(element.get_text())
        elif element.name == 'h1':
            latex_content.append(f"\\chapter{{{element.get_text()}}}")
        elif element.name == 'h2':
            latex_content.append(f"\\section{{{element.get_text()}}}")
        elif element.name == 'ul':
            latex_content.append("\\begin{itemize}")
            for li in element.find_all('li'):
                latex_content.append(f"\\item {li.get_text()}")
            latex_content.append("\\end{itemize}")
        elif element.name == 'ol':
            latex_content.append("\\begin{enumerate}")
            for li in element.find_all('li'):
                latex_content.append(f"\\item {li.get_text()}")
            latex_content.append("\\end{enumerate}")
        elif element.name == 'div' and 'class' in element.attrs and 'codeblock' in element['class']:
            code = element.find('code').get_text()
            code_filename = f"code_blocks/code_block_{code_block_counter}.py"
            with open(code_filename, 'w', encoding='utf-8') as code_file:
                code_file.write(code)
            code_block_counter += 1

    return "\n".join(latex_content)

# Convertir le contenu HTML en LaTeX
latex_content = html_to_latex(soup)

# Sauvegarder le contenu LaTeX dans un fichier
with open('article.tex', 'w', encoding='utf-8') as latex_file:
    latex_file.write(latex_content)

print("Conversion terminée. Les fichiers LaTeX et .py ont été générés.")