Feature: Gestion du stock
  Scenario: Tentative d'achat d'un produit en rupture de stock
    Given un produit "ProduitB" avec 0 en stock
    When l'utilisateur essaie d'acheter "ProduitB"
    Then l'achat est refusé
    And un message "Produit en rupture de stock" est affiché