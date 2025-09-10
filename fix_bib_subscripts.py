import re
import sys
from pathlib import Path

# regex: detects things like CO2, TiO2, Fe2O3, Nb2O5, etc.
pattern = re.compile(r'([A-Za-z]+)(\d+)')

def fix_subscripts(text: str) -> str:
    return pattern.sub(r'\1<sub>\2</sub>', text)

def process_bib_file(input_file: str, output_file: str):
    content = Path(input_file).read_text(encoding="utf-8")
    fixed_content = fix_subscripts(content)
    Path(output_file).write_text(fixed_content, encoding="utf-8")
    print(f"✅ Fixed file saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python fix_bib_subscripts.py input.bib output.bib")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_bib_file(input_file, output_file)

