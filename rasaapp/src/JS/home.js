import React, { useState } from 'react';
// import { Route } from 'react-router-dom'

function Home() {
    const [count, setCount] = useState(0);
    
    return (
        <div>
        <p>Count: {count}</p>
        <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
    );
}

export default Home;