import React, { useState, useEffect } from 'react';
import axios from 'axios';
import LoginPage from './LoginPage.jsx';
import RegisterPage from './RegisterPage.jsx';
import RecipeList from './RecipeList.jsx';
import RecipeForm from './RecipeForm.jsx';
import Profile from './Profile.jsx';

function App() {
  const [user, setUser] = useState(JSON.parse(localStorage.getItem('user')) || null);
  const [showRegister, setShowRegister] = useState(false);
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/recipes')
      .then(res => setRecipes(res.data))
      .catch(() => {
        setRecipes([
          { id: 1, title: 'Sample Pasta', ingredients: 'Pasta, sauce', instructions: 'Boil pasta, add sauce' },
          { id: 2, title: 'Sample Soup', ingredients: 'Tomatoes, onion', instructions: 'Cook and blend' }
        ])
      });
  }, []);

  const handleLogout = () => {
    setUser(null);
    localStorage.removeItem('user');
  }

  const handleAddRecipe = recipe => setRecipes([recipe, ...recipes]);

  return (
    <div>
      {!user ? (
        showRegister ? (
          <>
            <h2>Register</h2>
            <RegisterPage onRegister={setUser} />
            <p>Already have an account? <button onClick={() => setShowRegister(false)}>Login</button></p>
          </>
        ) : (
          <>
            <h2>Login</h2>
            <LoginPage onLogin={setUser} />
            <p>Don’t have an account? <button onClick={() => setShowRegister(true)}>Register</button></p>
          </>
        )
      ) : (
        <>
          <button onClick={handleLogout}>Logout</button>
          <h2>Profile</h2>
          <Profile userId={user.id} />
          <h2>Recipes</h2>
          <RecipeForm onAdded={handleAddRecipe} />
          <RecipeList recipes={recipes} />
        </>
      )}
    </div>
  )
}

export default App;
