const express = require('express')
const app = express()
const port = 3003
const basicAuth = require('express-basic-auth')

// Permet de lire automatiquement le JSON envoye dans les requetes.
app.use(express.json())

// Middleware de protection par identifiant / mot de passe.
// On l'applique seulement sur les routes que l'on veut securiser.
const authMiddleware = basicAuth({
    users: {
        'aurelie': 'Motdepasse'
    },
    challenge: true, // Force la demande d'authentification Basic Auth avec un formulaire
    unauthorizedResponse: () => ({
        message: 'Authentification requise'
    })
})

// Tableau temporaire en memoire.
// Dans un vrai projet, ces donnees viendraient plutot d'une base de donnees.
const books = [
    {
        titre: 'Livre 1',
        auteur: 'Jonathan',
        isbn: '12345679',
        disponibilite: true,
        date_retour: null
    },
    {
        titre: 'Livre 2',
        auteur: 'Elise',
        isbn: '98765428',
        disponibilite: false,
        date_retour: '01/01/2028'
    },
    {
        titre: 'Livre 3',
        auteur: 'Zineb',
        isbn: '87357493',
        disponibilite: false,
        date_retour: null
    }
]

// Route publique utile pour verifier rapidement que l'API fonctionne.
app.get('/', (req, res) => {
    res.json({
        message: 'API active',
        routes: ['/book', '/books', '/book/:isbn', '/books/:isbn']
    })
})

// GET /books ou /book : renvoie tous les livres.
app.get(['/books', '/books/', '/book'], authMiddleware, (req, res) => {
    res.json(books)
})

// GET /books/:isbn : renvoie un seul livre selon son ISBN.
app.get(['/books/:isbn', '/book/:isbn'], authMiddleware, (req, res) => {
    // req.params contient les parametres presents dans l'URL.
    const isbn = req.params.isbn

    // On cherche le livre qui possede cet ISBN.
    const book = books.find(book => book.isbn === isbn)

    if (!book) {
        // 404 = la ressource demandee n'existe pas.
        return res.status(404).json({ message: 'Livre introuvable' })
    }

    res.json(book)
})

// POST /books : ajoute un nouveau livre dans le tableau.
app.post('/books', authMiddleware, (req, res) => {
    // req.body contient les donnees envoyees par le client.
    books.push(req.body)
    res.status(200).json(books)
})

// PUT /books/:isbn : modifie un livre existant.
app.put('/books/:isbn', authMiddleware, (req, res) => {
    const isbn = req.params.isbn
    const book = books.find(book => book.isbn === isbn)

    if (!book) {
        return res.status(404).json({ message: 'Livre introuvable' })
    }

    // On remplace les anciennes valeurs par celles recues dans la requete.
    book.titre = req.body.titre
    book.auteur = req.body.auteur
    book.disponibilite = req.body.disponibilite
    book.date_retour = req.body.date_retour

    res.status(200).json(book)
})

// DELETE /books/:isbn : supprime un livre.
app.delete('/books/:isbn', authMiddleware, (req, res) => {
    const isbn = req.params.isbn
    const book = books.find(book => book.isbn === isbn)

    if (!book) {
        return res.status(404).json({ message: 'Livre introuvable' })
    }

    // indexOf retrouve la position du livre dans le tableau,
    // puis splice le supprime.
    books.splice(books.indexOf(book), 1)

    res.json(books)
})

// Demarre le serveur HTTP sur le port defini plus haut.
app.listen(port, () => {
    console.log(`Serveur demarre sur http://localhost:${port}`)
})
