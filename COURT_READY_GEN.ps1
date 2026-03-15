$base = "e:\000VSCODE PROJECT MULAI DARI DESEMBER 2025\CV KERJA\my-professional-resumes"
$masterDir = Join-Path $base "Master-CVs"
$htmlDir = Join-Path $base "COURT_HTML_ASSETS"
$pdfDir = Join-Path $base "OFFICIAL_COURT_PDFS"
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

if (!(Test-Path $htmlDir)) { New-Item -ItemType Directory -Path $htmlDir }
if (!(Test-Path $pdfDir)) { New-Item -ItemType Directory -Path $pdfDir }

$CSS = "@
body { font-family: 'Segoe UI', sans-serif; line-height: 1.4; color: #111; max-width: 800px; margin: 0 auto; padding: 40px; background: #fff; }
h1 { color: #000; border-bottom: 4px solid #000; padding-bottom: 8px; margin-top: 30px; font-size: 26pt; font-weight: 800; }
h2 { color: #333; border-bottom: 1.5px solid #eaeaea; padding-bottom: 5px; margin-top: 25px; font-size: 19pt; font-weight: 700; text-transform: uppercase; }
h3 { color: #444; margin-top: 20px; font-size: 15pt; font-weight: 600; border-left: 6px solid #000; padding-left: 12px; }
p { margin: 10px 0; font-size: 11.5pt; }
ul { margin: 10px 0; padding-left: 25px; }
li { margin: 6px 0; font-size: 11pt; }
strong { color: #000; font-weight: 700; }
a { color: #006ce0; text-decoration: none; }
.seal { text-align: right; font-style: italic; color: #999; font-size: 8pt; margin-top: 40px; border-top: 1px solid #eee; padding-top: 10px; }
@media print { body { padding: 30px; } @page { margin: 1cm; } }
@"

function Write-PremiumHtml($mdText, $title) {
    # Simple MD to HTML
    $body = $mdText -replace '^# (.*)$', '<h1>$1</h1>' `
                    -replace '^## (.*)$', '<h2>$1</h2>' `
                    -replace '^### (.*)$', '<h3>$1</h3>' `
                    -replace '\*\*(.*?)\*\*', '<strong>$1</strong>' `
                    -replace '^- (.*)$', '<li>$1</li>' `
                    -replace '\[(.*?)\]\((.*?)\)', '<a href="$2">$1</a>'
    
    # Wrap lists
    $body = $body -replace '<li>(.*?)</li>(\r?\n<li>.*?</li>)*', '<ul>$&</ul>'
    $body = $body -replace '(\r?\n){2,}', '<p>'
    
    return "<!DOCTYPE html><html><head><meta charset='utf-8'><title>$title</title><style>$CSS</style></head><body>$body<div class='seal'>OFFICIAL CV | @nayrbryanGaming</div></body></html>"
}

Write-Host "[MISSION] STARTING 16-CV PRODUCTION..."

$files = Get-ChildItem -Path $masterDir -Filter *.md -Recurse
foreach ($f in $files) {
    Write-Host "[BUILD] $($f.BaseName)..."
    $md = Get-Content -Path $f.FullName -Raw
    $html = Write-PremiumHtml $md $f.BaseName
    
    $htmlPath = Join-Path $htmlDir ($f.BaseName + ".html")
    $pdfPath = Join-Path $pdfDir ($f.BaseName + ".pdf")
    
    $html | Out-File -FilePath $htmlPath -Encoding utf8
    
    # EDGE CONVERSION
    & $edge --headless --print-to-pdf="$pdfPath" --no-pdf-header-footer --disable-gpu "$htmlPath"
    
    if (Test-Path $pdfPath) {
        Write-Host "  ✅ SUCCESS."
    } else {
        Write-Host "  ❌ FAILED."
    }
}

Write-Host "[COMPLETE] 16 PREMIUM CVs READY IN OFFICIAL_COURT_PDFS."
