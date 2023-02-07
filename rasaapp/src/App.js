import Home from './JS/home';
import CallApi from './JS/api';
import { Switch, Route, Router, BrowserRouter } from "react-router-dom";

function App() {
  return (
    <div>
      <BrowserRouter>
        <Switch>
          <Route path="/login" component={CallApi} />
        </Switch>
        <Route path="/" exact>
          <Home />
        </Route>
      </BrowserRouter>

    </div>
  );
}

export default App;
