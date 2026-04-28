const request = new XMLHttpRequest()
// Intégrer l'url donner par postman pour récupérer les infos du caractère 12 de Games of thrones
request.open('GET', 'https://www.anapioficeandfire.com/api/characters/12');
// On lui demande l'entête avec du JSON
request.setRequestHeader('Content-type', 'application/json');

// Ici pas d'argument car il est dans l'url
request.send()

// Manipuler l'info dès lors que nous aurons une réponse
request.onload = function () {
    // transforme en JSON avec true pour récupérer un objet et pas un array
    response_from_postman = JSON.parse(request.responseText, true)
        // On récupère l'élément pour ajouter la data
    response = document.getElementById('response')
    response.innerHTML = response_from_postman.name
}