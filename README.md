# 💰 Gestore Finanze Personali (Budget Tracker)

Un'applicazione Python da riga di comando (CLI) pulita, interattiva e moderna, progettata per tracciare le entrate, monitorare le uscite divise per categoria e generare resoconti statistici dettagliati sia in formato tabellare che grafico.

## 🚀 Caratteristiche Principali

- **Gestione Mensile Avanzata:** Visualizza bilanci, aggiungi entrate/uscite ed elimina transazioni con calcoli automatici dei risparmi.
- **Interfaccia Utente Dinamica (CLI):** Menu di selezione interattivi gestibili con le frecce direzionali.
- **Visualizzazione ad Alto Impatto:** Tabelle colorate nel terminale per differenziare a colpo d'occhio entrate e uscite.
- **Grafici Statistici incorporati:** Generazione automatica di grafici a torta raggruppati (le micro-spese inferiori al 5% vengono accorpate sotto la voce "Altro" per una migliore pulizia visiva).
- **Persistenza dei Dati:** Salvataggio strutturato automatico in un database in formato JSON.

---

## 📂 Struttura del Progetto

```text
budget_tracker_progetto_aggiornato/
│
├── data/
│   └── transactions.json          # Database JSON locale per il salvataggio dei dati
│
├── src/
│   ├── main.py                    # Punto di ingresso dell'applicazione
│   │
│   ├── database/
│   │   └── storage.py             # Funzioni di caricamento e salvataggio file JSON
│   │
│   ├── finance/
│   │   └── manager.py             # Logica finanziaria, filtri e calcolo totali
│   │
│   └── ui/
│       ├── menu.py                # Gestione dei menu (Questionary) e tabelle (Rich)
│       └── charts.py              # Generazione e salvataggio dei grafici (Matplotlib)
│
└── requirements.txt               # Dipendenze del progetto
```




[Personal Finance-2026-05-24-111004.pdf](https://github.com/user-attachments/files/28191168/Personal.Finance-2026-05-24-111004.pdf)


[JSON Input Management Flow-2026-05-24-111603.pdf](https://github.com/user-attachments/files/28191186/JSON.Input.Management.Flow-2026-05-24-111603.pdf)
