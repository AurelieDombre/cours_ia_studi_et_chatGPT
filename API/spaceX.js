const request = new XMLHttpRequest()
// Intégrer l'url donner par postman pour récupérer les infos du caractère 12 de Games of thrones
request.open('GET', 'https://api.spacexdata.com/v3/launches/past');
// On lui demande l'entête avec du JSON
request.setRequestHeader('Content-type', 'application/json');

// Ici pas d'argument car il est dans l'url
request.send()

// Manipuler l'info dès lors que nous aurons une réponse
request.onload = function () {
    // transforme en JSON avec true pour récupérer un objet et pas un array
    response_from_spaceX = JSON.parse(request.responseText, true)[0]
    // console.log(response_from_spaceX["mission_name"])
        // On récupère l'élément pour ajouter la data
    response = document.getElementById('space_x')
    response.innerHTML = response_from_spaceX["mission_name"]
}