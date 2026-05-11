import { useSelector } from 'react-redux';
import { setUserName } from './redux/nameSlice.js';
import { useDispatch } from 'react-redux';

// export default = on exporte ce composant
// pour pouvoir l'importer ailleurs
export default function UserName() {
  // useSelector permet de lire une valeur
  // dans le store Redux

  // state = le state global Redux
  // state.userName = le slice "userName"
  // .value = la propriété value du slice

  // Exemple du state :
  // {
  //   userName: {
  //      value: "John"
  //   }
  // }

  // Donc userName contiendra :
  // "John"

  const userName = useSelector((state) => state.userName.value);

  // useDispatch permet d'envoyer une action Redux
  // au store

  const dispatch = useDispatch();

  // Fonction appelée quand le formulaire est soumis
  const handleSubmit = (e) => {
    // Empêche le rechargement automatique
    // de la page lors du submit du formulaire
    e.preventDefault();

    // e.target = le formulaire
    // elements = tous les inputs du formulaire
    // userName = input qui possède :
    // name="userName"

    // .value = valeur tapée dans l'input

    console.log(e.target.elements.userName.value);

    // dispatch envoie une action Redux

    // setUserName(...) est une action creator
    // créée dans le slice Redux

    // Exemple :
    // dispatch(setUserName("Lucas"))

    // Redux va alors modifier le state global

    dispatch(setUserName(e.target.elements.userName.value));
  };

  // JSX retourné par le composant
  return (
    <div>
      {/* Affiche le username stocké dans Redux */}
      <span>{userName}</span>

      {/* Quand on soumet le formulaire,
               handleSubmit est exécuté */}
      <form onSubmit={handleSubmit}>
        {/* Champ texte */}
        <input type="text" name="userName" />

        {/* Bouton submit */}
        <button type="submit">Soumettre</button>
      </form>
    </div>
  );
}
