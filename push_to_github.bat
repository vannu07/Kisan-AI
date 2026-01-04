@echo off
echo Initializing Git...
git init

echo Adding Remote...
git remote add origin https://github.com/vannu07/Kisan-AI.git

echo Committing Config Files...
git add .gitignore requirements.txt README.md vercel.json
git commit -m "initial config"

echo Committing Backend Code...
git add app.py src/ api/ notebooks/
git commit -m "backend logic"

echo Committing Frontend Files...
git add frontend/
git commit -m "frontend ui"

echo Pushing to GitHub...
git push -u origin main

echo Done!
pause