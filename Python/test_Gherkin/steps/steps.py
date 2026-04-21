from behave import given, then, when
from test_Gherkin.produit_stocke import Produit


@given('un produit "{nom_produit}" avec {stock:d} en stock')
def step_given_produit_en_stock(context, nom_produit, stock):
    context.produit = Produit(nom_produit, stock)


@when('l\'utilisateur essaie d\'acheter "{nom_produit}"')
def step_when_utilisateur_achete_produit(context, nom_produit):
    try:
        context.produit.retirer_produit(1)
        context.achat_reussi = True
        context.message = ""
    except ValueError as error:
        context.achat_reussi = False
        context.message = str(error)


@then('l\'achat est refusé')
def step_then_achat_refuse(context):
    assert not context.achat_reussi, "L'achat aurait dû être refusé"


@then('un message "{message}" est affiché')
def step_then_message_affiche(context, message):
    assert context.message == message, (
        f"Message attendu: {message}, mais obtenu: {context.message}"
    )
