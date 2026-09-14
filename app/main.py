from app.pdf.loader import load_pdf, has_extractable_text
from app.chunking.splitter import split_text

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

def main():
    pdf_path = "data/uploads/Sadasiba_Baliyarsing_Cover_Letter.pdf"
    # pdf_path = "data/uploads/Doc1.pdf"
    

    pages = load_pdf(pdf_path)

    if not has_extractable_text(pages):
        print("No extractable text found in the PDF.")
        print("The PDF may be scanned or image-based.")
        return

    for page in pages:
        
        chunks = split_text(
            page["text"], 
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            )
        
        print(f"\n--- Page {page['page_number']} ---")
        print(page["text"])
        
        for index, chunk in enumerate(chunks, start=1):
            print(f"\nChunk {index}:")
            print(chunk)


if __name__ == "__main__":
    main()
    