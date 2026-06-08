# Katie Strategy Signal Bot (Production-Grade Architecture)

Production implementation tracking the execution of Katie's mathematical indicator intersections. This repository is configured to operate seamlessly via infinite loop local daemons or inside completely serverless execution frameworks such as **Vercel Serverless Functions**.

## 📊 Technical Indicators Embedded
- **SMA 4** (Green) - Cross Engine Fast Matrix
- **EMA 50** (Red) - Cross Engine Confirmation Threshold
- **EMA 200** (White) - Baseline Structural Long-Term Market Trend Line Filter
- **Stochastic Oscillator (5, 1, 1)** - Core Directional Momentum Guard

## 🛑 Logic Enhancements for Loss Prevention
Unlike traditional basic scripts that generate false tracking alerts on cross-noises:
1. **Pre-Signals (Setup Statuses):** Dispatched immediately to your Telegram endpoint when lines start converging inside validated long-term trends (`EMA 200`). This gives the user warning to open their brokerage windows early.
2. **True Momentum Cross Guards:** The bot completely discards crosses if momentum configurations fall flat or fail to clear boundary metrics (e.g. Stochastic rules).

## 💻 Local Setup
Run via specific shell orchestrators provided directly in the root directory:
- **Windows Command Prompt:** Double-click or run `start.bat`
- **Windows PowerShell Engine:** Execute `./start.ps1`

## ☁️ Serverless Deployment on Vercel
1. Install Vercel CLI toolchain globally: `npm install -g vercel`
2. Authenticate session instance: `vercel login`
3. Launch direct pipeline deployment command inside this folder root: `vercel`
4. Set Environmental Variables inside Vercel Dashboard Settings: `TELEGRAM_TOKEN`, `TELEGRAM_CHAT_ID`, `BOT_MODE`.
5. Automate regular calls via **Vercel Cron Jobs** pointing to the built path route `/api/cron`.
