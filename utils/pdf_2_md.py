from pathlib import Path
from typing import Union
from markitdown import MarkItDown


def pdf_2_md(pdf_path: Union[str, Path]) -> str:
    """
    Converts a PDF file to markdown text.
    """
    converter = MarkItDown()
    result = converter.convert(str(pdf_path))
    return result.text_content


def convert_pdf_file(pdf_path: Union[str, Path], output_path: Union[str, Path] = None) -> Path:
    """
    Converts a single PDF file and writes the markdown output to disk.
    """
    pdf_path = Path(pdf_path)
    if output_path is None:
        output_path = pdf_path.with_suffix(".md")
    else:
        output_path = Path(output_path)

    md_content = pdf_2_md(pdf_path)
    output_path.write_text(md_content, encoding="utf-8")
    return output_path


def convert_directory_pdfs(dir_path: Union[str, Path]) -> list[Path]:
    """
    Converts all PDF files located in the target directory to markdown files.
    """
    dir_path = Path(dir_path)
    pdf_files = list(dir_path.glob("*.pdf"))
    converted_files = []

    for pdf_file in pdf_files:
        out_file = convert_pdf_file(pdf_file)
        converted_files.append(out_file)
        print(f"Converted: {pdf_file.name} -> {out_file.name}")

    return converted_files


if __name__ == "__main__":
    # Resolve repository root relative to utils directory
    base_dir = Path(__file__).resolve().parent.parent
    general_research_dir = base_dir / "general_research"

    print(f"Starting conversion for directory: {general_research_dir}")
    converted = convert_directory_pdfs(general_research_dir)
    print(f"Total files converted: {len(converted)}")