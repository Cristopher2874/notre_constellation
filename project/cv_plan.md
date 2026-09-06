# PLAN FINAL — CV LaTeX Modulaire pour Écoles Centrales / Bourse Eiffel

> **Version intégrée** | Objectif : produire un CV 1 page en français, compilable sur Overleaf, structuré en fichiers modulaires, avec placeholders systématiques pour éviter tout blocage.

---

## TABLE DES MATIÈRES

1. [Fondation Stratégique](#phase-1--fondation-stratégique)
2. [Inventaire & Audit de Contenu](#phase-2--inventaire--audit-de-contenu)
3. [Moteurs Rédactionnels (Formules)](#phase-3--moteurs-rédactionnels)
4. [Architecture Modulaire Overleaf](#phase-4--architecture-modulaire-overleaf)
5. [Plan de Production par Section](#phase-5--plan-de-production-par-section)
6. [Workflow d'Exécution](#phase-6--workflow-dexécution)
7. [Checklist Qualité Finale](#phase-7--checklist-qualité-finale)
8. [Règles de Maintenance](#phase-8--règles-de-maintenance)

---

## PHASE 1 | FONDATION STRATÉGIQUE

### 1.1 Narrative Centrale
Avant d'écrire une ligne, le CV doit répondre implicitement à trois questions :

| Question | Ce que le CV doit démontrer |
|---|---|
| **Pourquoi la France ?** | La phrase d'accroche fait le pont entre ton parcours et l'éducation d'ingénieur française |
| **Pourquoi ce domaine ?** | Curiosité scientifique + profondeur technique |
| **Pourquoi toi ?** | Excellence prouvée via classement, projets et impact quantifié |

### 1.2 Contraintes & Critères de Succès

| Contrainte | Cible |
|---|---|
| **Longueur** | Exactement 1 page (standard école d'ingénieur française) |
| **Langue** | Français (sauf exigence explicite du programme en anglais) |
| **Format** | PDF, colonne unique, lisible par ATS |
| **Ton** | Rigueur, curiosité scientifique, potentiel — **pas** ton corporate développeur logiciel |
| **Photo** | Portrait professionnel, fond neutre (standard France) |

### 1.3 Choix du Template : `moderncv` (Style `classic`)

**Recommandé :** `moderncv` avec style `classic`, couleur `burgundy`.

**Pourquoi ce choix :**
- Compatibilité académique européenne native
- Support photo intégré (critique pour la France)
- Flux colonne unique = contrôle précis de la page unique
- 5 styles + palettes de couleurs, stable sur Overleaf

**Alternative :** `Awesome-CV` uniquement si profil très software et volonté de signaler "ingénieur qui code".

**À éviter :** `AltaCV` (sidebar gaspille l'espace), `Friggeri` (trop design), `Jake's Resume` (pas de photo, trop américain).

### 1.4 Spécifications Visuelles

```latex
\documentclass[11pt,a4paper,sans]{moderncv}
\moderncvstyle{classic}
\moderncvcolor{burgundy}
```

| Élément | Spécification | Justification |
|---|---|---|
| Couleur principale | `burgundy` ou `blue` | Sérieux, académique |
| Taille police | 11pt | Dense mais lisible |
| Photo | 64×64mm, professionnelle, fond neutre | Standard France |
| Marges | `geometry` scale ~0.85 | Tight mais aéré |
| Inter-titres | Gras, coloré, petites capitales | Scannabilité humaine |

---

## PHASE 2 | INVENTAIRE & AUDIT DE CONTENU

### 2.1 Matériel à Rassembler

**Depuis l'ancien CV software :**
- Intitulés de poste, entreprises, dates
- Descriptions de projets (garder les détails techniques)
- Liste de compétences (langages, frameworks, outils)

**Nouveau matériel obligatoire :**
- **Classement exact** (ex: "3ème sur 120")
- **Détails Bac/Prépa/BUT/Licence** avec mentions (Très Bien, Bien)
- **Prix, bourses, distinctions au mérite**
- **Expérience recherche/labo** (très valorisée en France)
- **Certifications linguistiques** avec niveaux CEFR (TOEIC, DELF, etc.)
- **URL LinkedIn** personnalisée
- **GitHub / Portfolio** (si projets démontrables)

### 2.2 Matrice de Traduction : Software → École d'Ingénieur

| Langage CV Software | Langage CV École d'Ingénieur |
|---|---|
| "Built REST API with Node.js" | "Conçu et déployé une API RESTful (Node.js), réduisant les temps de réponse de 40%" |
| "Worked on CI/CD pipeline" | "Automatisé le pipeline CI/CD (Jenkins/GitHub Actions), réduisant le déploiement de 28 min à 9 min" |
| "Led a team of 5 developers" | "Dirigé une équipe de 5 étudiants sur un projet robotique, livré avec 2 semaines d'avance, noté 18/20" |

**Décalage clé :** De *quelle techno j'ai utilisée* → *quel problème scientifique/technique j'ai résolu et comment je l'ai mesuré*.

---

## PHASE 3 | MOTEURS RÉDACTIONNELS

Quatre formules complémentaires. Chaque bullet doit en utiliser une — jamais de description narrative pure.

### 3.1 XYZ (Arme Principale)
**Formule :** `Accomplished [X] as measured by [Y] by doing [Z]`

- **X :** Résultat (ce qui a changé)
- **Y :** Métrique (nombre, %, échelle)
- **Z :** Méthode technique (outils, approche)

**Exemple avec placeholders :**
> Conçu [X: type de système], réduisant le temps de traitement de [Y: PLACEHOLDER pourcentage ou valeur], en implémentant [Z: PLACEHOLDER outils/méthodes].

### 3.2 STAR (Pour le Projet Phare)
**Formule :** Situation → Task → Action → Result

**Exemple :**
> Dans le cadre de [S: PLACEHOLDER concours/cours], chargé de [T: PLACEHOLDER objectif], j'ai [A: PLACEHOLDER action technique], permettant [R: PLACEHOLDER résultat chiffré].

### 3.3 PAR (Pour Expériences Professionnelles)
**Formule :** Problem → Action → Result

**Exemple :**
> Face à [P: PLACEHOLDER problème], j'ai [A: PLACEHOLDER action technique], ce qui a [R: PLACEHOLDER résultat chiffré].

### 3.4 C-A-R (Pour Recherche / Académique)
**Formule :** Context → Action → Result

**Exemple :**
> Au sein de [C: PLACEHOLDER labo/équipe], j'ai [A: PLACEHOLDER action technique], validé sur [R: PLACEHOLDER échantillon/métrique].

### 3.5 Arsenal de Verbes d'Action (Français, Passé Composé)

| Catégorie | Verbes |
|---|---|
| **Technique / Construction** | Conçu, Développé, Implémenté, Architecturé, Programmé, Modélisé, Simulé |
| **Optimisation** | Optimisé, Accéléré, Réduit, Amélioré, Parallélisé |
| **Recherche / Analyse** | Analysé, Évalué, Validé, Caractérisé, Quantifié, Comparé |
| **Leadership** | Dirigé, Coordonné, Encadré, Organisé, Piloté, Animé |
| **Création** | Créé, Élaboré, Rédigé, Prototypé |

**Règle :** Jamais le même verbe en tête de bullet dans une même section.

---

## PHASE 4 | ARCHITECTURE MODULAIRE OVERLEAF

### 4.1 Arborescence Obligatoire

```
project-root/
├── main.tex                 # Assembleur uniquement (≤ 25 lignes)
├── config/
│   ├── packages.tex         # Tous les \usepackage
│   ├── geometry.tex         # Layout, marges, espacement listes
│   ├── colors.tex           # Style moderncv + couleurs custom
│   └── personal-info.tex    # Nom, contact, titre, chemin photo
├── sections/
│   ├── accroche.tex         # Phrase d'accroche (2-3 lignes)
│   ├── formation.tex        # Formation (antéchronologique)
│   ├── projets.tex          # Projets scientifiques et techniques
│   ├── experiences.tex      # Stages, jobs, associatif
│   ├── competences.tex      # Compétences techniques + Langues
│   └── interets.tex         # Centres d'intérêt
└── assets/
    └── photo.jpg            # Photo professionnelle
```

### 4.2 Règles d'Architecture

| Règle | Description |
|---|---|
| **Un fichier = une responsabilité** | Aucun fichier ne mélange deux sections. Aucun fichier ne mélange config et contenu. |
| **main.tex est un assembleur** | Il ne contient que des `\input`. Jamais de texte de section. |
| **Config avant contenu** | Les fichiers `config/` établissent le contrat. Les fichiers `sections/` le consomment. |
| **Données personnelles centralisées** | `config/personal-info.tex` est le SEUL fichier contenant nom, téléphone, email, photo. |
| **Placeholders file-locaux** | Un placeholder dans `sections/formation.tex` décrit ce qui va DANS cette section, pas un vague "remplir ici". |

### 4.3 Contenu de Chaque Fichier

#### `main.tex` — L'Assembleur
```latex
% main.tex
% CV École d'Ingénieur — Bourse Eiffel
% Structure modulaire pour Overleaf

\documentclass[11pt,a4paper,sans]{moderncv}

\input{config/packages}
\input{config/geometry}
\input{config/colors}
\input{config/personal-info}

\begin{document}
\makecvtitle

\input{sections/accroche}
\input{sections/formation}
\input{sections/projets}
\input{sections/experiences}
\input{sections/competences}
\input{sections/interets}

\end{document}
```

#### `config/packages.tex`
```latex
% config/packages.tex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{enumitem}
\usepackage{microtype}
\usepackage[french]{babel}
```

#### `config/geometry.tex`
```latex
% config/geometry.tex
\usepackage[scale=0.85]{geometry}
\setlist{nosep, leftmargin=*}
% TODO: Si dépassement 1 page, réduire scale à 0.83 ou 0.80 (min 0.78)
```

#### `config/colors.tex`
```latex
% config/colors.tex
\moderncvstyle{classic}
\moderncvcolor{burgundy}
% TODO: Changer ici uniquement pour modifier style ou couleur
```

#### `config/personal-info.tex` — Registre de Données
```latex
% config/personal-info.tex
\name{[PLACEHOLDER: Prénom]}{[PLACEHOLDER: Nom]}
\title{[PLACEHOLDER: Candidature en Xe année — Spécialité [PLACEHOLDER]]}
\address{[PLACEHOLDER: Ville], [PLACEHOLDER: Pays]}{}
\phone[mobile]{[PLACEHOLDER: +XX X XX XX XX XX]}
\email{[PLACEHOLDER: prenom.nom@email.com]}
\social[linkedin]{[PLACEHOLDER: url-linkedin-personnalisée]}
\social[github]{[PLACEHOLDER: nom-github]}
\photo[64pt][0.4pt]{assets/photo.jpg}
% TODO: Remplacer assets/photo.jpg par le nom réel du fichier photo
```

---

## PHASE 5 | PLAN DE PRODUCTION PAR SECTION

### RÈGLE FONDAMENTALE
**Ne jamais s'arrêter pour une information manquante.** Si une donnée (date, métrique, rang, note, entreprise, outil, pourcentage de résultat, etc.) n'est pas fournie, insérer un placeholder au format exact : `[PLACEHOLDER: description précise de ce qui va ici]`. Continuer la construction. Ne jamais laisser une section vide.

---

### SECTION 1 : En-tête (Header)
**Déjà intégré dans** `config/personal-info.tex`.

**Règles :**
- Email professionnel (`prenom.nom@...`, pas de pseudos)
- URL LinkedIn personnalisée et propre
- Photo : fond neutre, tenue professionnelle, regard caméra, léger sourire

---

### SECTION 2 : Phrase d'Accroche (`sections/accroche.tex`)
**Longueur :** 2-3 lignes maximum.

**Formule :** `[Parcours : CPGE/BUT/Licence + spécialité] + [Métrique clé : rang/mention] + [Motivation école cible + domaine]`

```latex
% sections/accroche.tex
\cvitem{Profil}{
  Élève en [PLACEHOLDER: filière], classé [PLACEHOLDER: rang/mention],
  passionné par [PLACEHOLDER: domaine technique].
  Je vise l'intégration de [PLACEHOLDER: type d'école] pour
  [PLACEHOLDER: objectif de formation lié au programme].
}
```

**Règles :**
- Mentionner le **parcours académique** (CPGE, BUT, Licence, etc.)
- Mentionner **classement ou mention** si fort
- Énoncer explicitement la **spécialisation cible**
- Faire le pont vers **pourquoi la France / ce type d'école**

---

### SECTION 3 : Formation (`sections/formation.tex`) — SECTION LA PLUS IMPORTANTE
**Ordre :** Antéchronologique.

```latex
% sections/formation.tex
\section{Formation}

\cventry{[PLACEHOLDER: Année début--fin]}{[PLACEHOLDER: Diplôme/Programme]}{[PLACEHOLDER: Établissement]}{[PLACEHOLDER: Ville]}{[PLACEHOLDER: Rang/Mention/Classement]}{
  \begin{itemize}
    \item [PLACEHOLDER: Option/spécialité]
    \item [Bullet XYZ: classé [X: rang], moyenne [Y: note/20], en [Z: spécialité]]
    \item [Bullet XYZ: Lauréat de [X: prix], décerné au [Y: top X%], pour [Z: projet/sujet]]
  \end{itemize}
}

\cventry{[PLACEHOLDER: Année bac]}{Baccalauréat Général}{[PLACEHOLDER: Lycée]}{[PLACEHOLDER: Ville]}{[PLACEHOLDER: Mention]}{
  \begin{itemize}
    \item [PLACEHOLDER: Spécialités: ex: Maths, Physique, NSI]
  \end{itemize}
}
% TODO: Ajouter d'autres diplômes si pertinent
```

**Règles :**
- **Toujours inclure le classement** si disponible. Les écoles d'ingénieur françaises sont méritocratiques et obsédées par le classement.
- Inclure les détails du **Baccalauréat** (mention, section, option)
- Si en CPGE, mentionner les **résultats de concours** (ex: "Admissible Centrale-Supélec, Mines-Ponts")
- Minimum 2 entrées (la plus récente + Bac). Ajouter les autres si pertinentes.

---

### SECTION 4 : Projets Scientifiques et Techniques (`sections/projets.tex`)
**Objectif :** Démontrer curiosité scientifique, profondeur technique, capacité d'exécution.

```latex
% sections/projets.tex
\section{Projets Scientifiques et Techniques}

\cvitem{[PLACEHOLDER: Titre Projet 1 — Domaine/Technologie]}{
  \textbf{Contexte:} [PLACEHOLDER: 1 ligne décrivant le cadre: cours, concours, labo]. \newline
  \textbf{Résultat:} [Bullet XYZ: [X: outcome], [Y: PLACEHOLDER métrique/%], en [Z: PLACEHOLDER outils/langages]].
}

\cvitem{[PLACEHOLDER: Titre Projet 2 — Domaine/Technologie]}{
  \textbf{Contexte:} [PLACEHOLDER: 1 ligne décrivant le cadre]. \newline
  \textbf{Résultat:} [Bullet XYZ: [X: outcome], [Y: PLACEHOLDER métrique], en [Z: PLACEHOLDER outils]].
}
% TODO: 2-3 projets max. Si l'utilisateur en a plus de 3, garder les 3 meilleurs
```

**Règles :**
- 2-3 projets maximum (l'espace est limité sur 1 page)
- Prioriser les projets montrant : **pensée algorithmique, conception système, ou méthodologie scientifique**
- Toujours inclure : **problème, outils utilisés, résultat quantifié**
- Si compétition, mentionner **classement / résultat**

---

### SECTION 5 : Expériences Professionnelles (`sections/experiences.tex`)
**Inclut :** Stages, jobs d'été, engagements associatifs.

```latex
% sections/experiences.tex
\section{Expériences Professionnelles}

\cventry{[PLACEHOLDER: Dates MM/YYYY]}{[PLACEHOLDER: Intitulé du poste]}{[PLACEHOLDER: Entreprise/Asso]}{[PLACEHOLDER: Ville]}{}{
  \begin{itemize}
    \item [Bullet PAR: Face à [P: PLACEHOLDER], j'ai [A: PLACEHOLDER], résultat [R: PLACEHOLDER chiffre]]
    \item [Bullet XYZ: [X: action], [Y: PLACEHOLDER gain/temps/%], par [Z: PLACEHOLDER méthode/outil]]
  \end{itemize}
}
% TODO: Ajouter d'autres expériences si pertinent (max 2-3 au total)
```

**Règles :**
- Verbes d'action au passé (passé composé)
- Quantifier la **portée** (taille équipe, budget, utilisateurs) quand les métriques d'impact ne sont pas disponibles
- Si pas de chiffres : "Utilisé par 50+ collaborateurs" ou "Déployé sur 3 sites"
- Maximum 2-3 expériences, 2-3 bullets chacune

---

### SECTION 6 : Compétences et Langues (`sections/competences.tex`)

```latex
% sections/competences.tex
\section{Compétences et Langues}

\cvitem{Programmation}{
  [PLACEHOLDER: Langages avec niveau — ex: Python (avancé), C++ (intermédiaire)]
}

\cvitem{Frameworks \& Outils}{
  [PLACEHOLDER: Liste — ex: PyTorch, Git, Docker, Linux, LaTeX]
}

\cvitem{Langues}{
  Français — [PLACEHOLDER: CEFR] ([PLACEHOLDER: certification]) \newline
  Anglais — [PLACEHOLDER: CEFR] ([PLACEHOLDER: score TOEIC/TOEFL]) \newline
  [PLACEHOLDER: Autre langue] — [PLACEHOLDER: niveau]
}
```

**Règles :**
- **Toujours utiliser l'échelle CEFR** (A1-C2) — standard européen
- Inclure les **scores TOEIC/TOEFL/IELTS** si disponibles
- Le niveau de français compte : si pas fluent, montrer la **progression** ("B1, en cours de perfectionnement")
- Être honnête — les évaluateurs Eiffel peuvent interviewer en français

---

### SECTION 7 : Centres d'Intérêt (`sections/interets.tex`)
**Objectif :** Montrer l'équilibre, l'esprit d'équipe, la capacité à tenir sur la durée.

```latex
% sections/interets.tex
\section{Centres d'Intérêt}

\cvitem{[PLACEHOLDER: Catégorie, ex: Sport]}{[PLACEHOLDER: Activité] — [PLACEHOLDER: niveau/achievement chiffré, ex: 5 ans, 3 compétitions]}
\cvitem{[PLACEHOLDER: Catégorie, ex: Musique]}{[PLACEHOLDER: Instrument/Activité] — [PLACEHOLDER: durée/niveau]}
\cvitem{[PLACEHOLDER: Catégorie, ex: Associatif]}{[PLACEHOLDER: Rôle] — [PLACEHOLDER: responsabilité chiffrée, ex: budget X€, Y événements]}
```

**Règles :**
- Toujours ajouter un **petit quantificateur ou accomplissement** (années, niveau, rôle)
- Montrer la **dédication dans le temps** (les écoles françaises valorisent la persévérance)
- Inclure **sports collectifs ou activités de groupe** pour signaler l'esprit d'équipe
- Éviter les hobbies passifs sans contexte ("Lecture, cinéma")

---

## PHASE 6 | WORKFLOW D'EXÉCUTION

### Étape 1 : Brouillon Brut (60 min)
Pour chaque section, écrire **tout** sans se soucier de la longueur. Utiliser la formule XYZ pour chaque bullet. Ne pas éditer.

### Étape 2 : La "Guillotine 1 Page" (30 min)
Le brouillon fera 1,5-2 pages. Couper sans pitié :
- **Supprimer tout bullet sans nombre ou métrique**
- **Supprimer tout projet ne montrant pas de profondeur scientifique/technique**
- **Supprimer toute expérience de plus de 3 ans** (sauf exceptionnelle)
- **Compresser les descriptions de langues** à une ligne
- **Supprimer les bullets "soft"** ("Travail en équipe", "Bonne communication") — montrer par les actions

### Étape 3 : Intégration LaTeX Modulaire (45 min)
- Créer l'arborescence de fichiers sur Overleaf
- Copier le contenu poli dans les fichiers de section
- Compiler fréquemment pour vérifier l'espacement
- Ajuster `scale` dans `config/geometry.tex` si besoin (plage 0.82–0.88)
- Vérifier que la photo ne pousse pas le texte vers le bas de manière incongrue

### Étape 4 : Polissage Typographique (20 min)
- Vérifier les **veuves/orphelines** (mots seuls en fin de bullet)
- Assurer la **cohérence des formats de date** (tous "MM/YYYY" ou tous "Mois YYYY")
- Vérifier l'**alignement** de toutes les dates alignées à droite
- Vérifier qu'**aucun bullet ne dépasse 2 lignes**

### Étape 5 : Relecture Linguistique Française (20 min)
- Passer dans un correcteur (BonPatron, Reverso)
- Vérifier les **accents** (é, è, ê, à, ô)
- Vérifier l'**accord en genre** dans toutes les descriptions
- Vérifier la **cohérence des temps verbaux** (passé composé recommandé)

### Étape 6 : QA Finale (10 min)

| Check | Statut |
|---|---|
| Exactement 1 page | ☐ |
| Photo professionnelle, taille correcte | ☐ |
| Tous les bullets utilisent XYZ, STAR, PAR ou C-A-R | ☐ |
| Aucun bullet sans métrique ou quantificateur | ☐ |
| Classement/mention visiblement affiché dans Formation | ☐ |
| Niveaux CEFR utilisés pour toutes les langues | ☐ |
| URL LinkedIn personnalisée et professionnelle | ☐ |
| Email professionnel | ☐ |
| Aucune faute d'orthographe/grammaire | ☐ |
| Texte du PDF sélectionnable (test: copier-coller depuis le PDF) | ☐ |
| Nom du fichier : `Nom-Prenom-CV-Eiffel-Centrale-2026.pdf` | ☐ |

---

## PHASE 7 | CHECKLIST QUALITÉ FINALE (Pour l'Agent Builder)

Avant de retourner les fichiers `.tex`, vérifier :

1. [ ] Chaque section existe et est dans le bon ordre : Header → Accroche → Formation → Projets → Expériences → Compétences/Langues → Intérêts.
2. [ ] Aucune section n'est vide ; chaque champ contient soit des données réelles, soit un `[PLACEHOLDER: ...]`.
3. [ ] Chaque bullet utilise une des quatre formules (XYZ, STAR, PAR, C-A-R).
4. [ ] Aucun verbe d'action n'est répété en tête de bullet dans une même section.
5. [ ] Tous les niveaux de langue utilisent le format CEFR (`A1–C2`) ou un placeholder le demandant.
6. [ ] Le document est conçu pour compiler sur exactement 1 page.
7. [ ] Un placeholder de photo professionnelle est inclus.
8. [ ] Tous les placeholders sont enveloppés dans `[PLACEHOLDER: description]` pour faciliter le recherche-remplacement.
9. [ ] `main.tex` ne dépasse pas 25 lignes et ne contient aucun texte de section.
10. [ ] Aucun contenu n'est dupliqué entre fichiers (pas de redéfinition de couleur, pas de données perso dans les sections).
11. [ ] Des commentaires `% TODO:` sont présents pour guider l'utilisateur sur les ajustements (overflow, photo, sections facultatives).
12. [ ] La structure modulaire est respectée : `config/` pour la configuration, `sections/` pour le contenu, `assets/` pour les médias.

**Si des données réelles ont été fournies par l'utilisateur, les intégrer verbatim dans la section correcte et supprimer UNIQUEMENT ce placeholder spécifique. Laisser tous les autres placeholders intacts.**

---

## PHASE 8 | RÈGLES DE MAINTENANCE

Pour toute modification future du CV, ces règles garantissent la survie de la structure modulaire :

| Modification | Fichier à éditer UNIQUEMENT |
|---|---|
| Ajouter un nouveau diplôme | `sections/formation.tex` |
| Changer la photo | Remplacer le fichier dans `assets/` OU éditer le chemin dans `config/personal-info.tex` |
| Changer le schéma de couleurs | `config/colors.tex` |
| Ajouter un 4ème projet | `sections/projets.tex`, puis vérifier contrainte 1 page dans `config/geometry.tex` |
| Mettre à jour le numéro de téléphone | `config/personal-info.tex` |
| Passer en anglais | `config/packages.tex` (changer `french` → `english`) + traduire chaque fichier de section individuellement |
| Ajuster les marges (overflow) | `config/geometry.tex` |
| Modifier la phrase d'accroche | `sections/accroche.tex` |

---

## BLOC D'INSTRUCTION COMPLET POUR AGENT (One-Liner)

> **"Construire un CV LaTeX français d'1 page pour Écoles Centrales / Bourse Eiffel avec `moderncv` style `classic`, couleur `burgundy`. Utiliser une structure modulaire Overleaf : `main.tex` assemble `config/packages`, `config/geometry`, `config/colors`, `config/personal-info`, puis `sections/accroche`, `sections/formation`, `sections/projets`, `sections/experiences`, `sections/competences`, `sections/interets`. Chaque bullet doit utiliser XYZ, STAR, PAR ou C-A-R avec métriques quantifiées. Si une donnée manque, insérer `[PLACEHOLDER: description]` et continuer. Ne jamais laisser une section vide. Ne jamais créer de fichier monolithique. Fournir tous les fichiers séparément avec commentaires `% TODO:` de guidance."**

---
