import os
from pdf_parser import text_extract_from_page
from re_parser import parse_budget_codes

pdf_path = os.path.join("data", "Prilozhenie_2_k_prikazu_70n.pdf")
pages_texts = text_extract_from_page(pdf_path, 10000)


for p_tx in pages_texts:
    print(p_tx)
    result = parse_budget_codes(p_tx)
    print(result)

