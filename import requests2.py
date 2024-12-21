import requests
from bs4 import BeautifulSoup
import os
import deepl

# Remplacez 'your-api-key' par votre clé API DeepL
auth_key = "04226dcb-d1b2-4e84-b1eb-dc8185488841"
translator = deepl.Translator(auth_key)


def escape_latex(text):
    # Liste des caractères spéciaux LaTeX à échapper
    special_chars = {
        "\\": r"\textbackslash{}",
        "#": r"\#",
        "$": r"\$",
        "%": r"\%",
        "&": r"\&",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    # Échapper les caractères spéciaux
    for char, escaped_char in special_chars.items():
        text = text.replace(char, escaped_char)
    return text


def translate_text(text, dest_language="fr"):
    result = translator.translate_text(text, target_lang=dest_language.upper())
    return result.text

# URL de l'article
url = "https://realpython.com/absolute-vs-relative-python-imports/"

# Récupérer le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Récupérer le contenu de la div avec la classe 'article-body'
#article_body = soup.find('div', class_='article-body')
#article_body = soup.find_all('section', class_='section2')
sections = soup.find_all('section', class_='section2')

# Créer un dossier pour les fichiers .py
os.makedirs('code_blocks', exist_ok=True)

# Fonction pour convertir le HTML en LaTeX
def html_to_latex(sections):
    latex_content = []
    code_block_counter = 1

    for section in sections:
        for element in section.find_all(['p', 'h1', 'h2', 'ul', 'ol', 'div']):
            if element.name == 'p':
                if element.parent.name != 'li':
                    latex_content.append(translate_text(element.get_text()))
            elif element.name == 'h1':
                latex_content.append(f"\\chapter{{{translate_text(element.get_text())}}}")
            elif element.name == 'h2':
                latex_content.append(f"\\section{{{translate_text(element.get_text())}}}")
            elif element.name == 'ul':
                latex_content.append("\\begin{itemize}")
                for li in element.find_all('li'):
                    latex_content.append(f"\\item {translate_text(li.get_text())}")
                latex_content.append("\\end{itemize}")
            elif element.name == 'ol':
                latex_content.append("\\begin{enumerate}")
                for li in element.find_all('li'):
                    latex_content.append(f"\\item {translate_text(li.get_text())}")
                latex_content.append("\\end{enumerate}")
            elif element.name == 'div' and 'class' in element.attrs and 'codeblock' in element['class']:
                code = element.find('code').get_text()
                code_filename = f"code_blocks/code_block_{code_block_counter}.py"
                with open(code_filename, 'w') as code_file:
                    code_file.write(code)
                code_block_counter += 1

    return "\n".join(latex_content)

# Convertir le contenu HTML en LaTeX
latex_content = html_to_latex(sections)

# Sauvegarder le contenu LaTeX dans un fichier
with open('article.tex', 'w', encoding="utf-8") as latex_file:
    latex_file.write(latex_content)

print("Conversion terminée. Les fichiers LaTeX et .py ont été générés.")