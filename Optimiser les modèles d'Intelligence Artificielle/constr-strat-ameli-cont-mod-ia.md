Ce cours est la suite logique du chapitre sur le **monitoring**. Le précédent expliquait **comment détecter qu'un modèle IA se dégrade**. Celui-ci explique **comment améliorer continuellement le modèle** pour qu'il reste performant pendant toute sa durée de vie. 

---

# Résumé détaillé – Construire une stratégie d'amélioration continue des modèles IA

# I. Pourquoi mettre en place une amélioration continue ?

## L'idée principale

Un modèle d'intelligence artificielle n'est jamais parfait.

Même s'il fonctionne très bien aujourd'hui, plusieurs phénomènes peuvent diminuer ses performances :

* les données évoluent ;
* les besoins métier changent ;
* les utilisateurs ont de nouvelles attentes ;
* de nouvelles technologies apparaissent.

C'est pourquoi il faut améliorer le modèle en permanence.

L'amélioration continue consiste donc à **observer le fonctionnement du modèle, détecter ses faiblesses puis apporter régulièrement des améliorations**, sans attendre qu'il devienne complètement obsolète. 

---

## Exemple

Une entreprise possède un chatbot.

Au départ :

* il répond correctement à 92 % des questions.

Quelques mois plus tard :

* les produits vendus changent ;
* les questions des clients évoluent.

Le chatbot répond maintenant correctement à seulement 80 % des demandes.

Deux possibilités existent :

❌ attendre plusieurs années puis refaire entièrement le modèle.

ou

✅ améliorer régulièrement le modèle.

Le cours recommande évidemment la deuxième solution.

---

# II. Le principe du Kaizen

C'est une notion extrêmement importante.

## Définition

Le **Kaizen** est une méthode japonaise d'amélioration continue.

Son principe est très simple :

> Faire de petites améliorations régulièrement est plus efficace que réaliser une énorme amélioration très rarement. 

---

## Pourquoi ?

Imagine une voiture.

Deux façons de l'entretenir :

### Mauvaise méthode

Tu n'effectues aucune révision pendant 5 ans.

À la fin :

* moteur usé ;
* pneus abîmés ;
* freins fatigués.

Les réparations coûteront très cher.

---

### Méthode Kaizen

Chaque mois :

* tu vérifies les pneus ;
* tu fais la vidange ;
* tu contrôles les freins.

Les petits problèmes sont corrigés immédiatement.

La voiture reste performante.

C'est exactement la même logique pour un modèle IA.

---

## À retenir

Le Kaizen privilégie :

* des améliorations fréquentes ;
* des petites corrections ;
* une progression constante.

Il ne faut pas attendre une catastrophe avant d'agir. 

---

# III. Le cycle PDCA

C'est probablement **la notion la plus importante du chapitre**.

PDCA signifie :

* **P : Plan**
* **D : Do**
* **C : Check**
* **A : Act** 

Ce cycle tourne en permanence.

```text
Plan
   ↓
Do
   ↓
Check
   ↓
Act
   ↓
(recommencer)
```

---

## 1. Plan (Préparer)

On identifie un problème.

Exemple :

Le modèle détecte mal les fraudes.

On prépare donc un plan :

* quelles données utiliser ?
* quelle méthode tester ?
* quels objectifs atteindre ?

---

## 2. Do (Faire)

On applique l'amélioration.

Par exemple :

* nouvel algorithme ;
* nouvelles données ;
* modification d'un paramètre.

---

## 3. Check (Vérifier)

On compare :

Avant :

* précision = 84 %

Après :

* précision = 91 %

On mesure si l'amélioration fonctionne réellement.

---

## 4. Act (Agir)

Deux cas :

Si l'amélioration fonctionne :

→ on la conserve.

Sinon :

→ on revient à l'ancienne version puis on recommence le cycle.

---

## Ce qu'il faut retenir

Le PDCA est une **boucle**.

Ce n'est pas une méthode que l'on applique une seule fois.

Elle recommence toute la vie du modèle. 

---

# IV. La méthode DMAIC

Autre méthode importante.

DMAIC vient du Lean Six Sigma.

Les lettres signifient :

* **Define**
* **Measure**
* **Analyze**
* **Improve**
* **Control** 

---

## Les cinq étapes

### Define

Définir précisément le problème.

Exemple :

Le modèle fait trop de faux positifs.

---

### Measure

Mesurer la situation.

Exemple :

12 % de faux positifs.

---

### Analyze

Chercher la cause.

Pourquoi ?

* mauvaises données ?
* mauvais paramètre ?
* dérive ?

---

### Improve

Apporter une solution.

Par exemple :

* nouvelles variables ;
* nouvel algorithme ;
* réentraînement.

---

### Control

Surveiller que le problème ne réapparaisse pas.

On revient donc au monitoring.

---

## Différence PDCA / DMAIC

| PDCA                  | DMAIC                                                  |
| --------------------- | ------------------------------------------------------ |
| Très général          | Plus détaillé                                          |
| Boucle d'amélioration | Résolution structurée d'un problème                    |
| Utilisé partout       | Très utilisé dans les processus industriels et qualité |

---

# V. Le cycle de vie complet d'un modèle IA

Le cours rappelle qu'un modèle suit toujours les mêmes grandes étapes : 

```text
Collecte des données
        ↓
Conception et entraînement
        ↓
Validation et tests
        ↓
Déploiement
        ↓
Monitoring
        ↓
Retraining
        ↓
Retour au début
```

Le **retraining** (réentraînement) consiste à entraîner de nouveau le modèle avec des données plus récentes afin qu'il reste performant.

---

# VI. Comment choisir les améliorations à réaliser ?

On ne peut pas tout améliorer en même temps.

Le cours propose une **priorisation**.

Les améliorations sont évaluées selon plusieurs critères :

* criticité métier ;
* valeur générée ;
* faisabilité technique ;
* scalabilité (capacité à fonctionner à grande échelle). 

---

## Exemple

Une entreprise possède 20 modèles IA.

Deux modèles présentent des problèmes.

### Modèle A

Erreur sur la couleur d'un bouton.

Impact :

faible.

---

### Modèle B

Erreur sur la détection de fraude bancaire.

Impact :

très élevé.

On améliore d'abord le modèle B.

---

# VII. La roadmap d'amélioration

Une **roadmap** est une feuille de route qui planifie les améliorations. Elle doit être équilibrée entre trois types d'actions. 

## 1. Quick Wins

Ce sont les améliorations :

* rapides ;
* peu coûteuses ;
* immédiatement visibles.

Exemple :

Corriger un mauvais prétraitement des données.

---

## 2. Chantiers de fond

Ils demandent plus de temps.

Exemple :

Changer totalement le pipeline de traitement.

---

## 3. Innovations de rupture

Ce sont des projets très innovants.

Exemple :

Tester une nouvelle architecture de Deep Learning ou une technologie encore expérimentale.

---

## Pourquoi mélanger les trois ?

Une bonne roadmap :

* produit des résultats rapidement (quick wins) ;
* prépare les évolutions importantes (chantiers de fond) ;
* anticipe l'avenir (innovations de rupture). 

---

# VIII. Le feedback utilisateur

Le modèle doit apprendre grâce aux utilisateurs.

Le cours distingue **trois formes de feedback**.

## 1. Feedback explicite

L'utilisateur donne volontairement son avis.

Exemple :

⭐⭐⭐⭐☆

ou

« Cette prédiction est incorrecte. »

---

## 2. Feedback implicite

L'utilisateur ne dit rien.

On observe simplement son comportement :

* clics ;
* refus d'une recommandation ;
* modification manuelle d'une prédiction. 

Exemple :

Un site recommande un produit.

L'utilisateur clique toujours sur "Ignorer".

Le système comprend que la recommandation est mauvaise.

---

## 3. Feedback expert

Des spécialistes évaluent directement le modèle.

Exemple :

Des médecins corrigent les diagnostics proposés par une IA médicale.

---

## Attention au biais

Le cours souligne un point essentiel : les retours des utilisateurs ne sont pas toujours représentatifs. Les personnes mécontentes ont souvent plus tendance à laisser un avis, ce qui peut biaiser les améliorations si l'on ne tient pas compte de cette surreprésentation. 

---

# IX. La capitalisation des connaissances

C'est une notion très importante.

## Définition

La **capitalisation** consiste à transformer chaque expérience (succès, échec, incident, optimisation) en une connaissance réutilisable par toute l'organisation. 

---

## Exemple

Un data scientist découvre une excellente méthode.

Deux possibilités :

### Mauvaise pratique

Il garde cette méthode pour lui.

Personne n'en profite.

---

### Bonne pratique

Il rédige :

* une fiche ;
* une documentation ;
* un wiki.

Toute l'entreprise peut réutiliser cette connaissance.

C'est la capitalisation.

---

## Pourquoi est-ce important ?

Elle permet de :

* éviter de refaire les mêmes erreurs ;
* partager les bonnes pratiques ;
* accélérer les futurs projets ;
* améliorer la maturité de l'organisation. 

---

# X. La veille technologique

Le domaine de l'IA évolue très vite.

Une entreprise doit donc mettre en place une **veille** afin de rester compétitive. 

Cela peut inclure :

* la lecture d'articles scientifiques ;
* la participation à des conférences ;
* des benchmarks ;
* des collaborations avec des laboratoires de recherche.

L'objectif est d'identifier rapidement les innovations utiles.

---

# XI. La communication autour de l'optimisation

Un même résultat ne se présente pas de la même manière selon la personne qui le reçoit.

Le cours parle de **communication différenciée**. 

## Exemple

Imaginons qu'un modèle gagne 6 % de précision.

### Au directeur

On dira :

> "Cette amélioration réduit le risque et augmente le retour sur investissement."

### Au data scientist

On présentera :

* précision ;
* rappel ;
* F1-score ;
* courbe ROC.

### Aux équipes métier

On expliquera :

> "Le système détecte davantage de cas corrects et fait moins d'erreurs."

Le message est identique, mais adapté au public.

---

# XII. Les tableaux de bord (Dashboards)

Un bon dashboard ne doit pas afficher toutes les métriques.

Il doit montrer les informations utiles selon le public concerné. 

Le cours recommande une structure en plusieurs niveaux :

* **niveau exécutif** : 3 à 5 KPI clés pour la direction ;
* **niveau technique** : métriques détaillées pour les équipes IA ;
* **niveau opérationnel** : alertes et informations utiles au quotidien.

---

# XIII. La transparence

Le cours insiste sur un principe essentiel : **ne pas cacher les problèmes**.

Un reporting de qualité doit présenter :

* les réussites ;
* les difficultés ;
* les limites du modèle ;
* les incertitudes ;
* le plan d'action prévu. 

Cette transparence renforce la confiance des décideurs, des métiers et des régulateurs.

---

# Les notions à retenir absolument pour l'examen

1. **Amélioration continue** : processus permanent d'optimisation d'un modèle IA.
2. **Kaizen** : petites améliorations régulières plutôt que grands changements ponctuels.
3. **PDCA** : Plan → Do → Check → Act.
4. **DMAIC** : Define → Measure → Analyze → Improve → Control.
5. **Roadmap** : feuille de route équilibrée entre quick wins, chantiers de fond et innovations de rupture.
6. **Priorisation** : basée sur la valeur métier, le risque, la faisabilité et la scalabilité.
7. **Feedback explicite, implicite et expert** : trois sources complémentaires d'amélioration.
8. **Capitalisation** : partager et documenter les connaissances pour éviter les silos.
9. **Communication différenciée** : adapter le message à chaque type d'interlocuteur.
10. **Transparence** : communiquer aussi les limites et les incertitudes du modèle.

## 📝 En une phrase

L'idée centrale du cours est que **la performance d'un modèle d'IA ne dépend pas seulement de sa conception initiale, mais surtout de sa capacité à être amélioré en continu**. Pour cela, il faut mettre en place une démarche structurée (Kaizen, PDCA ou DMAIC), recueillir les retours des utilisateurs, prioriser intelligemment les améliorations, partager les connaissances acquises et communiquer efficacement avec toutes les parties prenantes. Cette approche garantit des modèles plus performants, plus fiables et mieux alignés sur les besoins métier tout au long de leur cycle de vie. 
