# Deployment Guide — JT/CALL

Get your app live on GitHub + Vercel in 5 minutes.

## Step 1: Push to GitHub

```bash
# Initialize git (if not done)
cd jt-call
git config user.name "Your Name"
git config user.email "your@email.com"

# Add files
git add .
git commit -m "Initial commit: JT/CALL app"

# Create repo on GitHub.com first, then:
git remote add origin https://github.com/yourusername/jt-call.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy to Vercel

Vercel is free serverless hosting. It handles the `/api/generate` function automatically.

### Option A: Quick Deploy (Recommended)
1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Click "New Project"
4. Select your `jt-call` repo
5. Click "Deploy"
6. Done! Your app is live at `https://jt-call-yourusername.vercel.app`

### Option B: CLI Deploy
```bash
npm i -g vercel
vercel
# Follow prompts, answer "yes" to all defaults
```

## What Happens

- **GitHub** hosts your static HTML/CSS/JS
- **Vercel** runs your Python logic as serverless functions
- Users visit your app, paste their Anthropic API key, and it works

Your app is now **publicly accessible** from any device:
- Desktop: `https://jt-call-yourusername.vercel.app`
- iPhone: Same URL, works in Safari
- iPad: Same URL, responsive design

## Custom Domain (Optional)

Once deployed on Vercel:
1. Go to Vercel project settings
2. Click "Domains"
3. Add custom domain (e.g., `jt-call.au`)
4. Follow DNS setup

Then your URL becomes `https://jt-call.au` — looks way more professional.

## Making Changes

Push to GitHub → Vercel auto-deploys within ~60 seconds.

```bash
# Edit files locally
# Commit & push
git add .
git commit -m "Update flowchart logic"
git push origin main

# Check Vercel dashboard for deployment status
```

## Troubleshooting

**App deployed but `/api/generate` fails?**
- Make sure `api/generate.js` exists
- Check Vercel Function logs in dashboard
- Verify Anthropic API key is correct in the app

**Stuck? DM Sev or check:**
- Vercel docs: vercel.com/docs
- GitHub docs: github.com/git-tips

## Cost

- **GitHub**: Free ✓
- **Vercel**: Free tier includes 100GB bandwidth/month (more than enough)
- **Anthropic API**: Only pay for calls (~$0.03 each)

**Total monthly cost for you: $0** (unless you get 100M+ requests/month, which would be insane)

