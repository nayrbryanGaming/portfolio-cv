import os
import markdown2
from fpdf import FPDF, HTMLMixin

class MyPDF(FPDF, HTMLMixin):
    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_pdf(md_file_path, pdf_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert MD to HTML (fpdf2 likes simple tags)
    html_content = markdown2.markdown(md_content)
    
    # Clean up some HTML that fpdf2 might struggle with
    html_content = html_content.replace('<hr />', '<br><hr><br>')
    
    pdf = MyPDF()
    pdf.add_page()
    pdf.set_font('helvetica', '', 10)
    
    # Add a header for premium feel
    pdf.set_font('helvetica', 'B', 16)
    # pdf.write_html(html_content)
    
    # Actually, let's use a simpler approach for the PDF layout
    # fpdf2's html support is limited, so we'll do basic parsing
    
    try:
        pdf.write_html(html_content)
    except Exception as e:
        print(f"Error converting {md_file_path}: {e}")
        # Fallback to plain text if HTML fails
        pdf.set_font('helvetica', '', 10)
        pdf.multi_cell(0, 10, md_content)

    pdf.output(pdf_file_path)

def main():
    base_dir = r"e:\000VSCODE PROJECT MULAI DARI DESEMBER 2025\CV KERJA\my-professional-resumes"
    master_cv_dir = os.path.join(base_dir, "Master-CVs")
    output_dir = os.path.join(base_dir, "PDF_Export")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    categories = [
        '01-Web3-Solana', '02-Eth-Base', '03-Mobile-Flutter', '04-AI-Automation',
        '05-GameFi-Degen', '06-Community-Growth', '07-Web3-Strategy', '08-Fintech-Payments'
    ]
    
    for cat in categories:
        cat_path = os.path.join(master_cv_dir, cat)
        if not os.path.exists(cat_path): continue
        
        for file in os.listdir(cat_path):
            if file.endswith('.md'):
                md_path = os.path.join(cat_path, file)
                pdf_name = file.replace('.md', '.pdf')
                pdf_path = os.path.join(output_dir, pdf_name)
                
                print(f"Generating PDF for {file}...")
                generate_pdf(md_path, pdf_path)
                print(f"Successfully generated {pdf_name}")

if __name__ == "__main__":
    main()
