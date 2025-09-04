import React, { useState } from 'react';
import axios from 'axios';

function RecipeForm({ onAdded, token }) {
  const [title, setTitle] = useState('');
  const [ingredients, setIngredients] = useState('');
  const [instructions, setInstructions] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    const newRecipe = { id: Date.now(), title, ingredients, instructions };
    try {
      if (token) {
        await axios.post('http://localhost:8000/recipes', newRecipe, {
          headers: { Authorization: `Bearer ${token}` }
        });
      }
      onAdded(newRecipe);
      setTitle(''); setIngredients(''); setInstructions('');
    } catch(err) {
      alert('Error adding recipe');
    }
  }

  return (
    <form onSubmit={handleSubmit} style={{marginBottom:'20px'}}>
      <input placeholder="Title" value={title} onChange={e=>setTitle(e.target.value)} required/><br/>
      <input placeholder="Ingredients" value={ingredients} onChange={e=>setIngredients(e.target.value)} required/><br/>
      <input placeholder="Instructions" value={instructions} onChange={e=>setInstructions(e.target.value)} required/><br/>
      <button type="submit">Add Recipe</button>
    </form>
  )
}

export default RecipeForm;
