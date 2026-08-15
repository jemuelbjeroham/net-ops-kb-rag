import pymupdf

with pymupdf.open("sample_data/firewall_operations.pdf") as pdf:
    for page in pdf:
        text = page.get_text("text")

        print(f"\nPage {page.number + 1}")
        print(f"Characters: {len(text)}")
        print(text[:100])