# Techniques de débogage pour les modèles de Machine Learning et Deep Learning 

![Main](https://images.openai.com/static-rsc-4/R0CjogpfR6l8QQEw9traHbRca3NyKZ7t2lLR2gKS6kuVWCez-Zv71O2rkUP9Ku2z7XYRfgQZbB2u503yqwL9QjTmoiWrBdJYzhKnulU1uUphsU-2BaSsb2b87IyHTxWyx45Un7RvLcZud0mLsxeRBbT80UwFgAg6gOxBdx_edx4oYVmMYQA4R64rJW1M9yT0?purpose=fullsize)

### L'idée centrale du cours

Le message principal est simple :

En IA, la plupart des erreurs ne viennent pas du modèle lui-même, mais de l'ensemble du pipeline.

Un problème peut provenir :

* des données,

* du prétraitement,

* des hyperparamètres,

* de l'architecture,

* de l'environnement d'exécution,

* ou du code.

Le débogage IA consiste donc à isoler méthodiquement la cause racine plutôt qu'à modifier le modèle au hasard. Le cours insiste sur une démarche scientifique : observation → hypothèses → expérimentation → analyse → itération. La reproductibilité, l'isolation des composants et la traçabilité des expériences sont présentées comme indispensables pour localiser rapidement l'origine d'un bug. La simplification progressive, l'ablation, les comparaisons contrôlées et les tests unitaires adaptés à l'IA font partie des stratégies clés. En Deep Learning, il faut en plus diagnostiquer les problèmes de gradient, ajuster batch size et learning rate, doser la régularisation et maîtriser le transfert learning. Le pipeline d'IA couvre la collecte, la préparation, le feature engineering, l'entraînement, la validation, le déploiement et l'inférence. Le débogage stochastique rappelle que les résultats peuvent varier d'une exécution à l'autre à cause des batchs, seeds ou augmentations de données, d'où la nécessité d'analyser des distributions de résultats plutôt qu'un seul run. Le cycle itératif complet comprend aussi la documentation systématique de chaque test.

techniq-debog-model-mach-learn.pdf.

### I. Pourquoi le débogage IA est plus difficile que le débogage classique ?

Dans un logiciel classique, un bug provoque souvent :

* un crash,

* une exception,

* un message d'erreur explicite.

En IA, le modèle peut continuer à fonctionner tout en produisant de mauvaises prédictions.

Exemples :

* la précision baisse progressivement,

* certaines catégories deviennent mauvaises,

* les résultats changent d'un entraînement à l'autre,

* le problème n'apparaît que sur certains segments.

La difficulté vient notamment de la stochasticité :

* initialisation aléatoire,

* ordre des batchs,

* augmentation de données,

* sampling.

👉 On raisonne donc souvent en tendances statistiques plutôt qu'en cas uniques.

techniq-debog-model-mach-learn.pdf

### II. Le pipeline d'IA : la carte mentale à retenir

![Machine Learning Pipeline: Data Collection to Model Deployment | Ankur Ranjan posted on the topic | LinkedIn](https://images.openai.com/static-rsc-4/4z49EmvtT1L7nXIrbOUyoY3ko5jVZwoUQb_pUoO3_EURFjhN__CPvqUJUeqVQlIczO6LpMsyJgu08nh_GESh2FqUlw1VRdSlllu9HhQHZ49KjlIqnGi0JE5ot2i-D3M-fDRwM9pQuwWEstA_c6GdFf3Js2ZjFLYF1kOT_JevjCEAyfHpeDoDkLCq35T7PLLO?purpose=fullsize)

Le pipeline complet est :

Collecte des données

Préparation / nettoyage

Feature engineering

Entraînement

Validation

Déploiement

Inférence

Chaque maillon peut contenir une erreur.

Exemple classique du cours :

Le modèle médical se dégrade après un changement de scanner ; la cause réelle est un prétraitement de couleur devenu incorrect.

techniq-debog-model-mach-learn.pdf

💡 À retenir : Toujours tester chaque étape séparément.

### III. La méthode de débogage en 6 étapes

![Writing More Successful Machine Learning Research Papers | by Prof. Marc Aubreville | TDS Archive | Medium](https://images.openai.com/static-rsc-4/oXGD5wb_pPaNIerd_163hzoJCOulxRN7xhECo3SwiExL8jnP5gyoZgA6fJLXJDFTliZWbwrSyJPHb3ogHnBsY4nHlv2DsAn6hnt1uedPAnF-FcA20XBVoHw6x1oeKp27JOMFYx3m5jPcz0t16rUvpxvOznoiehAZOKa57szZaNGfrlPN2IGr0J8RuHAXuczq?purpose=fullsize)

C'est probablement la partie la plus importante du cours.

1

Observation

Noter précisément les symptômes, dates, logs, métriques.

2

Hypothèses

Lister plusieurs causes possibles (données, code, modèle, infra).

3

Expérimentation

Modifier un seul élément à la fois.

4

Analyse

Mesurer l'effet du changement.

5

Itération

Recommencer si nécessaire.

6

Documentation

Garder l'historique de tous les essais.

Le cours insiste :

Ne jamais changer plusieurs choses en même temps.

Sinon, on ne sait plus ce qui a réellement amélioré ou dégradé le modèle.

techniq-debog-model-mach-learn.pdf

### IV. Reproductibilité : la règle d'or

![5 Reproducible ML Habits: Seeds to Dataset Locks | by Vectorlane | Medium](https://images.openai.com/static-rsc-4/m1JKrHc3dggDCr9LpIWH8lo8O45CjiRg1SBvZeu6L14dulTquWNR0sLjT7QWb3p8n9dH2T9jtJLG2vmFr1yE1K3ksfiVA_bnq7immaJqZ7vs86a0SOtUC5O3NMve2qprLEvEQc3qfzhI6zTtQUZy5s4qXjJljj-b6RsrcGZ26MJGren20FNvLGb_HJQEW-ui?purpose=fullsize)

Pour pouvoir retrouver un bug, il faut pouvoir rejouer exactement l'expérience.

Le cours recommande :

* fixer les seeds aléatoires,

* geler les versions logicielles,

* versionner les données,

* journaliser les expériences (MLflow, DVC, etc.),

* sauvegarder les checkpoints.

Exemple marquant :

Une équipe d'assurance a découvert qu'un changement d'heure d'hiver décalait les timestamps et faussait les prédictions. Sans environnement reproductible, le bug serait resté invisible.

techniq-debog-model-mach-learn.pdf

💡 Mnémo : SVDJ = Seeds, Versions, Données, Journalisation.

### V. Stratégies de débogage systématique

### 1. Simplification progressive

![The Black Box Problem: Why AI Must Learn to Explain Itself | by Iqra Naeem | Medium](https://images.openai.com/static-rsc-4/Ncybs6zqTfOYinbmGHoZmvGiYJcQmqym0eQB6XvP6ARvssCQC7eK9TE_fnfgzxt80TU-LS_gbloPGA6MaZuqjSNIpH8Np8TzupwpZeH7jh4ieBFudSSANZHxRmPp4ANlRjFX9sZE8-Jv_gruofjvFFzW_Zkb34k0gO8zqOrWJGf3CH5SKwyxBnzSJZZbXjGB?purpose=fullsize)

Quand le système est trop complexe, on le réduit progressivement.

On peut enlever :

* des features,

* des couches,

* des modules,

* des transformations.

Si le bug disparaît après suppression d'un composant, ce composant devient suspect.

Exemple du cours :

Un surapprentissage n'apparaissait qu'à partir d'une certaine profondeur de réseau ; la vraie cause était une mauvaise gestion du dropout dans les couches profondes.

techniq-debog-model-mach-learn.pdf

### 2. Ablation

Définition :

Retirer une composante et observer l'effet.

Exemple :

* retirer la feature revenu,

* retirer une couche CNN,

* retirer un module d'attention.

Si l'erreur disparaît → la composante était probablement impliquée.

techniq-debog-model-mach-learn.pdf

### 3. Comparaisons contrôlées

Comparer :

| Version A  | Version B |
| ---------- | --------- |
| fonctionne | échoue    |

Puis identifier la seule différence significative.

Très utile après une mise à jour de modèle ou de pipeline.

techniq-debog-model-mach-learn.pdf

### VI. Débogage des données (la cause n°1)

![Tools for Data Diagnosis, Exploration, Transformation • dlookr](https://images.openai.com/static-rsc-4/LoARbGnQFPcdfF3QbxmV1WmL3zcOxpR6EM-8plyG6owv3K5mTy98hJ-B2-a97aI-vMiMQnDjKFSycLvSLuX-MYpawbDFW54WPHpCBpDdydXyTfA-urkd2wFPbREpsXc2DZ8adG3jW5WmGYxahUBJta9ljnfA4P0tEU0tlAlpg0qGB8N2UB4fN-kRGPNVHmaR?purpose=fullsize)

Le cours affirme que la majorité des bugs ML viennent des données.

### À vérifier systématiquement

* Valeurs manquantes

* Outliers (valeurs extrêmes)

* Doublons

* Types incorrects

* Catégories incohérentes

* Biais de collecte

* Data leakage

### Outlier

Observation très éloignée de la tendance normale.

Exemple :

| Client | Dépense  |
| ------ | -------- |
| A      | 120 €    |
| B      | 135 €    |
| C      | 20 000 € |

Le client C est un outlier.

Il peut signaler :

* une erreur de saisie,

* une fraude,

* un événement exceptionnel.

### Data leakage (très important pour l'examen)

La cible ou une information du futur fuit dans les features.

Exemple :

On utilise la variable "montant remboursé après le prêt" pour prédire si le prêt sera remboursé.

Le modèle triche et obtient des performances artificiellement excellentes.

techniq-debog-model-mach-learn.pdf

### Bugs silencieux du prétraitement

Ils ne provoquent aucun crash.

Exemples :

* normalisation appliquée deux fois,

* colonnes inversées,

* mapping catégoriel incorrect,

* changement discret de librairie.

Le seul symptôme est souvent une dérive lente des performances.

techniq-debog-model-mach-learn.pdf

### VII. Déséquilibre de classes

![The Metrics Are Lying — A Hands-On Guide to Avoiding Data Illusions | by Aria Lucent | Data Science Collective | Medium](https://images.openai.com/static-rsc-4/VialnANZesjqzA5diLnwYXx7dHibxHpKxTcuOTU8K19ccZjB8SUDk194_ZSQhHsEzwHhtFgs_wxr4qiBRoIkio_rOxvkc-fxDK7rYtqlaZ7hzo0t6QW9oj1bOfxAf8a6yGSCfI23J1MpXD7995wem5lXySFuZ_Uj8GepPcrUAYwpOtdKSZSfQhz97sPhK0Jw?purpose=fullsize)

Problème fréquent :

| Classe     | Nombre |
| ---------- | ------ |
| Non fraude | 99 000 |
| Fraude     | 1 000  |

Le modèle peut prédire toujours "non fraude" et obtenir 99 % d'accuracy.

Le cours recommande de regarder :

* précision,

* rappel,

* F1-score,

* matrice de confusion.

### Solutions

* SMOTE (sur-échantillonnage synthétique),

* sous-échantillonnage,

* pondération de la loss,

* algorithmes spécialisés.

⚠️ Toujours valider sur un jeu de test indépendant après rééquilibrage.

techniq-debog-model-mach-learn.pdf

### VIII. Sous-apprentissage (Underfitting)

![Generalization | ML System Design in a Hurry](https://images.openai.com/static-rsc-4/wOtqaf0Qyjr_WqGoIQM5zzJe_pUrKdvRwNzJWN7OU7NqA3wboURLmgAlRYbm4xne_YF-nyJps5TKYQX_UPYv89DXXQCmrXYaRVc6JygIbwFmeyumW8cDImSgomGgvjCOzSxs3XFUg1jdG2HUwcxaRs2_DjTCBRKXkw3uixIKmJy_jcIFUVr4t9NRQOmqvrSe?purpose=fullsize)

Définition :

Le modèle est trop simple et n'apprend pas la structure des données.

Symptôme :

Erreur entraînement

Élevée

Erreur validation

Élevée

Les deux courbes restent mauvaises.

### Causes

* modèle trop simple,

* trop de régularisation,

* features peu informatives,

* pas assez de données.

### Corrections

* augmenter la capacité,

* ajouter de meilleures features,

* réduire la régularisation excessive.

techniq-debog-model-mach-learn.pdf

### IX. Problèmes de convergence

![Learning Rate: The One Hyperparameter That Actually Matters | by Bhargavi Guddati | Mar, 2026 | Medium](https://images.openai.com/static-rsc-4/0vOyEkFBSIrg-mkObMxn8n4WdvKsvqmlGTWNs2GlBgjHy9VxvVUAHjXZTSsDWIo3ym0Cfe8uOhHaCvDUmhAhbrR-qgdYfCu6ModZ7s5CwBi2zfhtyHLDFVjNKCrhmUcCRZp-5V2Id9g5NIZL7AxwhZX2MVBQ4-xfiCuqR47l47eM3p-KVgDlrzllU42-sebc?purpose=fullsize)

La loss :

* oscille,

* stagne,

* diverge.

Le cours conseille de vérifier :

* la fonction de coût,

* le learning rate,

* l'initialisation des poids,

* la normalisation des données,

* la cohérence des gradients.

💡 Un learning rate scheduler peut aider à sortir d'un plateau.

techniq-debog-model-mach-learn.pdf

### X. Hyperparamètres : la règle absolue

![Parameter Tuning Techniques: Grid Search, Random Search, and Bayesian Optimization | Jillani SoftTech | Artificial intelligence](https://images.openai.com/static-rsc-4/J70OB6Qo9gmMjwRi43NHZ5UTKu7p3YWaSPOkYlhqbI4hX3lN97yUG3R7oegFnhRgqYi6mVtEwI0eZHHQGct44qUksJNZYWVMfO-cMaBuRKP2r8uwFLLtZpSHOtlhkUyVJc7hJI2N79eCpnXQhMw0BTuwxgOpkp85oWSuhkq9oKiYEwqn44ceeIUgrlKWFGxe?purpose=fullsize)

Le cours répète :

Modifier un seul hyperparamètre à la fois.

Exemples :

* learning rate,

* batch size,

* nombre de couches,

* profondeur d'arbres,

* dropout,

* L1/L2.

Méthodes de recherche :

* Grid Search

* Optimisation bayésienne

* Recherche incrémentale

⚠️ Vérifier chaque gain sur plusieurs splits pour éviter un faux progrès.

techniq-debog-model-mach-learn.pdf

### XI. Deep Learning : les problèmes de gradient

![How a 1967 Algorithm Stabilized Modern Large Language Models | by Akhilesh Pant (APX) | Jan, 2026 | Medium](https://images.openai.com/static-rsc-4/kFhvc70GlO-5ej9xo1R0IcYIJXiEUl2HYhfL5cCAcFrzVVMFe2w1OqCaFcU22mH_bTEhU5yyKrGfQodf6_tETq-XtbUaDzn0bE5TAJTrvyfvSIKg7LI-ChgQbl9AoUDoT7HDWN8hReE6vvdvOTo1naqUbJgsgTENZRi9HKSIw4BDi9iN2HJZaHqNVptlJzBO?purpose=fullsize)

### Gradient vanishing

Le gradient devient presque nul.

Conséquence :

* les couches profondes n'apprennent plus,

* l'entraînement se bloque.

Solutions :

* ReLU / Leaky ReLU,

* BatchNorm,

* initialisation He/Xavier.

### Gradient explosion

Le gradient devient énorme.

Conséquence :

* instabilité numérique,

* divergence de la loss.

Solutions :

* gradient clipping,

* BatchNorm,

* learning rate plus faible.

Le diagnostic se fait en visualisant les gradients couche par couche (TensorBoard, Weights & Biases).

techniq-debog-model-mach-learn.pdf

### Neurone mort

Un neurone retourne toujours la même valeur (souvent 0).

Cela réduit la capacité d'apprentissage du réseau.

techniq-debog-model-mach-learn.pdf

### XII. Architecture : trop grosse ou trop petite ?

![Model selection — Data Science Academy](https://images.openai.com/static-rsc-4/PNf2Ry-B7fZJFohHVVp0lhhxtOzLqAJfkv8tglpYhJEuv1yXZ3ZJc43g3rTNN0xa5xjjNYy5MvQ3sSBaUxNgpGhZohYuLlqxPMpYmJNuf4MM6WSHwtb0TTeOWSqAu9kDGbL_D3iQMfo9gK_spAh8qDWn2H9b_TnzJ7U6nCXSHPwPnAEB-VR7J_bZl8HLHpG6?purpose=fullsize)

| Trop simple                              | Trop complexe                     |
| ---------------------------------------- | --------------------------------- |
| Sous-apprentissageFaibles scores partout | SurapprentissageMémorise le bruit |

Le cours met en garde contre :

"Toujours plus gros" ≠ toujours meilleur.

Ajouter des couches augmente :

* la complexité,

* le coût calculatoire,

* le risque de bugs subtils.

techniq-debog-model-mach-learn.pdf

### XIII. Transformers et RNN : problèmes spécifiques

![Exploring the Gated Attention Exploration Paper by Qwen : Best Paper Winner ar NeurIPS 2025 | by Abu Huzaifah Bin Haji Bidin | Medium](https://images.openai.com/static-rsc-4/p6icbEH0ff41DQzYOGwLXQ4l499CBR-wK9afoEbxBAxKWOSaLHfxSJY0GTyQ4EfxogCUip360hKDMG6T9_ZHrJJDubdp7o63noLkmrcRm7u54MPCBlvZUTdqhozlO11qS-M4SyLyhNJRzUhgHYwe-NCeDFCdu9dL34L4tHhKBsA5GguSCj5m3sSaSvp9bWmG?purpose=fullsize)

### RNN / LSTM

Problème principal : oubli des dépendances longues (gradient qui s'efface).

### Transformers

Problème principal : attention défectueuse.

Symptômes :

* certains tokens monopolisent l'attention,

* la fin des phrases est ignorée,

* les longues séquences se dégradent.

Le cours recommande :

* visualiser les poids d'attention,

* tester des phrases très longues,

* surveiller les gradients dans le temps.

Exemple :

Un système de traduction oubliait systématiquement la fin des phrases de plus de 30 tokens.

techniq-debog-model-mach-learn.pdf

### XIV. Batch size et Learning rate

![Optimizing Deep Learning Models](https://images.openai.com/static-rsc-4/JNJHewN2ru5p0Nnf9XGATT-M36NdmHuVCLsujkN2h7E8HTskoJ3yAYeP20kAkk4aeJxGBtOW_K3Qrvwy1CsMp5rE-Gsi10stUWq1_s0pjybJVRrdbhf0hd2JpMOkSTBOASiPaD0LUfQUczISw9wHUl7bprvRhFO211HN-8SOmtL54vzSjqrjdZLklB2H7eQ9?purpose=fullsize)

| Paramètre        | Problème typique                  |
| ---------------- | --------------------------------- |
| LR trop élevé    | Loss qui diverge                  |
| LR trop faible   | Apprentissage très lent           |
| Batch trop petit | Bruit élevé                       |
| Batch trop grand | Mauvaise généralisation / mémoire |

Warm-up :

Commencer avec un petit learning rate puis l'augmenter progressivement.

Très utile pour stabiliser les débuts d'entraînement.

techniq-debog-model-mach-learn.pdf

### XV. Régularisation

![How I Prevent Overfitting in ML Models Using EarlyStopping and Dropout | by Bhagya Rana | Medium](https://images.openai.com/static-rsc-4/lsgk1DMI1sBkdSpdVXX7Fnjk4oD1v7P33Ekh_G3X5iu5YNOZT-sIy1gEiJ0MOOreyWR6XZ0Tqd-sZCVHbeYBWmqFsgXb2Vp2z-0TsqJZOTsYiFef2wLysDNfHvdXIjyAolcMM9tNZv5CnSzsmr2vjrOLTSysdB_05J9QRkDVXVtP-YwJ53fzJ4Q1a4CzTCTl?purpose=fullsize)

| Trop forte                             | Trop faible                     |
| -------------------------------------- | ------------------------------- |
| Le modèle n'apprend plus(underfitting) | Le modèle mémorise(overfitting) |

Outils :

* Dropout

* Early stopping

* L1 / L2

⚠️ Le cours avertit :

Trop de régularisation peut masquer un vrai bug de données ou d'architecture.

techniq-debog-model-mach-learn.pdf

### XVI. Transfert learning

![#ai #machinelearning #deeplearning #transferlearning #nlp #computervision | Nourhane KEFSI](https://images.openai.com/static-rsc-4/i42hs30HYdAk-h83C4XJN360LmE41eT0T-MBNkPXVoIFccCY_OJstA_Q1F4XtMxhI0WBawkayE3axAoalYFag-jT4hntgGq2t7C45mdz-9BwkgOu0BHA0T-R41AcFvq2N1fpo3yeNAvi9AQfgqorY3T-ltK_mpxN6MkhALF19nGBFfAFY0QrwXkUnb7Q29oS?purpose=fullsize)

Problème majeur :

### Catastrophic forgetting

Le modèle oublie ses connaissances pré-entraînées en se spécialisant trop vite.

Diagnostic :

* suivre les performances sur la tâche cible et source,

* tester différents degrés de fine-tuning,

* geler progressivement les couches.

💡 Mnémo : "Too much fine-tuning = too much forgetting."

techniq-debog-model-mach-learn.pdf

### XVII. La check-list finale à apprendre

1. Vérifier les données

2. Vérifier le prétraitement

3. Vérifier le déséquilibre des classes

4. Vérifier le sous-/surapprentissage

5. Vérifier la convergence (loss, gradients)

6. Tester les hyperparamètres (un à la fois)

7. Simplifier / faire de l'ablation

8. Comparer avec une baseline stable

9. Tester chaque brique du pipeline séparément

10. Garantir la reproductibilité (seeds, versions, données)

Cette séquence résume pratiquement tout le cours.

techniq-debog-model-mach-learn.pdf

### Les 10 notions indispensables à connaître

| Notion                  | Définition simple                                                   |
| ----------------------- | ------------------------------------------------------------------- |
| Pipeline d'IA           | Chaîne complète de traitement des données jusqu'à l'inférence.      |
| Débogage stochastique   | Débogage d'un système dont les résultats varient selon l'aléatoire. |
| Ablation                | Retrait progressif de composants pour isoler une cause.             |
| Outlier                 | Valeur très éloignée de la tendance normale.                        |
| Data leakage            | Fuite de la cible ou d'informations futures dans les features.      |
| Underfitting            | Modèle trop simple.                                                 |
| Gradient vanishing      | Gradient quasi nul dans les couches profondes.                      |
| Gradient explosion      | Gradient énorme provoquant une divergence.                          |
| Neurone mort            | Neurone qui retourne toujours la même valeur.                       |
| Catastrophic forgetting | Perte des connaissances pré-entraînées lors du fine-tuning.         |

techniq-debog-model-mach-learn.pdf

### La phrase d'examen à retenir

« Déboguer un modèle d'IA consiste à isoler méthodiquement la cause racine en contrôlant chaque maillon du pipeline — données, prétraitement, modèle, hyperparamètres et environnement — dans un cadre strictement reproductible. »

Si tu sais expliquer cette phrase, puis définir ablation, data leakage, gradient vanishing et catastrophic forgetting, tu maîtrises déjà l'essentiel du cours.

techniq-debog-model-mach-learn.pdf
