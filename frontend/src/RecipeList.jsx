import React, { useState, useEffect } from 'react';
import axios from 'axios';

function RecipeList() {
    const [recipes,setRecipes] = useState([]);
    const [search,setSearch] = useState('');
    const [tag,setTag] = useState('');
    useEffect(()=>{
        const fetchData = async()=>{
            const res = await axios.get('http://localhost:8000/api/v1/recipes', { params: {search, tag} });
            setRecipes(res.data);
        };
        fetchData();
    }, [search, tag]);
    return (
        <div>
            <input placeholder="Search" value={search} onChange={e=>setSearch(e.target.value)} />
            <input placeholder="Tag" value={tag} onChange={e=>setTag(e.target.value)} />
            <ul>{recipes.map(r=><li key={r.id}>{r.title}</li>)}</ul>
        </div>
    );
}
export default RecipeList;