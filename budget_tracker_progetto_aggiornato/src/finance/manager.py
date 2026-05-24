from datetime import datetime

def add_transaction(transactions: list, tipo: str, categoria: str, importo: float, data: str, descrizione: str) -> list:
    if not transactions:
        nuovo_id = 1
    else:
        nuovo_id = max(t["id"] for t in transactions) + 1
    nuova_transazione = {
        "id": nuovo_id, "data": data, "tipo": tipo, "categoria": categoria, "importo": round(importo, 2), "descrizione": descrizione
    }
    transactions.append(nuova_transazione)
    return transactions

def delete_transaction(transactions: list, transaction_id: int) -> tuple:
    for t in transactions:
        if t["id"] == transaction_id:
            transactions.remove(t)
            return transactions, True
    return transactions, False

def filter_by_month(transactions: list, year: int, month: int) -> list:
    risultato = []
    for t in transactions:
        try:
            data_oggetto = datetime.strptime(t["data"], "%Y-%m-%d")
            if data_oggetto.year == year and data_oggetto.month == month:
                risultato.append(t)
        except ValueError:
            continue
    return risultato

def get_monthly_totals(monthly_transactions: list) -> dict:
    totale_entrate = 0.0
    totale_uscite = 0.0
    categorie_uscite = {}
    for t in monthly_transactions:
        if t["tipo"] == "entrata":
            totale_entrate += t["importo"]
        elif t["tipo"] == "uscita":
            totale_uscite += t["importo"]
            cat = t["categoria"]
            categorie_uscite[cat] = categorie_uscite.get(cat, 0.0) + t["importo"]
    return {
        "entrate": round(totale_entrate, 2), "uscite": round(totale_uscite, 2),
        "risparmio": round(totale_entrate - totale_uscite, 2), "categorie": categorie_uscite
    }

def get_annual_report(transactions: list, year: int) -> dict:
    report_anno = {m: {"entrate": 0.0, "uscite": 0.0} for m in range(1, 13)}
    for t in transactions:
        try:
            data_oggetto = datetime.strptime(t["data"], "%Y-%m-%d")
            if data_oggetto.year == year:
                mese = data_oggetto.month
                if t["tipo"] == "entrata":
                    report_anno[mese]["entrate"] += t["importo"]
                elif t["tipo"] == "uscita":
                    report_anno[mese]["uscite"] += t["importo"]
        except ValueError:
            continue
    return report_anno
