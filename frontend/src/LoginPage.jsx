import React, { useState } from 'react';
import axios from 'axios';

function LoginPage({ onLogin }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:8000/auth/login', { email, password });
      onLogin(res.data.user); // directly store user object
      localStorage.setItem('user', JSON.stringify(res.data.user));
    } catch(err) {
      alert(err.response?.data?.message || 'Login failed');
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} required /><br/>
      <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} required /><br/>
      <button type="submit">Login</button>
    </form>
  )
}

export default LoginPage;
