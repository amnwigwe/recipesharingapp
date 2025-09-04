import React, { useState } from 'react';
import LoginPage from './LoginPage.jsx';
import RegisterPage from './RegisterPage.jsx';
import RecipeList from './RecipeList.jsx';
import RecipeForm from './RecipeForm.jsx';

function App() {
    const [token,setToken] = useState(localStorage.getItem('token'));
    const handleLogin = (tok)=>setToken(tok);
    return (
        <div>
            {!token ? <LoginPage onLogin={handleLogin}/> : 
            <>
                <h2>Recipes</h2>
                <RecipeForm onAdded={()=>{}}/>
                <RecipeList/>
            </>}
        </div>
    );
}
export default App;