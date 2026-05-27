# 💰 Gestore Finanze Personali (Budget Tracker)

Un'applicazione Python da riga di comando (CLI) pulita, progettata per tracciare le entrate, monitorare le uscite divise per categoria e generare resoconti statistici dettagliati sia in formato tabellare che grafico.

## 🚀 Caratteristiche Principali

- **Gestione Mensile Avanzata:** Visualizza bilanci, aggiungi entrate/uscite ed elimina transazioni con calcoli automatici dei risparmi.
- **Interfaccia Utente Dinamica (CLI):** Menu di selezione interattivi gestibili con le frecce direzionali.
- **Visualizzazione ad Alto Impatto:** Tabelle colorate nel terminale per differenziare a colpo d'occhio entrate e uscite.
- **Grafici Statistici incorporati:** Generazione automatica di grafici a torta raggruppati (le micro-spese inferiori al 5% vengono accorpate sotto la voce "Altro" per una migliore pulizia visiva).
- **Persistenza dei Dati:** Salvataggio strutturato automatico in un database in formato JSON.


## 🛠️ Requisiti e Pacchetti Utilizzati
Il progetto fa uso di alcuni pacchetti esterni per ottimizzare l'esperienza utente e l'analisi dei dati. Ecco quali sono e perché sono stati scelti:

questionary:

Perché: Sostituisce i vecchi controlli ad input() numerici testuali, azzerando i crash dovuti a inserimenti di caratteri errati e rendendo la CLI moderna e navigabile con le frecce della tastiera.

rich:

Perché: Utilizzata per impaginare i dati finanziari in tabelle colorate ed eleganti nel terminale, applicando stili condizionali (verde per le entrate, rosso per le uscite).

matplotlib:

Perché: Genera grafici a torta relativi alle spese. È configurato con il backend non interattivo Agg per salvare i file PNG in locale in modo asincrono, senza interrompere il flusso della riga di comando e senza richiedere finestre GUI pop-up.

python-dateutil:

Perché: Gestisce in automatico le operazioni sulle date (come l'incremento o decremento continuo dei mesi), risolvendo i passaggi critici come il cambio dell'anno tra dicembre e gennaio.
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


## 📅 Development Roadmap (Gantt)

[JSON Input Management Flow-2026-05-24-113049.pdf](https://github.com/user-attachments/files/28191430/JSON.Input.Management.Flow-2026-05-24-113049.pdf)

## 🔄 Application Logic & Flow (Flowchart)

[JSON Input Management Flow-2026-05-24-111603.pdf](https://github.com/user-attachments/files/28191186/JSON.Input.Management.Flow-2026-05-24-111603.pdf)
