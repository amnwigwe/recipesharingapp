import React, { useState } from 'react';
import axios from 'axios';

function LoginPage({ onLogin }) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await axios.post('http://localhost:8000/auth/login', { email, password });
            localStorage.setItem('token', res.data.token);
            onLogin(res.data.token);
        } catch (err) {
            alert(err.response.data.message || 'Error');
        }
    };
    return (
        <form onSubmit={handleSubmit}>
            <input type="email" placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} required />
            <input type="password" placeholder="Password" value={password} onChange={e=>setPassword(e.target.value)} required />
            <button type="submit">Login</button>
        </form>
    );
}
export default LoginPage;