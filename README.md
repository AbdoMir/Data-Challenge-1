# Data Challenge 1 — Buprenorphine/Naloxone vs. Clonidine for Opioid Detoxification

Analyse comparative de deux traitements de désintoxication aux opioïdes à partir de deux essais cliniques NIDA (National Institute on Drug Abuse) : **CTN-0001** (patients hospitalisés) et **CTN-0002** (patients ambulatoires).

**Groupe 5** — M1 S1

---

## Contexte clinique

Ce projet analyse les données de deux essais cliniques randomisés comparant :

- **BUPNAL** — Buprénorphine/Naloxone
- **CLON** — Clonidine

pour la détoxification rapide aux opioïdes sur une période de 13 jours, suivie d'une phase de suivi.

> Référence principale : Ling et al., 2005 (*Primary Publication*)

---

## Structure du projet

```
Data Challenge 1/
├── data/raw/               # Données nettoyées (format SDTM, 2 études)
│   ├── dm1/2.csv           # Démographie & bras de randomisation
│   ├── ds1/2.csv           # Disposition (phases, abandon)
│   ├── ex1/2.csv           # Exposition / dosages
│   ├── lb1/2.csv           # Résultats labo (dépistages urinaires)
│   ├── mh1/2.csv           # Antécédents médicaux
│   ├── sc1/2.csv           # Sociodémographie
│   └── vs1/2.csv           # Signes vitaux
│
├── notebooks/
│   ├── flowchart.ipynb     # Diagramme CONSORT de flux patients
│   ├── Figure 1.ipynb      # Courbe de rétention au fil du temps
│   └── Tableau 2.ipynb     # Analyse d'efficacité & tests statistiques
│
├── src/
│   └── flowchart.py        # Script Graphviz pour le diagramme CONSORT
│
├── Projet/                 # Livrables
│   ├── figure1_retention.html
│   ├── Table1_Ambulatoire.html
│   ├── Table1_Hospitalisation.html
│   ├── Mini-Rapport_Table1-Partielle.docx
│   └── Presentation Data challenge 1 -Groupe5.pptx
│
└── docs/                   # Documentation, protocole, articles
```

---

## Population étudiée

| Étude | Cadre | Patients screenés | BUPNAL | CLON | Échec screening |
|-------|-------|:-----------------:|:------:|:----:|:---------------:|
| CTN-0001 | Hospitalisé (IN) | 138 | 77 | 36 | 25 |
| CTN-0002 | Ambulatoire (OUT) | 273 | 156 | 74 | 43 |
| **Total** | | **411** | **233** | **110** | **68** |

**Randomisés :** 343 patients (ratio BUPNAL:CLON ≈ 2:1)

---

## Analyses réalisées

### Flowchart CONSORT (`flowchart.ipynb`)
Diagramme de flux des patients à travers les phases de l'essai :
- Screening → Randomisation → Phase active → Suivi
- Calcul des abandons précoces (< 14 jours) : 33 au total (14 BUPNAL, 19 CLON)
- Population Per-Protocol (PP) : 310 patients ayant complété la phase active de 13 jours

### Figure 1 — Rétention (`Figure 1.ipynb`)
Courbe de proportion de patients retenus à chaque visite, stratifiée par :
- Bras de traitement (BUPNAL vs CLON)
- Cadre (hospitalisé vs ambulatoire)

Visualisation interactive générée avec **Plotly** → [`figure1_retention.html`](Projet/Flowchart-Table1-2%20%26Figure/figure1_retention.html)

### Tableau 2 — Efficacité (`Tableau 2.ipynb`)
Analyse du critère de jugement principal composite :

> Un patient est **répondeur** si :
> 1. Il a au moins une observation à VISITNUM ≥ 13 *(rétention)*
> 2. Tous ses tests urinaires aux opioïdes à VISITNUM ≥ 13 sont **négatifs** *(abstinence)*

Tests statistiques :
- Test de proportion (unilatéral) : H₀ : p_BUPNAL = p_CLON vs H₁ : p_BUPNAL > p_CLON
- Intervalles de confiance à 95 %
- Analyses ITT et Per-Protocol

---

## Stack technique

| Outil | Usage |
|-------|-------|
| `polars` | Traitement principal des données |
| `pandas` | Manipulation complémentaire |
| `scipy.stats` | Tests statistiques |
| `plotly` | Visualisations interactives |
| `matplotlib` | Figures statiques |
| `graphviz` | Diagramme CONSORT |

### Installation

```bash
# Créer et activer l'environnement virtuel
python -m venv challenge1-env
challenge1-env\Scripts\activate   # Windows

# Installer les dépendances
pip install polars pandas scipy plotly matplotlib graphviz
```

### Lancer les notebooks

```bash
jupyter notebook notebooks/
```

---

## Données sources

Les données brutes proviennent des archives publiques NIDA Clinical Trials Network :
- `ascii-data-files-nida-ctn-0001-20251024/` — CTN-0001
- `ascii-data-files-nida-ctn-0002-20251027/` — CTN-0002

Format : **SDTM (Study Data Tabulation Model)** avec fichier `define.xml` de métadonnées.

---

## Résultats clés

- BUPNAL présente une rétention numériquement supérieure à CLON sur l'ensemble des visites
- Les patients hospitalisés (IN) ont une meilleure rétention que les patients ambulatoires (OUT)
- L'analyse Per-Protocol confirme la tendance observée en ITT
- Le déséquilibre de randomisation 2:1 limite la puissance statistique pour certaines comparaisons

---

## Références

- Ling, W. et al. (2005). Buprenorphine maintenance treatment of opiate dependence. *Drug and Alcohol Dependence*.
- NIDA Clinical Trials Network — [CTN-0001](https://datashare.nida.nih.gov/study/nida-ctn-0001) / [CTN-0002](https://datashare.nida.nih.gov/study/nida-ctn-0002)
- ICH E9 — Statistical Principles for Clinical Trials
