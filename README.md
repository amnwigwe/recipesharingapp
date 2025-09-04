# 🍳 Recipe App

A full-stack recipe management application with **user authentication**, **CRUD recipes**, **favorites**, **search/filtering**, and a modern **React frontend**. Fully containerized with **Docker** for easy setup.

## 🖥 Features

- User authentication with **JWT**  
- Create, read, update, delete **recipes**  
- **Favorites**: save your favorite recipes  
- **Search and filter** recipes by keyword or tags  
- Responsive **React frontend** with Vite  
- **MySQL database** (can connect via MySQL Workbench)  
- Fully containerized with **Docker + Docker Compose**  
- Ready for deployment with **CI/CD**  

## 📦 Tech Stack

| Layer        | Technology        |
|-------------|-----------------|
| Frontend     | React + Vite      |
| Backend      | Flask + JWT       |
| Database     | MySQL             |
| Auth         | JSON Web Tokens   |
| Deployment   | Docker + Docker Compose |
| API Requests | Axios             |

## ⚙️ Getting Started

### Clone the repository

```bash
git clone <your-github-repo-url>
cd recipe-app-full
```

### Run Backend + Database (Docker)

```bash
docker compose up --build
```

- Backend API: `http://localhost:8000`  
- PostgreSQL database exposed on port `5432`  

### Run Frontend

```bash
cd frontend
npm install
npm run dev
```

- Frontend: `http://localhost:5173`  

## 🔑 User Authentication

- Register: `POST /auth/register`  
  - Body: `{ "username": "user", "email": "user@example.com", "password": "password" }`  
- Login: `POST /auth/login`  
  - Returns JWT token  
- Get current user: `GET /auth/me` (requires `Authorization: Bearer <token>`)

## 📖 Recipe API Endpoints

- `GET /api/v1/recipes` → List all recipes (optional query: `search`, `tag`)  
- `POST /api/v1/recipes` → Create a recipe (auth required)  
- `GET /api/v1/recipes/<id>` → Get single recipe  
- `PUT /api/v1/recipes/<id>` → Update recipe (auth & owner required)  
- `DELETE /api/v1/recipes/<id>` → Delete recipe (auth & owner required)  

### Favorites Endpoints

- `POST /api/v1/favorites/<recipe_id>` → Toggle favorite  
- `GET /api/v1/favorites` → List user's favorite recipes  

## 🗂 Project Structure

```
recipe-app-full/
├─ backend/          # Flask API
│  ├─ app/
│  │  ├─ models/     # DB models
│  │  ├─ routes/     # API routes
│  │  └─ main.py     # App entrypoint
│  └─ requirements.txt
├─ frontend/         # React frontend
│  ├─ src/
│  ├─ package.json
│  └─ vite.config.js
├─ docker-compose.yml
└─ README.md
```

## 💡 Usage

1. Start backend + DB with Docker  
2. Start frontend with `npm run dev`  
3. Register a new user  
4. Login to receive JWT token  
5. Create, edit, delete recipes  
6. Favorite recipes for easy access  
7. Search or filter recipes by keyword or tag  

## 📄 Documentation

- Database schema:  
  - **Users**: `id`, `username`, `email`, `password_hash`  
  - **Recipes**: `id`, `title`, `ingredients`, `instructions`, `tags`, `created_by`  
  - **Favorites**: `user_id`, `recipe_id`  
- **Uses MySQL**  
- Axios handles frontend API requests

## 🚀 Next Steps

- Add image upload to Cloudinary or S3  
- Add comments or reviews on recipes  
- Implement meal planning / shopping list  
- Improve UI/UX with styling libraries (Chakra UI / Tailwind CSS)  

## 📝 Contributing

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Make your changes  
4. Commit and push (`git push origin feature-name`)  
5. Create a pull request
