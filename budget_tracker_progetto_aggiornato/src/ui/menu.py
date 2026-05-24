import questionary
from rich.console import Console
from rich.table import Table
from datetime import datetime

console = Console()

def main_menu() -> str:
    console.print("\n=== 💰 GESTORE FINANZE PERSONALI 💰 ===", style="bold cyan")
    scelta = questionary.select(
        "Cosa vuoi fare?",
        choices=[
            "1. Gestisci mese corrente",
            "2. Seleziona un mese/anno specifico",
            "3. Visualizza Resoconto Annuale",
            "4. Esci dal programma"
        ]
    ).ask()
    return scelta[0]

def monthly_menu(year: int, month: int) -> str:
    mesi_ita = ["", "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", 
                "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
    console.print(f"\n--- 📅 MENU DI {mesi_ita[month].upper()} {year} ---", style="bold yellow")
    scelta = questionary.select(
        "Scegli un'azione:",
        choices=[
            "1. Visualizza transazioni e riepilogo",
            "2. Aggiungi Entrata o Uscita",
            "3. Elimina una transazione (tramite ID)",
            "4. Mostra Grafico a Torta delle Spese",
            "5. ⬅️ Mese Precedente",
            "6. ➡️ Mese Successivo",
            "7. ↩️ Torna al Menu Principale"
        ]
    ).ask()
    return scelta[0]

def get_transaction_inputs(default_date: str):
    tipo = questionary.select("Tipo:", choices=["entrata", "uscita"]).ask()
    cat = questionary.text("Categoria:").ask()
    
    # --- VALIDAZIONE ROBUSTA DELL'IMPORTO ---
    while True:
        imp_str = questionary.text("Importo:").ask()
        try:
            # Sostituisce l'eventuale virgola con il punto decimale
            imp = float(imp_str.replace(",", "."))
            if imp <= 0:
                console.print("[Errore] L'importo deve essere maggiore di zero.", style="bold red")
                continue
            break
        except ValueError:
            console.print("[Errore] Inserisci un numero decimale valido (es. 15.50).", style="bold red")
            
    data = questionary.text("Data (AAAA-MM-GG):", default=default_date).ask()
    desc = questionary.text("Descrizione:").ask()
    return tipo, cat, imp, data, desc

def display_monthly_table(transactions, totals, title):
    table = Table(title=title)
    table.add_column("ID", justify="center")
    table.add_column("Data", justify="center")
    table.add_column("Tipo", justify="center")
    table.add_column("Categoria")
    table.add_column("Importo", justify="right")
    table.add_column("Descrizione")
    for t in transactions:
        table.add_row(str(t["id"]), t["data"], t["tipo"], t["categoria"], f"{t['importo']:.2f} €", t["descrizione"])
    console.print(table)
    console.print(f"Totale Entrate: {totals['entrate']:.2f} €")
    console.print(f"Totale Uscite: {totals['uscite']:.2f} €")
    console.print(f"Totale: {totals['risparmio']:.2f} €")

def display_annual_report(report_anno, year):
    table = Table(title=f"Rapporto Annuale - {year}")
    table.add_column("Mese", style="cyan")
    table.add_column("Entrate", justify="right", style="green")
    table.add_column("Uscite", justify="right", style="red")
    table.add_column("Risparmio", justify="right")
    
    mesi_ita = ["", "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", 
                "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
    
    tot_entrate = 0.0
    tot_uscite = 0.0
    
    for m in range(1, 13):
        entrate = report_anno[m]["entrate"]
        uscite = report_anno[m]["uscite"]
        risparmio = entrate - uscite
        
        tot_entrate += entrate
        tot_uscite += uscite
        
        stile_risp = "green" if risparmio >= 0 else "red"
        table.add_row(
            mesi_ita[m], 
            f"{entrate:.2f} €", 
            f"{uscite:.2f} €", 
            f"[{stile_risp}]{risparmio:.2f} €[/{stile_risp}]"
        )
    
    # --- AGGIUNTA RIGA FINALE CON I TOTALI COMPLESSIVI ---
    table.add_section()
    tot_risparmio = tot_entrate - tot_uscite
    stile_tot_risp = "bold green" if tot_risparmio >= 0 else "bold red"
    
    table.add_row(
        f"[{stile_tot_risp}]TOTALE[/{stile_tot_risp}]", 
        f"[bold green]{tot_entrate:.2f} €[/bold green]", 
        f"[bold red]{tot_uscite:.2f} €[/bold red]", 
        f"[{stile_tot_risp}]{tot_risparmio:.2f} €[/{stile_tot_risp}]", 
        
    )
    
    console.print(table)