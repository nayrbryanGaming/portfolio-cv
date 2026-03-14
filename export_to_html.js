const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

// Premium CSS Template
const css = `
    body { 
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; 
        line-height: 1.6; 
        color: #1a1a1a; 
        max-width: 850px; 
        margin: 40px auto; 
        padding: 40px; 
        background-color: #ffffff;
        box-shadow: 0 0 20px rgba(0,0,0,0.05);
    }
    h1 { font-size: 2.2em; color: #111; margin-bottom: 0.2em; border-bottom: 2px solid #333; padding-bottom: 10px; }
    h2 { font-size: 1.5em; margin-top: 1.5em; color: #333; border-bottom: 1px solid #eee; }
    h3 { font-size: 1.2em; margin-top: 1.2em; color: #444; }
    p, li { font-size: 1.05em; color: #444; }
    strong { color: #000; font-weight: 700; }
    hr { border: 1px solid #eee; margin: 30px 0; }
    code { background: #f8f8f8; padding: 2px 5px; border-radius: 4px; font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; }
    a { color: #0066cc; text-decoration: none; }
    a:hover { text-decoration: underline; }
    ul { padding-left: 20px; }
    li { margin-bottom: 8px; }
    @media print {
        body { box-shadow: none; margin: 0; padding: 20px; }
        .no-print { display: none; }
    }
`;

const categories = [
    '01-Web3-Solana', '02-Eth-Base', '03-Mobile-Flutter', '04-AI-Automation',
    '05-GameFi-Degen', '06-Community-Growth', '07-Web3-Strategy', '08-Fintech-Payments'
];

async function generate() {
    const exportDir = path.join(__dirname, 'Exported_HTML');
    if (!fs.existsSync(exportDir)) fs.mkdirSync(exportDir);

    for (const cat of categories) {
        const catPath = path.join(__dirname, 'Master-CVs', cat);
        const files = fs.readdirSync(catPath).filter(f => f.endsWith('.md'));

        for (const file of files) {
            const content = fs.readFileSync(path.join(catPath, file), 'utf8');
            const htmlContent = marked.parse(content);
            const finalHtml = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>${file.replace('.md', '')}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>${css}</style>
</head>
<body>
    <div class="no-print" style="background: #f0f0f0; padding: 10px; margin-bottom: 20px; text-align: center; border-radius: 8px;">
        💡 <b>Boss Mode Activated:</b> Open this file in your browser and press <b>Ctrl + P</b> (Print to PDF) for a premium CV!
    </div>
    ${htmlContent}
</body>
</html>`;
            fs.writeFileSync(path.join(exportDir, file.replace('.md', '.html')), finalHtml);
            console.log(`✅ Exported: ${file.replace('.md', '.html')}`);
        }
    }
}

generate();
