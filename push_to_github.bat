@echo off
set GIT_PATH="C:\Program Files\Git\cmd\git.exe"

echo Initializing Git...
%GIT_PATH% init

echo Adding Remote...
%GIT_PATH% remote add origin https://github.com/vannu07/Kisan-AI.git

echo Committing Config Files...
%GIT_PATH% add .gitignore requirements.txt README.md vercel.json
%GIT_PATH% commit -m "initial config"

echo Committing Backend Code...
%GIT_PATH% add app.py src/ api/ notebooks/
%GIT_PATH% commit -m "backend logic"

echo Committing Frontend Files...
%GIT_PATH% add frontend/
%GIT_PATH% commit -m "frontend ui"

echo Pushing to GitHub...
%GIT_PATH% push -u origin main

echo Done!
pause