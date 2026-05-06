const express = require('express')
const jwt = require('jsonwebtoken')
const { expressjwt: e_jwt } = require('express-jwt')

const app = express()
const port = 3004

const SECRET = 'monapplication'

// Lire le JSON
app.use(express.json())

// Fake base de données
const users = [
    {
        username: 'John Doe',
        email: 'john@doe.com',
        password: 'johndoe',
        role: 'user'
    },
    {
        username: 'Jane Done',
        email: 'jane@done.com',
        password: 'janedone',
        role: 'admin'
    },
]

// 🔐 Middleware de protection
app.use(
    e_jwt({
        secret: SECRET,
        algorithms: ['HS256']
    }).unless({ path: ['/login'] })
)

// Gestion erreurs JWT
app.use((err, req, res, next) => {
    if (err.name === 'UnauthorizedError') {
        return res.status(401).json({
            message: 'Token invalide ou manquant'
        })
    }
    next()
})

// 🔑 LOGIN
app.post('/login', (req, res) => {

    const { email, password } = req.body

    // Vérifier utilisateur
    const user = users.find(
        u => u.email === email && u.password === password
    )

    if (!user) {
        return res.status(401).json({
            message: 'Identifiants invalides'
        })
    }

    // Créer le token
    const token = jwt.sign(
        {
            username: user.username,
            role: user.role
        },
        SECRET,
        { expiresIn: '3h' }
    )

    res.json({ access_token: token })
})

// Route protégée
app.get('/protected', (req, res) => {
    res.json({
        message: 'Accès autorisé',
        user: req.auth
    })
})

// Lancer serveur
app.listen(port, () => {
    console.log(`Serveur démarré sur http://localhost:${port}`)
})