import { useState } from 'react'
import '../../styling/index/index.css'
import NavigationBar from '../common/NavigationBar'

function Index() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <h1>HEllo Vite and React</h1>
        <NavigationBar />
      </div>
    </>
  )
}

export default Index;
