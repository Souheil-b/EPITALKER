import { useLocation } from 'react-router-dom';
import {useEffect, useState} from 'react';

function CallAppi() {

    const location = useLocation();
    const link  = location.state.link;
    const [response, setResponse] = useState('');
    useEffect(() => {
        let test = fetch('http://127.0.0.1:8000/login/?link=' + link)
        setResponse(test)
        console.log(response)
    }, [response]);
    return (
    <div>
        {response}
    </div>)

}
export default CallAppi;