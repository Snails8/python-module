import subprocess

def compression_pdf():
    result_pwd = subprocess.run(["pwd"], capture_output=True)
    current_dir = result_pwd.stdout.decode().strip()
    
    pdf_path = "data/pdf/sample.pdf"
    output_path = "data/pdf/sample.pdf"
    quality = "/ebook"
    
    cmd  = f"gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS={quality} -dNOPAUSE -dQUIET -dBATCH -sOutputFile={output_path} {pdf_path}"
    r = subprocess.run(cmd, capture_output=True, cwd=current_dir, shell=True)
    
    print("cmd", r.args)
    print("標準エラー出力", r.stderr)
    
    return 