import React, { useEffect, useState } from "react";
import axios from "axios";

const Profile = ({ userId }) => {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/auth/profile/${userId}`);
        setProfile(response.data.user);
      } catch (err) {
        setError("Failed to load profile.");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    if (userId) fetchProfile();
  }, [userId]);

  if (loading) return <p>Loading profile...</p>;
  if (error) return <p>{error}</p>;
  if (!profile) return <p>No profile found.</p>;

  return (
    <div>
      <h2>User Profile</h2>
      <p><strong>ID:</strong> {profile.id}</p>
      <p><strong>Username:</strong> {profile.username}</p>
      <p><strong>Email:</strong> {profile.email}</p>
    </div>
  );
};

export default Profile;
