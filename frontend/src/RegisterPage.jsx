import React, { useState } from 'react';
import axios from 'axios';

function RegisterPage({ onRegister }) {
  const [username,setUsername] = useState('');
  const [email,setEmail] = useState('');
  const [password,setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Register user
      await axios.post('http://localhost:8000/auth/register', { username, email, password });

      // Log in immediately after registering
      const res = await axios.post('http://localhost:8000/auth/login', { email, password });

      // Store user and notify parent
      onRegister(res.data.user);
      localStorage.setItem('user', JSON.stringify(res.data.user));
    } catch(err) {
      alert(err.response?.data?.message || 'Error');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Username" value={username} onChange={e=>setUsername(e.target.value)} required />
      <input type="email" placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} required />
      <input type="password" placeholder="Password" value={password} onChange={e=>setPassword(e.target.value)} required />
      <button type="submit">Register</button>
    </form>
  );
}

export default RegisterPage;
