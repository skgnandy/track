# 🚀 Quick Start Guide

Get Track running in 3 minutes!

## Choose Your Version

### 🌐 Web UI (Beautiful Interface)

```bash
# 1. Install dependencies
pip3 install -r requirements_web.txt

# 2. Start server
python3 track_server.py

# 3. Open browser
# Go to: http://localhost:3000
```

**Done!** Click around and start tracking! 🎉

---

### 💻 CLI (Terminal Interface)

```bash
# 1. Install dependencies
pip3 install -r requirements.txt

# 2. Run program
python3 Track_improved.py

# 3. Choose option (1-4)
```

**Done!** Follow the prompts! ⚡

---

## Test It Out

Try these to verify everything works:

### Test IP Tracking
```
8.8.8.8
```
Should show Google DNS location

### Test Phone Number
```
+14155552671
```
Should show US number info

### Test Username
```
github
```
Should find GitHub's profiles

---

## Need Help?

- **Full Installation**: See [INSTALL.md](INSTALL.md)
- **Troubleshooting**: See [README.md](README.md#troubleshooting)
- **Documentation**: See [WEB_UI_GUIDE.md](WEB_UI_GUIDE.md) or [SETUP_GUIDE.md](SETUP_GUIDE.md)

---

## Common Issues

**"Module not found"**
```bash
pip3 install requests phonenumbers flask flask-cors
```

**"Permission denied"**
```bash
chmod +x Track_improved.py track_server.py
```

**"Port already in use"**
- Edit `track_server.py`, change `port=3000` to `port=8080`

---

**That's it! Happy tracking! 🔍✨**
