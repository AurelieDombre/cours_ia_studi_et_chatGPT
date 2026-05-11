
import './App.css'
import Counter from './Counter.jsx'
import { useSelector, useDispatch } from 'react-redux'
import { useEffect } from 'react'

import { randomColor } from './redux/colorSlice.js'


function App() {

  const color = useSelector((state) => state.color.value)

  useEffect(() => {
    document.body.style.backgroundColor = color
  }, [color])
  const dispatch = useDispatch()


  return (
    <>
    <button onClick={()=> { dispatch(randomColor()) }}>Change Background Color</button>
    <Counter />
    </>
    
  )
}

export default App