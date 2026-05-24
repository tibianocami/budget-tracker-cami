import os
import matplotlib
# Configura il backend non interattivo prima di importare pyplot
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def show_pie_chart(category_totals: dict, title: str):
    if not category_totals or sum(category_totals.values()) == 0:
        print("\n[Avviso] Nessuna spesa registrata per questo periodo. Impossibile generare il grafico.")
        return

    spesa_totale = sum(category_totals.values())

    # --- LOGICA DI RAGGRUPPAMENTO DELLE SPESE MINORI (< 5%) ---
    categorie_filtrate = {}
    totale_altro = 0.0

    for cat, val in category_totals.items():
        percentuale = (val / spesa_totale) * 100
        if percentuale < 5.0:
            # Se la spesa vale meno del 5%, accumuliamo l'importo
            totale_altro += val
        else:
            # Se supera il 5%, la categoria resta indipendente
            categorie_filtrate[cat] = val

    # Se abbiamo accumulato delle micro-spese, creiamo l'unico spicchio "Altro"
    if totale_altro > 0:
        categorie_filtrate["Altro"] = totale_altro

    # Liste definitive per il grafico
    labels = list(categorie_filtrate.keys())
    values = list(categorie_filtrate.values())

    # Palette colori
    colori_armoniosi = [
        '#4682B4', '#E9967A', '#8FBC8F', '#D2B48C', '#9370DB', '#A9A9A9',
        '#708090', '#5F9EA0', '#BC8F8F', '#B0C4DE', '#D8BFD8', '#E6E6FA',
        '#BDB76B', '#F4A460', '#CD853F', '#E0A96D', '#D4A5A5', '#95A78D',
        '#778899', '#8A9A86', '#AB92BF', '#AF8F6F', '#8FA4B4', '#A8B0A0',
        '#C2B280', '#A3B19B'
    ]

    fig, ax = plt.subplots(figsize=(9, 7), facecolor='#FAFAFA') 
    
    # Mostra la percentuale interna solo se lo spicchio è abbastanza grande
    def autopct_filter(pct):
        return f'{pct:.1f}%' if pct >= 2.0 else ''

    # Creazione della ciambella
    wedges, texts, autotexts = ax.pie(
        values, 
        autopct=autopct_filter, 
        startangle=140, 
        colors=colori_armoniosi[:len(labels)],
        pctdistance=0.75, 
        wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'width': 0.4, 'antialiased': True}
    )

    for autotext in autotexts:
        autotext.set_color('#1A202C')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)

    # Testo centrale con la somma totale di tutto il mese
    ax.text(
        0, 0, f"Totale Spese\n{spesa_totale:.2f} €", \
        ha='center', va='center', \
        fontsize=12, fontweight='bold', color='#2C3E50'
    )

    # Legenda ordinata a destra: mostrerà anche "Altro (70.00 €)"
    ax.legend(
        wedges, 
        [f"{l} ({v:.2f} €)" for l, v in zip(labels, values)],
        title="Categorie",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        fontsize=9,
        title_fontsize=10,
        frameon=True,
        facecolor='#FAFAFA',
        edgecolor='#E2E8F0'
    )

    ax.set_title(title, fontsize=13, fontweight='bold', color='#2C3E50', pad=20)
    plt.tight_layout()

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    output_dir = os.path.join(base_dir, "reports")
    os.makedirs(output_dir, exist_ok=True)
    
    filename = title.lower().replace(" ", "_").replace("/", "-").replace("_-", "").replace("-", "_") + ".png"
    filepath = os.path.join(output_dir, filename)

    plt.savefig(filepath, format='png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close(fig)

    print(f"\n[Successo] Grafico a ciambella generato e salvato correttamente!")
    print(f"[Percorso] {filepath}")