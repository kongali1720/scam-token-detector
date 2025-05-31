# scam_detector.py
import sys
from rich.console import Console
from utils import fetch_contract_source

console = Console()

def analyze_contract_code(source_code: str):
    """
    Analisa source code untuk tanda-tanda scam/honeypot sederhana.
    Contoh: cari fungsi 'transfer' yang bermasalah, 'hidden fees', dll.
    """
    warnings = []
    if "transfer" not in source_code:
        warnings.append("Contract tidak mengandung fungsi transfer yang valid!")
    if "honeypot" in source_code.lower():
        warnings.append("Potensi Honeypot ditemukan dalam kode!")
    # Contoh cek sederhana lainnya bisa ditambah
    return warnings

def main():
    console.print("[bold cyan]🛡️ Scam Token Detector CLI[/bold cyan]\n")

    if len(sys.argv) < 3:
        console.print("[red]Usage: python scam_detector.py <ethereum|bsc> <contract_address>[/red]")
        sys.exit(1)

    chain = sys.argv[1].lower()
    contract_address = sys.argv[2]

    console.print(f"🔍 Memeriksa contract: [bold]{contract_address}[/bold] di [bold]{chain}[/bold] blockchain...\n")

    source_code = fetch_contract_source(chain, contract_address)
    if not source_code:
        console.print("[red]Gagal mengambil source code contract. Pastikan alamat dan API key benar.[/red]")
        sys.exit(1)

    console.print("[green]Source code contract berhasil diambil![/green]\n")
    warnings = analyze_contract_code(source_code)
    if warnings:
        console.print("[bold red]⚠️ Potensi masalah ditemukan:[/bold red]")
        for w in warnings:
            console.print(f"- {w}")
    else:
        console.print("[bold green]✅ Tidak ditemukan potensi scam/honeypot dari analisa awal.[/bold green]")

if __name__ == "__main__":
    main()
