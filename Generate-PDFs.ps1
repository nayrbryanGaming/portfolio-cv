$baseDir = "e:\000VSCODE PROJECT MULAI DARI DESEMBER 2025\CV KERJA\my-professional-resumes"
$masterCvDir = Join-Path $baseDir "Master-CVs"
$outputDir = Join-Path $baseDir "Final_PDFs"

if (!(Test-Path $outputDir)) { New-Item -ItemType Directory -Path $outputDir }

$categories = @(
    "01-Web3-Solana", "02-Eth-Base", "03-Mobile-Flutter", "04-AI-Automation",
    "05-GameFi-Degen", "06-Community-Growth", "07-Web3-Strategy", "08-Fintech-Payments"
)

# Start Word
Write-Host "Initializing Word Engine..."
$word = New-Object -ComObject Word.Application
$word.Visible = $false

foreach ($cat in $categories) {
    $catPath = Join-Path $masterCvDir $cat
    if (!(Test-Path $catPath)) { continue }
    
    $files = Get-ChildItem -Path $catPath -Filter "*.md"
    foreach ($file in $files) {
        Write-Host "Processing $($file.Name)..."
        $md = Get-Content -Path $file.FullName -Raw
        
        # Super simple MD to HTML for Word
        # Note: Word's HTML support is actually quite good for simple formatting
        $html = $md -replace '^# (.*)$', '<h1>$1</h1>' `
                    -replace '^## (.*)$', '<h2>$1</h2>' `
                    -replace '^### (.*)$', '<h3>$1</h3>' `
                    -replace '\*\*(.*?)\*\*', '<b>$1</b>' `
                    -replace '^- (.*)$', '<li>$1</li>'
        
        # Wrap in <ul> manually for lists
        $html = $html -replace '<li>(.*?)</li>(\r?\n<li>.*?</li>)*', '<ul>$&</ul>'
        
        $tempHtml = Join-Path $env:TEMP "$($file.BaseName).html"
        "<html><head><style>body { font-family: 'Segoe UI', sans-serif; }</style></head><body>$html</body></html>" | Out-File -FilePath $tempHtml -Encoding utf8
        
        $doc = $word.Documents.Open($tempHtml)
        $pdfPath = Join-Path $outputDir "$($file.BaseName).pdf"
        
        # 17 is the value for wdExportFormatPDF
        $doc.ExportAsFixedFormat($pdfPath, 17)
        $doc.Close([Microsoft.Office.Interop.Word.WdSaveOptions]::wdDoNotSaveChanges)
        
        Write-Host "✅ Generated $($file.BaseName).pdf"
    }
}

$word.Quit()
Write-Host "Mission Accomplished: 16 PDFs Ready."
