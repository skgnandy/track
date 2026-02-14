# Installation Guide

Complete installation instructions for Track on all platforms.

## 📋 Table of Contents

- [System Requirements](#system-requirements)
- [Windows Installation](#windows-installation)
- [macOS Installation](#macos-installation)
- [Linux Installation](#linux-installation)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

---

## System Requirements

### Minimum Requirements
- **Python**: 3.6 or higher
- **RAM**: 256 MB
- **Disk Space**: 50 MB
- **Internet**: Active connection required

### Recommended Requirements
- **Python**: 3.8 or higher
- **RAM**: 512 MB
- **Disk Space**: 100 MB
- **Browser**: Chrome, Firefox, Safari, or Edge (latest version)

---

## Windows Installation

### Step 1: Install Python

1. **Download Python**
   - Visit [python.org/downloads](https://www.python.org/downloads/)
   - Download Python 3.8+ for Windows
   - Choose "Windows installer (64-bit)" for most systems

2. **Install Python**
   - Run the downloaded installer
   - ✅ **IMPORTANT**: Check "Add Python to PATH"
   - Click "Install Now"
   - Wait for installation to complete

3. **Verify Installation**
   - Open Command Prompt (Win + R, type `cmd`)
   - Type: `python --version`
   - You should see: `Python 3.x.x`

### Step 2: Install Git (Optional)

1. **Download Git**
   - Visit [git-scm.com/download/win](https://git-scm.com/download/win)
   - Download and run installer
   - Use default settings

### Step 3: Download Track

**Option A: Using Git (Recommended)**
```cmd
git clone https://github.com/yourusername/Track.git
cd Track
```

**Option B: Download ZIP**
1. Go to [github.com/yourusername/Track](https://github.com/yourusername/Track)
2. Click "Code" → "Download ZIP"
3. Extract ZIP to desired location
4. Open Command Prompt in that folder

### Step 4: Install Dependencies

**For Web UI:**
```cmd
pip install -r requirements_web.txt
```

**For CLI:**
```cmd
pip install -r requirements.txt
```

### Step 5: Run Track

**Web UI:**
```cmd
python track_server.py
```
Then open: http://localhost:3000

**CLI:**
```cmd
python Track_improved.py
```

---

## macOS Installation

### Step 1: Install Python

**Method 1: Using Homebrew (Recommended)**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python3
```

**Method 2: Download from Python.org**
1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download macOS installer
3. Run installer and follow prompts

**Verify Installation:**
```bash
python3 --version
```

### Step 2: Download Track

**Using Git:**
```bash
git clone https://github.com/yourusername/Track.git
cd Track
```

**Or download ZIP from GitHub**

### Step 3: Install Dependencies

```bash
# For Web UI
pip3 install -r requirements_web.txt

# For CLI
pip3 install -r requirements.txt
```

### Step 4: Run Track

**Web UI:**
```bash
python3 track_server.py
```
Open browser to: http://localhost:3000

**CLI:**
```bash
python3 Track_improved.py
```

### Quick Setup (Automated)

Use the included setup script:
```bash
bash setup_mac.sh
```

---

## Linux Installation

### Ubuntu / Debian

**Step 1: Install Python and pip**
```bash
sudo apt update
sudo apt install python3 python3-pip git
```

**Step 2: Download Track**
```bash
git clone https://github.com/yourusername/Track.git
cd Track
```

**Step 3: Install Dependencies**
```bash
# For Web UI
pip3 install -r requirements_web.txt

# For CLI
pip3 install -r requirements.txt
```

**Step 4: Run Track**
```bash
# Web UI
python3 track_server.py

# CLI
python3 Track_improved.py
```

### Fedora / RHEL / CentOS

**Step 1: Install Python**
```bash
sudo dnf install python3 python3-pip git
```

**Step 2-4: Same as Ubuntu above**

### Arch Linux

**Step 1: Install Python**
```bash
sudo pacman -S python python-pip git
```

**Step 2-4: Same as Ubuntu above**

---

## Verification

### Test CLI Version

1. Run the program:
   ```bash
   python3 Track_improved.py
   ```

2. You should see the menu with 4 options

3. Try option 1 (IP Tracker) with: `8.8.8.8`

4. If you see results, installation is successful! ✅

### Test Web UI Version

1. Start server:
   ```bash
   python3 track_server.py
   ```

2. You should see:
   ```
   🔍 Track Web Server Starting...
   📡 Server running on: http://localhost:3000
   ```

3. Open browser to: http://localhost:3000

4. You should see the Track interface

5. Try the IP Tracker with: `8.8.8.8`

6. If you see results, installation is successful! ✅

---

## Troubleshooting

### Python Issues

**"python: command not found"**
- Windows: Use `python` instead of `python3`
- Mac/Linux: Install Python 3 or use `python3`

**"pip: command not found"**
```bash
# Install pip
python3 -m ensurepip --upgrade

# Or on Linux
sudo apt install python3-pip
```

**"Permission denied"**
```bash
# Use --user flag
pip3 install --user -r requirements.txt

# Or use sudo (not recommended)
sudo pip3 install -r requirements.txt
```

### Module Not Found Errors

**"ModuleNotFoundError: No module named 'requests'"**
```bash
pip3 install requests phonenumbers flask flask-cors
```

**Import errors after installation:**
```bash
# Make sure you're in the right directory
cd Track

# Reinstall dependencies
pip3 install --upgrade -r requirements_web.txt
```

### Network Issues

**"Failed to establish connection"**
- Check your internet connection
- Try a different network
- Check firewall settings

**"Read timed out"**
- Internet is slow
- API might be down
- Try again in a few minutes

### Web UI Issues

**"Address already in use"**
```bash
# Change port in track_server.py
# Change line: app.run(host='0.0.0.0', port=3000, debug=True)
# To: app.run(host='0.0.0.0', port=8080, debug=True)
```

**"Cannot connect to server"**
- Make sure server is running
- Check for error messages in terminal
- Try http://127.0.0.1:3000 instead

**Web page not loading:**
- Clear browser cache
- Try incognito/private mode
- Try a different browser
- Check browser console (F12) for errors

### Permission Issues

**macOS/Linux: Permission denied when running scripts**
```bash
chmod +x Track_improved.py
chmod +x track_server.py
chmod +x setup_mac.sh
```

**Windows: Execution policy error**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### SSL Certificate Errors

```bash
# Update certificates
pip3 install --upgrade certifi

# Or on macOS
/Applications/Python\ 3.x/Install\ Certificates.command
```

### Virtual Environment Issues

If you get conflicts, use a virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements_web.txt

# Run Track
python track_server.py
```

---

## Advanced Installation

### Using Docker (Coming Soon)

```bash
# Pull image
docker pull track/track:latest

# Run container
docker run -p 3000:3000 track/track:latest
```

### Development Installation

For contributors:

```bash
# Clone repository
git clone https://github.com/yourusername/Track.git
cd Track

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements_dev.txt
```

---

## Post-Installation

### Update Track

```bash
cd Track
git pull origin main
pip3 install --upgrade -r requirements_web.txt
```

### Uninstall Track

```bash
# Remove directory
rm -rf Track

# Uninstall Python packages (optional)
pip3 uninstall requests phonenumbers flask flask-cors
```

---

## Platform-Specific Notes

### Windows Subsystem for Linux (WSL)

Track works great in WSL! Follow the Linux installation steps.

To access from Windows browser:
```
http://localhost:3000
```

### Raspberry Pi

Track works on Raspberry Pi! Follow Linux installation steps.

**Note**: Username search might be slower due to CPU limitations.

### Chrome OS (Linux)

Enable Linux on Chrome OS, then follow Linux installation steps.

---

## Getting Help

If installation fails:

1. **Check Documentation**: Read the troubleshooting section above
2. **Search Issues**: Check [GitHub Issues](https://github.com/yourusername/Track/issues)
3. **Ask for Help**: Create a new issue with:
   - Your OS and version
   - Python version (`python3 --version`)
   - Error messages (full text)
   - Steps you've tried

---

## Next Steps

After successful installation:

1. **Read the README**: Get familiar with features
2. **Try Examples**: Test with known data (8.8.8.8, +14155552671, github)
3. **Explore Documentation**: Check WEB_UI_GUIDE.md and SETUP_GUIDE.md
4. **Customize**: Adjust colors, add features
5. **Contribute**: Report bugs, suggest features

---

**Congratulations! Track is now installed and ready to use! 🎉**

For usage instructions, see [README.md](README.md)
