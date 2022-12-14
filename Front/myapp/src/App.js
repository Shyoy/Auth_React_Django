import { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';


function App() {
  const MY_SERVER = "http://127.0.0.1:8000/products/" 

  const [products,setProducts] = useState([])

  const allProducts = async()=>{
    const response = await axios.get(MY_SERVER)
    // console.table(response.data)
    setProducts(response.data)
    
  }

  
  useEffect(()=>{
    allProducts()
    // .then(e => console.table(products))
  },[])


  return (
    <div className="App">
      {products.map((product,i) => 
        <li key={i} >
          <h1>{product.desc}</h1>
          <p>{product.price}</p>
        </li>)}
    </div>
  );
}

export default App;
