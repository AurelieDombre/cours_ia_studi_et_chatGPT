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

L’interprétabilité se définit comme la capacité pour un humain à comprendre les raisons d’une décision d’un modèle. Ce critère est devenu prépondérant pour de nombreuses raisons.

Au niveau scientifique, le développement des connaissances et le progrès reposent sur la compréhension profonde du phénomène étudié. Il est donc inimaginable pour un data scientist de laisser fonctionner un modèle de machine learning sans chercher à connaître les variables influentes, sans chercher à vérifier la cohérence des résultats à la lumière des connaissances métier du domaine, … Il s’agit de comprendre, d’avoir confiance et d’avoir une preuve de la consistance du modèle.

Au niveau éthique : imaginons une situation dans laquelle un individu est atteint d’un cancer. Il se voit refuser son intervention chirurgicale à cause de la seule décision d’un algorithme. De plus, par nature cet algorithme sera complexe et alors aucun chirurgien ne sera en capacité de justifier une telle décision. Cette situation n’est pas acceptable.

Il y a trois grandes raisons.

## 1. Une obligation juridique

En Europe, les entreprises doivent expliquer certaines décisions automatisées.

Deux réglementations sont importantes :

### Le RGPD

Le RGPD donne aux personnes concernées le droit d'obtenir une explication lorsqu'une décision importante est prise automatiquement.
l’article 22 de la RGPD (Règlement Général sur la Protection des Données) prévoit qu’une personne ne doit pas faire l’objet d’une décision fondée exclusivement sur un traitement automatisé et émanant uniquement de la décision d’une machine.

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
La mise en œuvre de SHAP repose sur une méthode d’estimation des valeurs de Shapley. Il existe différentes méthodes d’estimation comme le KernelSHAP (méthode inspirée de LIME) ou le TreeSHAP (méthode à base d’arbres de décision).
SHAP est aujourd'hui l'un des outils les plus utilisés.

Son principe :

Chaque variable reçoit une contribution.
Pour un individu donné, la valeur de Shapley d’une variable (ou de plusieurs variables) est sa contribution à la différence entre la valeur prédite par le modèle et la moyenne des prédictions de tous les individus.

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
un modèle local qui cherche à expliquer la prédiction d’un individu par analyse de son voisinage

Puis il observe quelles variables influencent la décision.

LIME est :

* plus rapide,
* compatible avec presque tous les modèles.
* Interprétable. Il fournit une compréhension qualitative entre les variables d’entrée et la réponse. Les relations entrées-sortie sont faciles à comprendre.
* Simple localement. Le modèle est globalement complexe, il faut alors chercher des réponses localement plus simples.
* Agnostique. Il est capable d’expliquer n’importe quel modèle de machine learning.

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

Bien sûr. C'est une notion qui pose souvent problème au début, car **SHAP et LIME font la même chose, mais pas de la même manière**.

Je vais te l'expliquer avec un exemple très simple.

---

# Imaginons une banque

Tu demandes un prêt bancaire.

Le modèle d'IA répond :

❌ **Prêt refusé**

Tu demandes :

> **"Pourquoi ?"**

Le modèle est un énorme réseau de neurones.

Personne ne peut facilement suivre tous ses calculs.

On utilise donc **LIME** ou **SHAP** pour obtenir une explication.

---

# LIME : "Je regarde autour de toi"

Imagine que tu regardes une montagne.

Tu ne peux pas comprendre toute la montagne.

Alors tu observes seulement **l'endroit où tu te trouves**.

C'est exactement ce que fait LIME.

Il dit :

> "Je ne vais pas essayer de comprendre tout le modèle.
>
> Je vais seulement comprendre pourquoi CETTE personne a été refusée."

---

## Comment fait LIME ?

Il crée plein de clients **qui ressemblent au tien**.

Exemple :

Ton dossier :

| Âge    | Salaire | Dettes |
| ------ | ------- | ------ |
| 30 ans | 2000 €  | 900 €  |

LIME invente des dossiers proches :

| Âge    | Salaire | Dettes |
| ------ | ------- | ------ |
| 31 ans | 2000 €  | 900 €  |
| 30 ans | 2100 €  | 900 €  |
| 30 ans | 1900 €  | 850 €  |
| 29 ans | 2000 €  | 950 €  |

Puis il regarde :

> "Quand je change un peu le salaire, que se passe-t-il ?"

> "Quand je baisse les dettes, que se passe-t-il ?"

À partir de ces essais, il construit **un petit modèle très simple** (souvent une régression linéaire ou un arbre de décision).

Il conclut par exemple :

```
Refus du prêt

+ Dettes élevées
- Salaire faible
+ Peu d'ancienneté
```

LIME ne comprend donc **que ton cas**, pas tout le modèle.

---

# Une image pour retenir LIME

Imagine Google Maps.

Tu fais un zoom.

```
France
      ↓
Paris
      ↓
Ton quartier
      ↓
Ta rue
```

LIME regarde uniquement **ta rue**.

Pas toute la France.

👉 **LIME = explication locale.**

---

# SHAP : "Chaque variable reçoit une note"

SHAP fait quelque chose de différent.

Il ne construit pas un petit modèle.

Il cherche :

> **"Combien chaque variable a-t-elle contribué à la décision ?"**

Chaque variable reçoit une sorte de "score".

---

Prenons notre client.

Le modèle donne :

```
Risque = 80 %
```

SHAP explique :

| Variable            | Contribution |
| ------------------- | ------------ |
| Salaire             | −20 %        |
| Dettes              | +40 %        |
| Âge                 | +10 %        |
| Historique bancaire | +15 %        |
| Épargne             | −5 %         |

On additionne :

```
40
+10
+15
-20
-5
------
40 %
```

Chaque variable pousse la décision :

➡ vers le refus

ou

➡ vers l'acceptation.

---

# Une image pour retenir SHAP

Imagine que cinq amis portent une table.

```
Alice porte 40 %

Paul porte 20 %

Léa porte 15 %

Tom porte 15 %

Emma porte 10 %
```

Tu peux dire exactement :

> **Qui a fait le plus d'effort ?**

SHAP fait pareil.

Il mesure la contribution de **chaque variable** dans la décision finale.

---

# La grande différence

## LIME

Il dit :

> "Je vais simplifier le modèle autour de CE client."

Il fabrique un petit modèle local.

Il est rapide.

Mais si tu recommences plusieurs fois, l'explication peut changer.

---

## SHAP

Il dit :

> "Je vais calculer précisément la contribution de chaque variable."

Il ne simplifie pas le modèle.

Il utilise une méthode mathématique inspirée de la **théorie des jeux** (les valeurs de Shapley), qui répartit "le mérite" ou "la responsabilité" entre toutes les variables.

Ses explications sont plus fiables.

Mais elles demandent beaucoup plus de calculs.

---

# Exemple concret

Le modèle refuse ton prêt.

## LIME répond

> "Autour de ton dossier, j'observe que les dettes et le salaire expliquent principalement le refus."

Il donne une **explication approximative mais rapide**.

---

## SHAP répond

```
Salaire      : -18 %
Dettes       : +41 %
Âge          : +8 %
Épargne      : -6 %
Historique   : +12 %
```

Tu sais précisément **combien chaque variable a influencé la décision**.

---

# Une analogie très simple

Imagine un professeur qui met une note de **14/20** à un exposé.

### LIME

Le professeur dit :

> "Globalement, tu as perdu des points à cause de ton introduction et de ta conclusion."

C'est une explication simple et locale.

---

### SHAP

Le professeur détaille exactement :

* Introduction : **−2 points**
* Contenu : **+8 points**
* Illustrations : **+4 points**
* Conclusion : **−1 point**
* Questions : **+5 points**

Tu connais la contribution de chaque partie à la note finale.

---

# Le tableau à retenir pour l'examen

| LIME                                            | SHAP                                       |
| ----------------------------------------------- | ------------------------------------------ |
| Explique une décision locale                    | Explique une décision locale               |
| Crée un petit modèle simple autour de l'exemple | Calcule la contribution de chaque variable |
| Rapide                                          | Plus lent                                  |
| Approximation                                   | Très précis                                |
| Les résultats peuvent varier                    | Les résultats sont stables                 |

## 🎓 L'astuce pour ne plus les confondre

* **LIME = Loupe** 🔍 → il **zoome** sur un seul exemple et construit une explication locale.
* **SHAP = Score** 📊 → il attribue un **score de contribution** à chaque variable pour expliquer la décision.

Si tu retiens **"LIME = loupe locale"** et **"SHAP = score de chaque variable"**, tu auras déjà compris l'essentiel demandé dans la plupart des examens.


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
