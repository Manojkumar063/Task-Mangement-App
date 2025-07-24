# setup.py - Setup and initialization script
import os
import subprocess
import sys

def check_python_version():
    """Check if Python version is 3.7 or higher"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages!")
        return False

def create_env_file():
    """Create .env file with default configuration"""
    env_content = """# Flask Configuration
FLASK_APP=main.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-change-in-production
JWT_SECRET_KEY=jwt-secret-string-change-in-production

# Database Configuration
DATABASE_URL=sqlite:///taskflow.db

# CORS Configuration
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000,http://localhost:8000,http://127.0.0.1:8000
"""
    
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ .env file created!")
    else:
        print("⚠️  .env file already exists, skipping...")

def create_run_script():
    """Create run script for easy startup"""
    run_script_content = """#!/usr/bin/env python3
# run.py - Easy startup script
import os
import subprocess
import sys
import webbrowser
import time
from threading import Timer

def open_browser():
    """Open browser after a delay"""
    webbrowser.open('http://localhost:8000')
    print("🌐 Opening browser at http://localhost:8000")

def start_frontend_server():
    """Start a simple HTTP server for the frontend"""
    print("🚀 Starting frontend server on http://localhost:8000")
    try:
        # Python 3
        subprocess.run([sys.executable, "-m", "http.server", "8000"])
    except KeyboardInterrupt:
        print("\\n👋 Frontend server stopped!")

def main():
    print("🚀 TaskFlow - Full Stack Application")
    print("=" * 50)
    
    choice = input("""
Choose what to run:
1. Backend API only (http://localhost:5000)
2. Frontend only (http://localhost:8000)  
3. Full application (Backend + Frontend)

Enter choice (1-3): """).strip()
    
    if choice == "1":
        print("\\n🔧 Starting Backend API...")
        os.system("python main.py")
        
    elif choice == "2":
        print("\\n🎨 Starting Frontend...")
        Timer(2, open_browser).start()
        start_frontend_server()
        
    elif choice == "3":
        print("\\n🚀 Starting Full Application...")
        print("Note: You'll need to run backend and frontend in separate terminals")
        print("\\nTerminal 1: python main.py")
        print("Terminal 2: python -m http.server 8000")
        print("\\nOr use: python run.py")
        
        # For demo, start backend
        os.system("python main.py")
    else:
        print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
"""
    
    with open('run.py', 'w') as f:
        f.write(run_script_content)
    
    print("✅ run.py script created!")

def main():
    """Main setup function"""
    print("🚀 TaskFlow Setup Script")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Create configuration files
    create_env_file()
    create_run_script()
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Run the backend: python main.py")
    print("2. In another terminal, serve frontend: python -m http.server 8000")
    print("3. Open http://localhost:8000 in your browser")
    print("\nOr use the run script: python run.py")
    print("\n🎯 API will be available at: http://localhost:5000/api")
    print("🌐 Frontend will be available at: http://localhost:8000")

if __name__ == "__main__":
    main()
