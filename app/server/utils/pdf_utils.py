import pdfkit

def report_generation(filename: str, scan,name:str):
    # Generate HTML content
    html_content = f"<html><head><h3>{name}</h3></head><body>"
    for line in scan:
        html_content += f"<p>{line}</p>"
    html_content += "</body></html>"

    # Save HTML to a file
    html_filename = f"{filename}.html"
    with open(html_filename, "w") as file:
        file.write(html_content)

    # Generate PDF from HTML
    pdf_filename = f"{filename}.pdf"
    pdfkit.from_file(html_filename, pdf_filename)

    return pdf_filename
