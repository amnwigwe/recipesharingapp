import React, { useState } from 'react';
import axios from 'axios';

function RecipeForm({ onAdded }) {
    const [title,setTitle]=useState('');
    const [ingredients,setIngredients]=useState('');
    const [instructions,setInstructions]=useState('');
    const [tags,setTags]=useState('');
    const handleSubmit=async(e)=>{
        e.preventDefault();
        const token = localStorage.getItem('token');
        try{
            const res = await axios.post('http://localhost:8000/api/v1/recipes', {
                title, ingredients, instructions, tags: tags.split(',')
            }, { headers: { Authorization: 'Bearer '+token }});
            onAdded(res.data);
        }catch(err){ alert(err.response.data.message||'Error'); }
    };
    return (
        <form onSubmit={handleSubmit}>
            <input placeholder="Title" value={title} onChange={e=>setTitle(e.target.value)} required/>
            <textarea placeholder="Ingredients" value={ingredients} onChange={e=>setIngredients(e.target.value)} required/>
            <textarea placeholder="Instructions" value={instructions} onChange={e=>setInstructions(e.target.value)} required/>
            <input placeholder="Tags comma separated" value={tags} onChange={e=>setTags(e.target.value)}/>
            <button type="submit">Add Recipe</button>
        </form>
    );
}
export default RecipeForm;