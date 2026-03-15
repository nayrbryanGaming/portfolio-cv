import os
import re
import subprocess

# --- SETTINGS ---
BASE_DIR = r"e:\000VSCODE PROJECT MULAI DARI DESEMBER 2025\CV KERJA\my-professional-resumes"
MASTER_DIR = os.path.join(BASE_DIR, "Master-CVs")
HTML_DIR = os.path.join(BASE_DIR, "INTERNAL_BUILD_ASSETS")
PDF_DIR = os.path.join(BASE_DIR, "OFFICIAL_COURT_DELIVERY")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# --- PREMIUM STYLING ---
CSS = """
body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.4; color: #111; max-width: 800px; margin: 0 auto; padding: 40px; background-color: #fff; }
h1 { color: #000; border-bottom: 3.5px solid #000; padding-bottom: 8px; margin-top: 30px; font-size: 26pt; font-weight: 800; letter-spacing: -1.2px; }
h2 { color: #333; border-bottom: 1.2px solid #eaeaea; padding-bottom: 4px; margin-top: 25px; font-size: 19pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
h3 { color: #444; margin-top: 18px; font-size: 15pt; font-weight: 600; border-left: 5px solid #000; padding-left: 12px; }
p { margin: 10px 0; font-size: 11.5pt; color: #333; }
ul { margin: 8px 0; padding-left: 22px; }
li { margin: 5px 0; font-size: 11pt; color: #444; }
strong { color: #000; font-weight: 700; }
a { color: #0060df; text-decoration: none; border-bottom: 1px solid transparent; }
a:hover { border-bottom: 1px solid #0060df; }
hr { border: 0; border-top: 2px solid #111; margin: 30px 0; }
.seal { text-align: right; font-style: italic; color: #999; font-size: 8.5pt; margin-top: 40px; border-top: 1px solid #eee; padding-top: 10px; }
@media print {
    body { padding: 30px; box-shadow: none; font-size: 10.5pt; }
    h1 { font-size: 22pt; margin-top: 10px; }
    .no-print { display: none; }
    @page { margin: 1.2cm; }
}
"""

def md_to_html_robust(md):
    lines = md.split('\n')
    html_lines = []
    in_list = False
    for line in lines:
        line = line.strip()
        if not line:
            if in_list: html_lines.append("</ul>"); in_list = False
            continue
            
        if line.startswith('# '):
            if in_list: html_lines.append("</ul>"); in_list = False
            html_lines.append(f"<h1>{line[2:].strip()}</h1>")
        elif line.startswith('## '):
            if in_list: html_lines.append("</ul>"); in_list = False
            html_lines.append(f"<h2>{line[3:].strip()}</h2>")
        elif line.startswith('### '):
            if in_list: html_lines.append("</ul>"); in_list = False
            html_lines.append(f"<h3>{line[4:].strip()}</h3>")
        elif line == "---" or line.startswith("---"):
            if in_list: html_lines.append("</ul>"); in_list = False
            html_lines.append("<hr>")
        elif line.startswith('- '):
            if not in_list: html_lines.append("<ul>"); in_list = True
            content = line[2:].strip()
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', content)
            html_lines.append(f"<li>{content}</li>")
        else:
            if in_list: html_lines.append("</ul>"); in_list = False
            content = line
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', content)
            html_lines.append(f"<p>{content}</p>")
            
    if in_list: html_lines.append("</ul>")
    return "\n".join(html_lines)

def main():
    print("🚀 [MISSION] STARTING DEFINITIVE CV REBUILD...")
    
    for d in [HTML_DIR, PDF_DIR]:
        if not os.path.exists(d): os.makedirs(d)
        
    categories = [
        "01-Web3-Solana", "02-Eth-Base", "03-Mobile-Flutter", "04-AI-Automation",
        "05-GameFi-Degen", "06-Community-Growth", "07-Web3-Strategy", "08-Fintech-Payments"
    ]
    
    total_generated = 0
    
    for cat in categories:
        cat_path = os.path.join(MASTER_DIR, cat)
        if not os.path.exists(cat_path):
            print(f"⚠️ [SKIP] Category not found: {cat}")
            continue
            
        print(f"📁 [DIR] Entering: {cat}")
        for file in os.listdir(cat_path):
            if file.endswith(".md"):
                md_path = os.path.join(cat_path, file)
                print(f"  📝 [BUILD] {file}...")
                
                with open(md_path, 'r', encoding='utf-8') as f:
                    md_text = f.read()
                
                html_body = md_to_html_robust(md_text)
                html_full = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{html_body}<div class='seal'>OFFICIAL CV ARTIFACT | @nayrbryanGaming</div></body></html>"
                
                html_name = file.replace(".md", ".html")
                html_path = os.path.join(HTML_DIR, html_name)
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(html_full)
                
                pdf_name = file.replace(".md", ".pdf")
                pdf_path = os.path.join(PDF_DIR, pdf_name)
                
                try:
                    subprocess.run([
                        EDGE_PATH, "--headless", f"--print-to-pdf={pdf_path}", 
                        "--no-pdf-header-footer", "--disable-gpu", html_path
                    ], check=True, capture_output=True, timeout=30)
                    if os.path.exists(pdf_path):
                        print(f"    ✅ SUCCESS: {pdf_name}")
                        total_generated += 1
                    else:
                        print(f"    ❌ FAILED: {pdf_name} [File missing]")
                except Exception as e:
                    print(f"    ❌ ERROR: {str(e)}")

    print(f"\n✅ [COMPLETE] {total_generated}/16 Artifacts Deployed to {PDF_DIR}")

if __name__ == "__main__":
    main()
