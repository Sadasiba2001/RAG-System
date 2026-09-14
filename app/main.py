import sys
from pathlib import Path

from app.chunking.splitter import split_text
from app.pdf.loader import has_extractable_text, load_pdf


CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m app.main <pdf_path>")
        return

    pdf_path = Path(sys.argv[1])

    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}")
        return

    if pdf_path.suffix.lower() != ".pdf":
        print("Please provide a PDF file.")
        return

    pages = load_pdf(str(pdf_path))

    if not has_extractable_text(pages):
        print("No extractable text found in the PDF.")
        print("The PDF may be scanned or image-based.")
        return

    source = pdf_path.name

    all_chunks = []

    for page in pages:
        chunks = split_text(
            page["text"],
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )

        for chunk in chunks:
            all_chunks.append(
                {
                    "text": chunk,
                    "metadata": {
                        "source": source,
                        "page_number": page["page_number"],
                    },
                }
            )

    print(f"PDF: {source}")
    print(f"Total pages: {len(pages)}")
    print(f"Total chunks: {len(all_chunks)}")

    for index, chunk in enumerate(all_chunks, start=1):
        print(f"\n--- Chunk {index} ---")
        print(f"Source: {chunk['metadata']['source']}")
        print(f"Page: {chunk['metadata']['page_number']}")
        print(f"Text: {chunk['text']}")


if __name__ == "__main__":
    main()