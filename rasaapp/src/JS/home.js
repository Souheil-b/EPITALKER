import React, { useState } from 'react';
// import { Route } from 'react-router-dom'
// import { MDBCol, MDBFormInline, MDBBtn } from "mdbreact";
import '../CSS/home.css'

function Home() {
    const [value, setValue] = useState('');
    return (
        <>
            <div className="scrolling-text">
                <h1>EPITALKER</h1>
            </div>
                <div className="container">
                    <form className="search-form">
                        <input className="search-bar" type="text" placeholder="AutoLogin Link..." 
                        value={value}
                        onChange={(event) => setValue(event.target.value)}
                        />
                        <button
                            type="submit"
                            className="search-button"
                            onClick={() => alert(value)}
                        >
                            Rechercher
                        </button>
                    </form>
                </div>
        </>
    );
}


// const SearchPage = () => {
//   return (

//   );
// }


export default Home;