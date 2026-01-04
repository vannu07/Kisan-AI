# Vercel Deployment Guide for Kisan-AI

## 🔧 Fixed Issues

The 500 INTERNAL_SERVER_ERROR has been resolved by:

1. **Created proper Vercel entry point** (`api/index.py`)
   - Exports Flask app correctly for serverless deployment
   - Proper path configuration for templates and static files

2. **Updated Vercel configuration** (`vercel.json`)
   - Changed build source from `app.py` to `api/index.py`
   - Added Python version specification

3. **Implemented lazy loading** (`api/routes.py`)
   - Pipelines and database clients now initialize on-demand
   - Prevents crashes during cold starts
   - Reduces memory footprint

## 🚀 Deployment Steps

### 1. Configure Environment Variables in Vercel

Go to your Vercel project settings and add these environment variables:

#### Required:
- `GEMINI_API_KEY` - Your Google Gemini API key for AI features
- `MONGODB_URL` - Your MongoDB Atlas connection string (or leave empty to use local JSON storage)

#### Optional (if using Auth0):
- `AUTH0_DOMAIN` - Your Auth0 domain
- `AUTH0_CLIENT_ID` - Your Auth0 client ID
- `AUTH0_CLIENT_SECRET` - Your Auth0 client secret
- `FLASK_SECRET_KEY` - A secure random string for Flask sessions

### 2. Set Environment Variables via Vercel CLI

```bash
vercel env add GEMINI_API_KEY
vercel env add MONGODB_URL
```

Or via Vercel Dashboard:
1. Go to your project settings
2. Navigate to "Environment Variables"
3. Add each variable for Production, Preview, and Development environments

### 3. Deploy to Vercel

```bash
# Install Vercel CLI if not already installed
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel --prod
```

## 📝 Important Notes

### File System Limitations
Vercel serverless functions have **read-only file system** except for `/tmp` directory:
- Uploaded files are saved to `/tmp` (cleared after function execution)
- Use cloud storage (AWS S3, Cloudinary, etc.) for persistent file storage
- Local JSON database falls back automatically if MongoDB is not configured

### Cold Starts
- First request after idle time may be slower (2-5 seconds)
- Lazy loading ensures components initialize only when needed
- Consider upgrading to Vercel Pro for reduced cold starts

### Function Limits (Hobby Plan)
- **Execution timeout**: 10 seconds
- **Memory**: 1024 MB
- **Deployment size**: 250 MB
- Consider Pro plan if you need higher limits

### MongoDB Connection
If MongoDB is not configured:
- App automatically falls back to local JSON storage (`local_db.json`)
- Warning logged: "MongoDB connection failed... Switching to local JSON storage"
- For production, MongoDB Atlas (free tier) is recommended

## 🧪 Testing Your Deployment

### Health Check
```bash
curl https://your-app.vercel.app/health
```

Expected response:
```json
{"status": "ok", "message": "KisanAI API is running"}
```

### Test API Endpoints
```bash
# Test signup
curl -X POST https://your-app.vercel.app/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123","name":"Test User"}'

# Test login
curl -X POST https://your-app.vercel.app/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

## 🔍 Debugging Tips

### Check Vercel Logs
```bash
vercel logs
```

Or view in Vercel Dashboard:
1. Go to your project
2. Click on "Deployments"
3. Select the deployment
4. View "Functions" logs

### Common Issues

#### "Module not found" errors
- Ensure all dependencies are in `requirements.txt`
- Run `vercel --prod` to redeploy

#### "Timeout" errors
- Check if operations complete within 10 seconds (Hobby plan)
- Consider async processing for heavy operations
- Upgrade to Pro for 60-second timeout

#### "File system" errors
- Ensure file writes go to `/tmp` directory
- Use cloud storage for persistent files

#### Environment variables not working
- Verify variables are set in Vercel Dashboard
- Redeploy after adding new variables
- Check variable names match `.env.example`

## 📦 Local Development

To run locally (not on Vercel):

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your actual values

# Run the app
python app.py
```

The app will run on http://localhost:5000

## 🔄 Redeployment

After making changes:

```bash
git add .
git commit -m "Your commit message"
git push origin main

# Vercel auto-deploys from GitHub
# Or manually deploy:
vercel --prod
```

## 📚 Additional Resources

- [Vercel Python Runtime](https://vercel.com/docs/runtimes#official-runtimes/python)
- [Vercel Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)
- [Vercel Limits](https://vercel.com/docs/concepts/limits/overview)
- [Flask on Vercel Guide](https://vercel.com/guides/using-flask-with-vercel)
