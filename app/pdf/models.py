from dataclasses import dataclass


@dataclass
class DocumentPage:
    page_number: int
    text: str