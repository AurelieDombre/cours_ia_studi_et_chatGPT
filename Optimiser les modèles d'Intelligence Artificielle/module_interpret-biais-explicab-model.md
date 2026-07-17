Voici un **résumé détaillé et pédagogique** de ton cours **« Interprétabilité, biais et explicabilité des modèles »**, conçu pour comprendre les concepts et les mémoriser facilement.

---

# Résumé détaillé – Interprétabilité, biais et explicabilité des modèles

## Objectif du cours

Aujourd'hui, les modèles d'IA prennent des décisions importantes :

* accepter ou refuser un crédit,
* aider au recrutement,
* détecter une maladie,
* calculer un risque d'assurance.

Mais une simple réponse (« accepté » ou « refusé ») ne suffit plus.

Il faut pouvoir répondre à deux questions :

* **Comment le modèle fonctionne-t-il ?**
* **Pourquoi a-t-il pris cette décision ?**

Le but du cours est d'expliquer comment rendre un modèle **compréhensible**, **transparent** et **équitable**, afin d'inspirer confiance, de respecter la réglementation et d'améliorer les modèles.

---

# I. Pourquoi l'interprétabilité est-elle devenue indispensable ?

Il y a trois grandes raisons.

## 1. Une obligation juridique

En Europe, les entreprises doivent expliquer certaines décisions automatisées.

Deux réglementations sont importantes :

### Le RGPD

Le RGPD donne aux personnes concernées le droit d'obtenir une explication lorsqu'une décision importante est prise automatiquement.

Exemple :

Une banque refuse un crédit.

Le client peut demander :

> Pourquoi ai-je été refusé ?

L'entreprise doit être capable de répondre.

---

### L'AI Act

Le futur AI Act va encore plus loin.

Pour les systèmes d'IA considérés **à haut risque** (santé, recrutement, justice, crédit...), il faudra notamment :

* expliquer les décisions,
* documenter le fonctionnement du modèle,
* rendre le modèle auditable.

En résumé :

> Un modèle performant mais impossible à expliquer risque de ne plus être conforme à la réglementation.

---

## 2. Gagner la confiance des utilisateurs

Les utilisateurs veulent comprendre les décisions qui les concernent.

Par exemple :

* pourquoi un candidat n'a pas été retenu,
* pourquoi un prêt est refusé,
* pourquoi une assurance coûte plus cher.

Un modèle opaque (« boîte noire ») inspire de la méfiance.

À l'inverse, un modèle capable d'expliquer ses décisions favorise :

* la confiance,
* l'acceptation,
* une meilleure collaboration entre les experts métier et les data scientists.

---

## 3. Améliorer les modèles

L'interprétabilité ne sert pas uniquement à expliquer.

Elle permet aussi de découvrir :

* des biais,
* des erreurs,
* des variables inutiles,
* des comportements inattendus.

Autrement dit :

> Expliquer un modèle aide aussi à le rendre meilleur.

---

# II. Interprétabilité et explicabilité : quelle différence ?

C'est une notion très importante.

## L'interprétabilité

Elle consiste à comprendre **comment le modèle fonctionne à l'intérieur**.

Exemple :

Un arbre de décision.

On peut suivre chaque règle.

```
Si revenu > 3000 €
    alors accepter
Sinon
    refuser
```

On comprend directement la logique.

---

## L'explicabilité

Elle consiste à expliquer **une décision**, même si le modèle est très complexe.

Exemple :

Un réseau de neurones.

On ne comprend pas directement son fonctionnement.

Mais on peut expliquer pourquoi il a pris une décision grâce à des outils spécialisés.

À retenir :

> **Interprétabilité = comprendre le modèle.**
>
> **Explicabilité = expliquer une décision.**

Une IA peut être explicable sans être réellement interprétable.

---

# III. L'interprétabilité globale

L'interprétabilité globale cherche à comprendre le fonctionnement général du modèle.

Elle répond à des questions comme :

* quelles variables sont les plus importantes ?
* le modèle est-il logique ?
* suit-il les règles métier ?

---

## A. La Feature Importance

La Feature Importance mesure l'importance moyenne d'une variable sur toutes les prédictions.

Exemple :

Un modèle prédit le risque de défaut de paiement.

Importance des variables :

* revenu : 40 %
* historique bancaire : 30 %
* âge : 15 %
* profession : 10 %
* ville : 5 %

On voit immédiatement quelles variables influencent le plus les décisions.

Attention :

Une variable très importante n'est pas forcément une bonne variable.

Elle peut révéler un biais.

---

## B. Feature Importance vs Feature Attribution

Ces deux notions sont souvent confondues.

### Feature Importance

Elle explique le modèle **dans son ensemble**.

On regarde toutes les prédictions.

---

### Feature Attribution

Elle explique **une seule prédiction**.

Exemple :

Pourquoi ce client précis a été refusé ?

Les variables peuvent être totalement différentes de la moyenne.

---

# IV. Visualiser l'effet des variables

Connaître l'importance d'une variable ne suffit pas.

Il faut aussi comprendre **comment** elle influence le résultat.

Deux outils sont présentés.

---

## PDP (Partial Dependence Plot)

Le PDP montre comment la prédiction évolue lorsqu'une variable change.

Exemple :

Quand le taux d'endettement augmente :

* le risque augmente doucement,
* puis brutalement après 40 %.

Le graphique permet de repérer :

* des seuils,
* des ruptures,
* des comportements anormaux.

---

## ICE (Individual Conditional Expectation)

Le principe est proche du PDP.

Mais cette fois, on observe le comportement pour **chaque individu**, et non pour la moyenne.

Le PDP montre une tendance générale.

L'ICE montre les différences entre les individus.

---

# V. Les modèles « boîte noire »

Certains modèles sont difficiles à comprendre.

Exemples :

* réseaux de neurones,
* modèles très complexes.

Pour les expliquer, on peut créer un **Surrogate Model**.

## Le Surrogate Model

C'est un modèle simple (souvent un arbre de décision) qui imite le modèle complexe.

Le modèle complexe continue à faire les prédictions.

Le modèle simple sert uniquement à expliquer sa logique générale.

---

# VI. L'interprétabilité locale

L'interprétabilité locale cherche à répondre à une question :

> Pourquoi cette décision précise a-t-elle été prise ?

On ne regarde qu'un seul individu.

Exemple :

Pourquoi ce client a-t-il obtenu un score de risque élevé ?

---

## SHAP

SHAP est aujourd'hui l'un des outils les plus utilisés.

Son principe :

Chaque variable reçoit une contribution.

Exemple :

Pour un client :

* âge : +15 %
* revenu : -10 %
* dettes : +35 %
* ancienneté : -5 %

On comprend exactement pourquoi la décision a été prise.

SHAP est très fiable et fournit des explications cohérentes.

---

## LIME

LIME adopte une approche différente.

Il construit un modèle très simple autour du cas étudié.

Puis il observe quelles variables influencent la décision.

LIME est :

* plus rapide,
* compatible avec presque tous les modèles.

En revanche, ses résultats peuvent être moins stables que ceux de SHAP.

---

## SHAP ou LIME ?

| SHAP                    | LIME                                |
| ----------------------- | ----------------------------------- |
| Très précis             | Plus rapide                         |
| Stable                  | Peut varier selon les cas           |
| Plus coûteux à calculer | Léger et simple                     |
| Explications robustes   | Explications locales approximatives |

---

# VII. Les cartes de saillance

Elles concernent les modèles qui analysent des images.

Le principe :

On colore les zones qui ont attiré l'attention du modèle.

Exemple :

Une IA détecte une tumeur.

La carte montre si le modèle regarde :

* la tumeur (bon comportement),
* ou un coin de l'image (mauvais comportement).

Cela permet de vérifier que le modèle raisonne correctement.

---

# VIII. Détecter les biais

L'explicabilité permet de découvrir des biais invisibles.

Par exemple :

Le modèle refuse davantage :

* les jeunes,
* certaines régions,
* certains profils.

Les statistiques globales peuvent sembler excellentes.

Mais lorsqu'on étudie les groupes séparément, des injustices apparaissent.

---

## Les variables proxy

Une variable proxy paraît neutre.

Mais elle cache une information sensible.

Exemple :

Le code postal.

En réalité, il peut révéler :

* le niveau social,
* l'origine,
* certains quartiers.

Le modèle discrimine alors sans utiliser directement une variable interdite.

C'est un biais difficile à détecter.

---

# IX. Valider les hypothèses métier

Les experts métier possèdent une connaissance du terrain.

Grâce à l'interprétabilité, on peut vérifier si le modèle raisonne comme eux.

Deux situations peuvent apparaître.

### Cas 1

Une variable très importante pour les experts n'influence presque pas le modèle.

Il faut comprendre pourquoi.

---

### Cas 2

Une variable jugée secondaire devient la plus importante.

Cela révèle souvent :

* un biais,
* une erreur de données,
* une variable proxy.

Les experts métier doivent donc toujours participer à l'analyse des résultats.

---

# X. Corriger les biais

Une fois le problème identifié, plusieurs solutions existent.

## Modifier les variables

Certaines variables peuvent être :

* supprimées,
* transformées,
* remplacées.

---

## Rééquilibrer les données

Si certains groupes sont peu représentés :

* ajouter davantage d'exemples,
* rééchantillonner les données.

---

## Segmenter les modèles

Parfois, un seul modèle ne suffit pas.

On peut créer plusieurs modèles spécialisés selon les profils.

---

## Tester les corrections

Chaque modification doit être vérifiée.

Le cycle est toujours :

```
Explication
        ↓
Détection du problème
        ↓
Correction
        ↓
Validation
```

C'est le principe de l'amélioration continue.

---

# XI. Les notions essentielles à connaître

| Notion                  | Définition simple                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------- |
| **Interprétabilité**    | Comprendre le fonctionnement interne d'un modèle.                                      |
| **Explicabilité**       | Expliquer une décision prise par un modèle, même complexe.                             |
| **RGPD**                | Règlement imposant un droit à l'explication des décisions automatisées importantes.    |
| **AI Act**              | Futur règlement européen renforçant les obligations pour les IA à haut risque.         |
| **Feature Importance**  | Importance moyenne d'une variable sur toutes les prédictions.                          |
| **Feature Attribution** | Contribution d'une variable pour une prédiction précise.                               |
| **PDP**                 | Graphique montrant l'effet moyen d'une variable sur la prédiction.                     |
| **ICE**                 | Graphique montrant l'effet d'une variable pour chaque individu.                        |
| **SHAP**                | Méthode expliquant précisément la contribution de chaque variable à une décision.      |
| **LIME**                | Méthode créant un modèle local simplifié pour expliquer rapidement une prédiction.     |
| **Carte de saillance**  | Visualisation des zones d'une image ayant le plus influencé le modèle.                 |
| **Variable proxy**      | Variable apparemment neutre qui cache une information sensible et peut créer un biais. |
| **Surrogate Model**     | Modèle simple utilisé pour expliquer globalement un modèle complexe.                   |

# La méthode à retenir pour l'examen

Tu peux mémoriser cette **démarche en 6 étapes** :

1. **Comprendre pourquoi l'interprétabilité est importante** (réglementation, confiance, amélioration).
2. **Distinguer interprétabilité et explicabilité**.
3. **Analyser le modèle globalement** (Feature Importance, PDP, ICE).
4. **Expliquer une décision individuelle** (SHAP, LIME, cartes de saillance).
5. **Détecter les biais** (groupes, variables proxy, comparaison avec l'expertise métier).
6. **Mettre en place des actions correctives**, puis vérifier que les biais ont réellement diminué.

💡 **Conseil pour réviser :** commence par apprendre les différences entre **interprétabilité** et **explicabilité**, puis maîtrise les principaux outils (**Feature Importance, PDP, SHAP, LIME**). Enfin, retiens que leur objectif commun est de **rendre les modèles plus transparents, plus équitables et plus fiables**, tout en respectant les exigences réglementaires.
