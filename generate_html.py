import os
import re

# Premium CSS for CVs
CSS = """
body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }
h1 { color: #1a1a1a; border-bottom: 2px solid #1a1a1a; padding-bottom: 5px; margin-top: 30px; font-size: 24pt; }
h2 { color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 3px; margin-top: 25px; font-size: 18pt; }
h3 { color: #34495e; margin-top: 20px; font-size: 14pt; border-bottom: 1px solid #f9f9f9; }
h4 { color: #444; margin-top: 15px; font-size: 12pt; font-weight: bold; }
p { margin: 10px 0; font-size: 11pt; }
ul { margin: 10px 0; padding-left: 20px; }
li { margin: 5px 0; font-size: 11pt; }
strong { color: #000; }
a { color: #2980b9; text-decoration: none; }
hr { border: 0; border-top: 1px solid #ddd; margin: 20px 0; }
.header-meta { font-size: 10pt; color: #7f8c8d; }
@media print {
    body { padding: 0; }
    .no-print { display: none; }
}
"""

def md_to_html(md):
    # Very simple MD to HTML parser for CV structure
    html = md
    # Headers
    html = re.sub(r'^# (.*)$', r'<h1>\1</h1>', html, flags=re.M)
    html = re.sub(r'^## (.*)$', r'<h2>\1</h2>', html, flags=re.M)
    html = re.sub(r'^### (.*)$', r'<h3>\1</h3>', html, flags=re.M)
    html = re.sub(r'^#### (.*)$', r'<h4>\1</h4>', html, flags=re.M)
    # Bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    # Italic
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    # Links
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)
    # Horizontal Rule
    html = re.sub(r'^---$', r'<hr>', html, flags=re.M)
    # Lists
    # This is a bit tricky for nested lists, but CVs use simple ones
    html = re.sub(r'^- (.*)$', r'<li>\1</li>', html, flags=re.M)
    # Wrap series of <li> in <ul>
    html = re.sub(r'(<li>.*</li>(\n<li>.*</li>)*)', r'<ul>\1</ul>', html)
    # Paragraphs (crude)
    # html = re.sub(r'\n\n', r'</p><p>', html)
    return html

def main():
    base_dir = r"e:\000VSCODE PROJECT MULAI DARI DESEMBER 2025\CV KERJA\my-professional-resumes"
    master_cv_dir = os.path.join(base_dir, "Master-CVs")
    html_dir = os.path.join(base_dir, "HTML_Export")
    
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)
        
    categories = [
        '01-Web3-Solana', '02-Eth-Base', '03-Mobile-Flutter', '04-AI-Automation',
        '05-GameFi-Degen', '06-Community-Growth', '07-Web3-Strategy', '08-Fintech-Payments'
    ]
    
    for cat in categories:
        cat_path = os.path.join(master_cv_dir, cat)
        if not os.path.exists(cat_path): continue
        
        for file in os.listdir(cat_path):
            if file.endswith('.md'):
                with open(os.path.join(cat_path, file), 'r', encoding='utf-8') as f:
                    md = f.read()
                
                body = md_to_html(md)
                template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{file}</title>
    <style>{CSS}</style>
</head>
<body>
    {body}
</body>
</html>"""
                
                html_name = file.replace('.md', '.html')
                with open(os.path.join(html_dir, html_name), 'w', encoding='utf-8') as f:
                    f.write(template)
                print(f"Generated {html_name}")

if __name__ == "__main__":
    main()
