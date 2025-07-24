# TaskFlow - Full Stack Task Management Application
<img width="1919" height="948" alt="image" src="https://github.com/user-attachments/assets/a6ecdf87-2efc-4496-bd57-0fe256afb3b2" />
<img width="936" height="714" alt="image" src="https://github.com/user-attachments/assets/88608907-e683-4cee-b57e-645d77190990" />

A complete full-stack task management application built with **Python Flask** backend and **React** frontend.

## 🚀 Features

### Backend (Python Flask)
- **RESTful API** with comprehensive endpoints
- **JWT Authentication** for secure access
- **SQLite Database** with SQLAlchemy ORM
- **User Management** (register, login, profile)
- **Task CRUD Operations** (Create, Read, Update, Delete)
- **Task Statistics** and analytics
- **Input Validation** and error handling
- **CORS Support** for frontend integration

### Frontend (React)
- **Modern React UI** with hooks
- **Responsive Design** with CSS Grid/Flexbox
- **User Authentication** flow
- **Real-time Task Management**
- **Priority-based Color Coding**
- **Due Date Tracking** with visual indicators
- **Statistics Dashboard**
- **Glassmorphism Design** with smooth animations

## 📁 Project Structure

```
taskflow/
├── main.py              # Flask backend application
├── requirements.txt     # Python dependencies
├── setup.py            # Setup and installation script
├── run.py              # Easy startup script (created by setup)
├── index.html          # React frontend
├── README.md           # This file
├── .env               # Environment variables (created by setup)
└── taskflow.db        # SQLite database (created automatically)
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+ 
- pip (Python package manager)
- Modern web browser

### Quick Start

1. **Clone or download all files to a folder**

2. **Run the setup script:**
   ```bash
   python setup.py
   ```
   This will:
   - Check Python version
   - Install required packages
   - Create configuration files
   - Create run script

3. **Start the application:**
   ```bash
   python run.py
   ```
   Choose option 3 for full application guidance.

### Manual Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the backend:**
   ```bash
   python main.py
   ```
   API will be available at `http://localhost:5000`

3. **Start the frontend (in another terminal):**
   ```bash
   python -m http.server 8000
   ```
   Frontend will be available at `http://localhost:8000`

4. **Open your browser and go to `http://localhost:8000`**

## 🔧 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `GET /api/auth/profile` - Get user profile

### Tasks
- `GET /api/tasks` - Get all tasks for user
- `POST /api/tasks` - Create new task
- `GET /api/tasks/<id>` - Get specific task
- `PUT /api/tasks/<id>` - Update task
- `DELETE /api/tasks/<id>` - Delete task
- `GET /api/tasks/stats` - Get task statistics

### Health Check
- `GET /api/health` - API health check

## 📝 API Usage Examples

### Register User
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com", 
    "password": "securepass123",
    "name": "John Doe"
  }'
```

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepass123"
  }'
```

### Create Task
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive README and API docs",
    "priority": "high",
    "due_date": "2025-07-30"
  }'
```

## 🎨 Frontend Features

### User Interface
- **Modern Design** with glassmorphism effects
- **Responsive Layout** that works on all devices
- **Smooth Animations** and hover effects
- **Priority Color Coding** (High=Red, Medium=Amber, Low=Green)
- **Due Date Indicators** with overdue highlighting

### User Experience
- **Intuitive Task Creation** with form validation
- **One-click Task Completion** toggle
- **Confirm Delete** dialogs for safety
- **Real-time Statistics** updates
- **Loading States** for better feedback
- **Error Handling** with user-friendly messages

## 🗄️ Database Schema

### Users Table
- `id` - Primary key
- `username` - Unique username
- `email` - Unique email address
- `name` - Full name
- `password_hash` - Hashed password
- `created_at` - Account creation timestamp

### Tasks Table
- `id`
