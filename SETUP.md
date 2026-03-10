# Canvas Study AI — GitHub Actions & Supabase Migration Guide

This guide explains how to set up the automated pipeline using GitHub Actions, Supabase, and OpenAI.

## 1. Supabase Setup (Persistent Tracking)
Since GitHub Actions resets its environment every run, we use Supabase to remember which files have already been processed.
1. Go to [Supabase](https://supabase.com/) and create a free project.
2. Go to **Table Editor** → **New Table**.
    - **Name:** `seen_files`
    - **Columns:**
        - `file_id` (Type: `text`, Primary Key, **Disable** "Is Identity")
3. SQL to create via **SQL Editor**:
```sql
CREATE TABLE seen_files (
  file_id TEXT PRIMARY KEY
);
```
4. Get your credentials from **Project Settings → API**:
    - `URL`: Your `SUPABASE_URL`.
    - `service_role key`: Your `SUPABASE_KEY` (Keep this secret!).

## 2. OpenAI Setup (Summarization)
1. Go to [OpenAI Platform](https://platform.openai.com/).
2. Create an API Key.
3. Add this to your secrets as `OPENAI_API_KEY`. The pipeline uses `gpt-4o` for high-quality PDF analysis.

## 3. GitHub Secrets Configuration
Instead of a `.env` file, add all your credentials to GitHub:
1. Go to your GitHub Repository → **Settings → Secrets and Variables → Actions**.
2. Click **New repository secret** for each of these:

| Secret Name | Description |
|-------------|-------------|
| `CANVAS_BASE_URL` | e.g., `https://canvas.nus.edu.sg` |
| `CANVAS_TOKEN` | Your Canvas Access Token |
| `OPENAI_API_KEY` | Your OpenAI API Key |
| `GDRIVE_FOLDER_ID` | The ID of your target Google Drive folder |
| `GDRIVE_CREDS_JSON` | The **entire contents** of your GDrive JSON key file |
| `TELEGRAM_BOT_TOKEN` | Your bot's token from @BotFather |
| `TELEGRAM_CHAT_ID` | Your personal Telegram Chat ID |
| `SUPABASE_URL` | Your Supabase project URL |
| `SUPABASE_KEY` | Your Supabase `service_role` key |

## 4. Verification & Testing
1. **Push your code**: Commit and push these changes to GitHub.
2. **First Run**: Go to the **Actions** tab in your repo, select **Daily Canvas Pipeline**, and click **Run workflow**.
3. **Daily Run**: The pipeline is scheduled to run automatically every day at **8:00 AM UTC**.

## 5. Local Development (Optional)
If you still want to run it locally, you can use the template in `backend/.env`, but ensure you've created the Supabase table first.
