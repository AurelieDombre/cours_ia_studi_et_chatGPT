import { useSelector } from 'react-redux';
import { increment, decrement } from './redux/counterSlice.js';
import { useDispatch } from 'react-redux';

export default function Counter() {
  const count = useSelector((state) => state.counter.value);
  const dispatch = useDispatch();

  return (
    <div>
      <span>Valeur du compteur : {count}</span>
      <button onClick={() => dispatch(increment())}>
        Incrementer le compteur
      </button>
      <button onClick={() => dispatch(decrement())}>
        Decrementer le compteur
      </button>
    </div>
  );
}
