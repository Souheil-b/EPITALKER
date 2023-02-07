import React, {useState} from 'react';
import '../CSS/home.css'
import { Link } from 'react-router-dom';

import { useHistory } from 'react-router-dom';

function Home() {    
    const [value, setValue] = useState('');


    const history = useHistory();
    const handleClick = () => {
        history.push('/api', { link: value });
      };
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

                        <Link to={
                            {
                                pathname: "/login",
                                state: { link: value }
                            }
                            }>
                            
                            <button
                                type="submit"
                                className="search-button"
                            >
                                Rechercher
                            </button>
                        </Link>
                        
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