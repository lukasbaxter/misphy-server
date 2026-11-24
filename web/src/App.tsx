import { useState } from 'react'
import './App.css'

function App() {

const [songs, setSongs] = useState([])


  return (
    <>
      <div>
        <h1 className='lukas-text'>awesome search!</h1>
      </div>
      <div>
        <input onChange={async(e) => {
          const response = await fetch(`http://localhost:8000/api/v1/search?query=${(e.currentTarget.value)}`)
          setSongs(await response.json())
          console.log(songs)
        }} type='text'/>
      </div>
      <div>
        {
          songs.map(song => <p key={song[5]}><a target='_blank' href={`http://localhost:8000/static/${song[5]}`} className='search-results'>{song[0]} - {song[3]}</a></p>)
        }
      </div>
    </>
  )
}

export default App


