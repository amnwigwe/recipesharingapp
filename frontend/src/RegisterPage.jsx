import React, { useState } from 'react';
import axios from 'axios';

function RegisterPage() {
    const [username,setUsername] = useState('');
    const [email,setEmail] = useState('');
    const [password,setPassword] = useState('');
    const handleSubmit=async(e)=>{
        e.preventDefault();
        try{
            await axios.post('http://localhost:8000/auth/register',{username,email,password});
            alert('Registered! Login now.');
        }catch(err){
            alert(err.response.data.message||'Error');
        }
    };
    return (
        <form onSubmit={handleSubmit}>
            <input placeholder="Username" value={username} onChange={e=>setUsername(e.target.value)} required/>
            <input type="email" placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} required/>
            <input type="password" placeholder="Password" value={password} onChange={e=>setPassword(e.target.value)} required/>
            <button type="submit">Register</button>
        </form>
    );
}
export default RegisterPage;