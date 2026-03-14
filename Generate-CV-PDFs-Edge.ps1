$baseDir = "e:\000VSCODE PROJECT MULAI DARI DESEMBER 2025\CV KERJA\my-professional-resumes"
$masterCvDir = Join-Path $baseDir "Master-CVs"
$outputDir = Join-Path $baseDir "Exported_PDFs"
$htmlDir = Join-Path $baseDir "Internal_HTML"

if (!(Test-Path $outputDir)) { New-Item -ItemType Directory -Path $outputDir }
if (!(Test-Path $htmlDir)) { New-Item -ItemType Directory -Path $htmlDir }

$edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if (!(Test-Path $edgePath)) {
    $edgePath = "msedge" # Fallback to path
}

$categories = @(
    "01-Web3-Solana", "02-Eth-Base", "03-Mobile-Flutter", "04-AI-Automation",
    "05-GameFi-Degen", "06-Community-Growth", "07-Web3-Strategy", "08-Fintech-Payments"
)

$CSS = @"
body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.4; color: #333; max-width: 800px; margin: 0 auto; padding: 40px; }
h1 { color: #1a1a1a; border-bottom: 2px solid #1a1a1a; padding-bottom: 5px; margin-top: 20px; font-size: 24pt; }
h2 { color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 3px; margin-top: 15px; font-size: 18pt; }
h3 { color: #34495e; margin-top: 10px; font-size: 14pt; }
p { margin: 8px 0; font-size: 11pt; }
ul { margin: 8px 0; padding-left: 20px; }
li { margin: 4px 0; font-size: 11pt; }
strong { color: #000; font-weight: bold; }
a { color: #2980b9; text-decoration: none; }
hr { border: 0; border-top: 1px solid #ddd; margin: 20px 0; }
@media print {
    body { padding: 0; }
    @page { margin: 1cm; }
}
"@

foreach ($cat in $categories) {
    $catPath = Join-Path $masterCvDir $cat
    if (!(Test-Path $catPath)) { continue }
    
    $files = Get-ChildItem -Path $catPath -Filter "*.md"
    foreach ($file in $files) {
        $md = Get-Content -Path $file.FullName -Raw
        
        # Simple MD to HTML
        $body = $md -replace '^# (.*)$', '<h1>$1</h1>' `
                    -replace '^## (.*)$', '<h2>$1</h2>' `
                    -replace '^### (.*)$', '<h3>$1</h3>' `
                    -replace '\*\*(.*?)\*\*', '<strong>$1</strong>' `
                    -replace '^- (.*)$', '<li>$1</li>' `
                    -replace '\[(.*?)\]\((.*?)\)', '<a href="$2">$1</a>'
        
        # Crude list wrapping
        $body = $body -replace '<li>(.*?)</li>(\r?\n<li>.*?</li>)*', '<ul>$&</ul>'
        $body = $body -replace '(\r?\n){2,}', '<br>'
        
        $htmlFile = Join-Path $htmlDir "$($file.BaseName).html"
        $pdfFile = Join-Path $outputDir "$($file.BaseName).pdf"
        
        "<!DOCTYPE html><html><head><meta charset='UTF-8'><style>$CSS</style></head><body>$body</body></html>" | Out-File -FilePath $htmlFile -Encoding utf8
        
        Write-Host "Converting $($file.Name) to PDF..."
        Start-Process -FilePath $edgePath -ArgumentList "--headless", "--print-to-pdf=$pdfFile", "--no-pdf-header-footer", $htmlFile -Wait
    }
}

Write-Host "Conversion Complete. Check the Exported_PDFs folder."
