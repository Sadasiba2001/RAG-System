import re
import pymupdf

MIN_TEXT_LENGTH = 1

def load_pdf(file_path: str) -> list[dict]:

    document = pymupdf.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        raw_text = page.get_text()
        cleaned_text = clean_text(raw_text)

        pages.append(
            {
                "page_number": page_number,
                "text": cleaned_text,
            }
        )

    document.close()

    return pages


def clean_text(text: str) -> str:

    text = re.sub(r"\s+", " ", text)
    
    text = re.sub(
        r"\b(?:[A-Za-z]\s+){2,}[A-Za-z]\b",
        lambda match: match.group(0).replace(" ", ""),
        text,
    )

    return text.strip()


def has_extractable_text(pages: list[dict]) -> bool:
    total_text_length = sum(len(page["text"]) for page in pages)

    return total_text_length >= MIN_TEXT_LENGTH