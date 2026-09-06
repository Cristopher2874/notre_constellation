# CV LaTeX Modulaire — Cristopher Hernandez
## Double Diplôme Écoles Centrales / Bourse Eiffel

---

## Arborescence du projet

```
cv_report/
├── main.tex                   # Assembleur uniquement (24 lignes, aucun contenu de section)
├── config/
│   ├── packages.tex           # Tous les \usepackage
│   ├── geometry.tex           # Marges et espacement (knob overflow : paramètre scale)
│   ├── colors.tex             # Style moderncv + couleur (burgundy/classic)
│   └── personal-info.tex      # Nom, contact, photo — SEUL fichier avec données perso
├── sections/
│   ├── accroche.tex           # Phrase d'accroche (profil 2-3 lignes)
│   ├── formation.tex          # Formation antéchronologique (UASLP, PrepaTec, Collège)
│   ├── projets.tex            # 3 projets sélectionnés (FLOW, ICPC, Hackathons 2024)
│   ├── experiences.tex        # 3 expériences (Oracle, LEAD 3D, Nexon/FRC)
│   ├── competences.tex        # Compétences techniques + langues CEFR
│   └── interets.tex           # Centres d'intérêt avec quantificateurs
└── assets/
    ├── README_PHOTO.txt        # Instructions pour la photo
    └── photo.jpg               # TODO: Uploader votre photo ici sur Overleaf
```

---

## Instructions pour Overleaf

### 1. Créer un nouveau projet
- Overleaf > New Project > Blank Project
- Nommer le projet : `Hernandez-Cristopher-CV-Eiffel-Centrales-2026`

### 2. Uploader tous les fichiers
Recréer exactement la même arborescence sur Overleaf :
- Créer les dossiers `config/`, `sections/`, `assets/`
- Uploader chaque fichier `.tex` dans le bon dossier
- Uploader votre photo dans `assets/` sous le nom `photo.jpg`

### 3. Définir le compilateur
- Menu (en haut à gauche) > Compiler : **pdfLaTeX**

### 4. Compiler et vérifier
- Cliquer "Recompile"
- Vérifier que le document tient sur **exactement 1 page**
- Si débordement : ouvrir `config/geometry.tex` et réduire `scale` (0.85 → 0.83 → 0.80)

---

## Données à compléter avant soumission

| Champ | Fichier | Statut |
|---|---|---|
| Numéro de téléphone | `config/personal-info.tex` | `[PLACEHOLDER]` à remplacer |
| Photo professionnelle | `assets/photo.jpg` | Fichier à uploader |
| Nom du collège | `sections/formation.tex` | `[PLACEHOLDER]` à remplacer |
| Attestation UASLP 1er place | `sections/formation.tex` | Note "[attestation à fournir]" |
| Attestation 2e meilleure moyenne | `sections/formation.tex` | Note "[attestation à fournir]" |
| Attestation concours C++ | `sections/formation.tex` | Note "[attestation à fournir]" |
| Certificats échecs | `sections/interets.tex` | Note "[confirmer tournois]" |

---

## Règle de maintenance

| Modification | Fichier à éditer UNIQUEMENT |
|---|---|
| Changer la couleur ou le style | `config/colors.tex` |
| Ajuster les marges (overflow) | `config/geometry.tex` |
| Mettre à jour le téléphone | `config/personal-info.tex` |
| Changer la photo | `assets/` + chemin dans `config/personal-info.tex` |
| Ajouter un diplôme | `sections/formation.tex` |
| Ajouter un projet | `sections/projets.tex` (vérifier contrainte 1 page) |
| Modifier l'accroche | `sections/accroche.tex` |
| Passer en anglais | `config/packages.tex` (french → english) + traduire sections/ |

---

## Nom du fichier PDF final
```
Hernandez-Cristopher-CV-Eiffel-Centrales-2026.pdf
```
