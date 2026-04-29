const express = require('express')
const app = express()
const port = 3001
const basicAuth = require('express-basic-auth')

app.use(express.json())


// Middleware de protection par identifiant / mot de passe.
// On l'applique seulement sur les routes que l'on veut securiser.
const authMiddleware = basicAuth({
    users: {
        'aurelie': 'password'
    },
    challenge: true, // Force la demande d'authentification Basic Auth avec un formulaire
    unauthorizedResponse: () => ({
        message: 'Authentification requise'
    })
})

// Une liste d'utilisateur, qui pourrait être récupérée en base de données
const utilisateurs = [
    {
        "nom": "Livre",
        "prenom": "Jonathan",
        "livres": ["12345679" ],

    },
    {
        "nom": "Livy",
        "prenom": "Elise",
        "livres": ["98765428" ],
        "isbn": "",
    },
    {
        "nom": "Dupont",
        "prenom": "Zineb",
        "livres": [],
    },
]

// Route publique utile pour verifier rapidement que l'API fonctionne.
app.get('/', (req, res) => {
    res.json({
        message: 'API active',
        routes: ['/utilisateur', '/utilisateurs']
    })
})

app.get(['/utilisateurs/', '/utilisateur/:nom'], authMiddleware, (req, res) => {
    const nom = req.params.nom
    const utilisateur = utilisateurs.find(utilisateur => utilisateur.nom === nom)

    res.json(utilisateur)
})

app.post('/utilisateurs', authMiddleware, (req, res) => {
    utilisateurs.push(req.body)
    res.status(200).json(utilisateurs)
})

app.put('/utilisateurs/:nom',  authMiddleware,(req,res) => {
    const nom = req.params.nom
    let utilisateur = utilisateurs.find(utilisateur => utilisateur.nom === nom)

    // Modification du livre
    utilisateur.nom = req.body.nom
    utilisateur.prenom = req.body.prenom

    res.status(200).json(utilisateur)
})


app.delete('/utilisateurs/:isbn',  authMiddleware,(req, res) => {
    const isbn = req.params.isbn
    const utilisateur = utilisateurs.find(utilisateur => utilisateur.isbn === isbn)
    utilisateurs.splice(utilisateurs.indexOf(utilisateur), 1)

    res.json(utilisateurs)
})


app.listen(port, () => {
  console.log('Serveur démarré')
})
