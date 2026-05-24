import os
import sys

# Aggiunge il path corrente alla ricerca dei moduli per permettere l'importazione
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.storage import load_data, save_data
from finance.manager import add_transaction, delete_transaction, filter_by_month, get_monthly_totals, get_annual_report
from ui.menu import main_menu, monthly_menu, get_transaction_inputs, display_monthly_table, display_annual_report
from ui.charts import show_pie_chart
from datetime import datetime
from dateutil.relativedelta import relativedelta

DB_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "transactions.json")

def main():
    transactions = load_data(DB_FILE)
    oggi = datetime.now()
    view_year = oggi.year
    view_month = oggi.month

    while True:
        scelta_p = main_menu()

        if scelta_p == "1" or scelta_p == "2":
            if scelta_p == "2":
                try:
                    view_year = int(input("Inserisci l'anno (es. 2026): "))
                    view_month = int(input("Inserisci il numero del mese (1-12): "))
                    if not (1 <= view_month <= 12):
                        print("[Errore] Mese non valido! Reimpostato mese corrente.")
                        view_year, view_month = oggi.year, oggi.month
                except ValueError:
                    print("[Errore] Input numerico non valido! Reimpostato mese corrente.")
                    view_year, view_month = oggi.year, oggi.month

            while True:
                transazioni_mese = filter_by_month(transactions, view_year, view_month)
                totali_mese = get_monthly_totals(transazioni_mese)
                scelta_m = monthly_menu(view_year, view_month)

                if scelta_m == "1":
                    display_monthly_table(transazioni_mese, totali_mese, f"Transazioni di {view_month}/{view_year}")
                elif scelta_m == "2":
                    giorno_default = "01" if view_month != oggi.month or view_year != oggi.year else oggi.strftime("%d")
                    data_default = f"{view_year}-{str(view_month).zfill(2)}-{giorno_default}"
                    tipo, cat, imp, data, desc = get_transaction_inputs(data_default)
                    transactions = add_transaction(transactions, tipo, cat, imp, data, desc)
                    print("\n[Ok] Transazione aggiunta con successo!")
                    save_data(DB_FILE, transactions)
                elif scelta_m == "3":
                    try:
                        id_canc = int(input("Inserisci l'ID della transazione da eliminare: "))
                        transactions, successo = delete_transaction(transactions, id_canc)
                        if successo:
                            print(f"\n[Ok] Transazione con ID {id_canc} eliminata.")
                            save_data(DB_FILE, transactions)
                        else:
                            print(f"\n[Errore] Nessuna transazione trovata con l'ID {id_canc}.")
                    except ValueError:
                        print("\n[Errore] L'ID deve essere un numero intero.")
                elif scelta_m == "4":
                    show_pie_chart(totali_mese["categorie"], f"Spese per Categoria - {view_month}/{view_year}")
                elif scelta_m == "5":
                    data_corrente = datetime(view_year, view_month, 1)
                    nuova_data = data_corrente - relativedelta(months=1)
                    view_year, view_month = nuova_data.year, nuova_data.month
                elif scelta_m == "6":
                    data_corrente = datetime(view_year, view_month, 1)
                    nuova_data = data_corrente + relativedelta(months=1)
                    view_year, view_month = nuova_data.year, nuova_data.month
                elif scelta_m == "7":
                    break

        elif scelta_p == "3":
            try:
                anno_rep = int(input("Di quale anno vuoi il report? (es. 2026): "))
                report_anno = get_annual_report(transactions, anno_rep)
                display_annual_report(report_anno, anno_rep)
                
                # --- Generazione del grafico per il report annuale (CORRETTO) ---
                spese_annuali_reg = {}
                for t in transactions:
                    try:
                        # Rimosso il 'from datetime import datetime' locale che creava il bug
                        data_oggetto = datetime.strptime(t["data"], "%Y-%m-%d")
                        if data_oggetto.year == anno_rep and t["tipo"] == "uscita":
                            cat = t["categoria"]
                            spese_annuali_reg[cat] = spese_annuali_reg.get(cat, 0.0) + t["importo"]
                    except ValueError:
                        continue
                
                if spese_annuali_reg:
                    show_pie_chart(spese_annuali_reg, f"Spese per Categoria - Intero Anno {anno_rep}")

            except ValueError:
                print("[Errore] Inserisci un anno valido.")
                
        elif scelta_p == "4":
            save_data(DB_FILE, transactions)
            print("\nGrazie per aver usato il Gestore Finanze. Arrivederci!")
            break

if __name__ == "__main__":
    main()
