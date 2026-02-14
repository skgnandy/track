# 🔍 Track - Intelligence Gathering Toolkit

> A powerful, modern toolkit for IP tracking, phone number validation, and username searches across social media platforms. Available in both beautiful Web UI and fast CLI versions.

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()
[![Made with Love](https://img.shields.io/badge/Made%20with-❤-red.svg)]()

<div align="center">
  <img src="https://img.shields.io/badge/UI-Web%20%2B%20CLI-purple.svg" alt="UI Types">
  <img src="https://img.shields.io/badge/API-REST-orange.svg" alt="API">
  <img src="https://img.shields.io/badge/Design-Cyberpunk-ff006e.svg" alt="Design">
</div>

---

## ✨ Features

### 🌍 IP Tracker
- **Geolocation** - Country, city, region, coordinates
- **ISP Information** - Organization, ASN, domain
- **Timezone** - Current time, UTC offset
- **Google Maps** - Direct link to location
- **Connection Details** - Type, postal code, calling code

### 📱 Phone Number Tracker
- **Validation** - Check if number is valid/possible
- **Carrier** - Network operator information
- **Location** - Geographic region and timezone
- **Formatting** - International, E.164, national formats
- **Type Detection** - Mobile, landline, or other

### 👤 Username Search
- **Multi-Platform** - Search across 12+ social media sites
- **Real-time Check** - Live availability status
- **Direct Links** - Click to visit profiles
- **Platforms**: GitHub, Twitter, Instagram, Reddit, YouTube, TikTok, Facebook, Pinterest, Medium, Twitch, Spotify, LinkedIn

### 🔍 My IP Address
- **Instant Display** - See your public IP immediately
- **No Input** - Automatic detection

---

## 🎨 Two Ways to Use

### 🌐 Web UI (Recommended)
Beautiful, modern interface with cyberpunk aesthetics

**Features:**
- 🎨 Stunning visual design with neon accents
- ✨ Smooth animations and transitions
- 📱 Fully responsive (mobile, tablet, desktop)
- 🚀 Real-time results display
- 💡 Interactive cards and modals
- 🎯 Click-based interface (no typing!)

### 💻 CLI Version
Fast, powerful terminal interface

**Features:**
- ⚡ Lightning-fast performance
- 🎨 Colorful terminal output
- ⌨️ Keyboard-driven workflow
- 🔧 Easy to script/automate
- 📦 No server required
- 🛡️ Comprehensive error handling

---

## 🚀 Quick Start

### Web UI Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/Track.git
cd Track

# 2. Install dependencies
pip3 install -r requirements_web.txt

# 3. Start the server
python3 track_server.py

# 4. Open your browser
# Visit: http://localhost:3000
```

### CLI Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/Track.git
cd Track

# 2. Install dependencies
pip3 install -r requirements.txt

# 3. Run the program
python3 Track_improved.py
```

---

## 📋 Requirements

### System Requirements
- **Python**: 3.6 or higher
- **OS**: Windows, macOS, or Linux
- **Internet**: Active connection required
- **Browser**: Modern browser (for Web UI)

### Python Packages

**For Web UI:**
```
requests
phonenumbers
flask
flask-cors
```

**For CLI:**
```
requests
phonenumbers
```

Install with:
```bash
# Web UI
pip3 install -r requirements_web.txt

# CLI
pip3 install -r requirements.txt
```

---

## 📖 Usage

### Web UI Usage

1. **Start Server**
   ```bash
   python3 track_server.py
   ```

2. **Open Browser**
   - Navigate to `http://localhost:3000`

3. **Use Interface**
   - Click any card (IP Tracker, Phone Tracker, Username Search, My IP)
   - Enter information when prompted
   - View beautiful, formatted results

### CLI Usage

1. **Run Program**
   ```bash
   python3 Track_improved.py
   ```

2. **Select Option**
   - Choose 1-4 from the menu
   - Enter requested information
   - View results in terminal

### Example Commands

**Test IP Tracking:**
```
# Try with Google DNS
8.8.8.8
```

**Test Phone Tracking:**
```
# Try with US number
+14155552671
```

**Test Username Search:**
```
# Try with known username
github
```

---

## 🎯 API Endpoints (Web Version)

The Flask backend provides REST API endpoints:

### IP Tracking
```
GET /api/ip/<ip_address>
```
**Example:** `http://localhost:3000/api/ip/8.8.8.8`

### Phone Tracking
```
GET /api/phone/<phone_number>
```
**Example:** `http://localhost:3000/api/phone/+14155552671`

### Username Search
```
GET /api/username/<username>
```
**Example:** `http://localhost:3000/api/username/github`

### My IP
```
GET /api/myip
```
**Example:** `http://localhost:3000/api/myip`

**Response Format:**
```json
{
  "success": true,
  "data": { ... }
}
```

---

## 📁 Project Structure

```
Track/
│
├── 🌐 Web UI Files
│   ├── track_ui.html              # React frontend interface
│   ├── track_server.py            # Flask API backend
│   └── requirements_web.txt       # Web dependencies
│
├── 💻 CLI Files
│   ├── Track_improved.py          # Enhanced CLI version
│   ├── Track.py                   # Original CLI version
│   └── requirements.txt           # CLI dependencies
│
├── 📚 Documentation
│   ├── README.md                  # This file
│   ├── WEB_UI_GUIDE.md           # Web UI detailed guide
│   ├── SETUP_GUIDE.md            # CLI setup guide
│   ├── IMPROVEMENTS_DETAILED.md   # Technical improvements
│   └── UI_SHOWCASE.md            # Design documentation
│
├── 🔧 Utilities
│   └── setup_mac.sh              # Automated setup script
│
└── 🎨 Assets
    └── asset/                     # Images and icons
```

---

## 🎨 Screenshots

### Web UI
The web interface features a stunning cyberpunk-inspired design with:
- Dark background with neon gradient effects
- Interactive cards with hover animations
- Real-time results with smooth transitions
- Fully responsive layout

### CLI Interface
```
████████╗██████╗  █████╗  ██████╗ ██╗  ██╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝ ██║ ██╔╝
   ██║   ██████╔╝███████║██║      █████╔╝ 
   ██║   ██╔══██╗██╔══██║██║      ██╔═██╗ 
   ██║   ██║  ██║██║  ██║╚██████╔╝██║  ██╔
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝

              [ + ]  C O D E   B Y  S A I  [ + ]

[ 1 ] IP Tracker
[ 2 ] Show Your IP
[ 3 ] Phone Number Tracker
[ 4 ] Username Search
[ 0 ] Exit
```

---

## 🛠️ Configuration

### Change Server Port (Web UI)

Edit `track_server.py`:
```python
# Change the last line:
app.run(host='0.0.0.0', port=3000, debug=True)
# To:
app.run(host='0.0.0.0', port=8080, debug=True)
```

### Customize Colors (Web UI)

Edit `track_ui.html` CSS variables:
```css
:root {
    --accent-cyan: #00f0ff;
    --accent-pink: #ff006e;
    --accent-purple: #8338ec;
}
```

### Customize Colors (CLI)

Edit `Track_improved.py` color codes:
```python
Gr = '\033[1;32m'  # Green
Cy = '\033[1;36m'  # Cyan
```

---

## 🐛 Troubleshooting

### Common Issues

**"Module not found" error:**
```bash
pip3 install --user requests phonenumbers flask flask-cors
```

**"Port already in use":**
- Change the port in `track_server.py`
- Or kill the process using the port

**"Permission denied":**
```bash
chmod +x Track_improved.py
chmod +x setup_mac.sh
```

**Colors not displaying (CLI):**
- Check if terminal supports ANSI colors
- Try a different terminal emulator

**Can't connect to server:**
- Verify server is running
- Check firewall settings
- Try `http://127.0.0.1:3000` instead

---

## 🔒 Security & Privacy

- ✅ **Local Processing** - Data processed on your machine
- ✅ **No Data Storage** - No information saved or logged
- ✅ **Public APIs** - Uses only public, legal data sources
- ✅ **Open Source** - All code visible and auditable
- ⚠️ **Educational Use** - Intended for learning and legitimate purposes

**Important:** Use responsibly and ethically. Only search for information you have permission to access.

---

## 🌟 Why Track?

### For Developers
- **Learn Web Development** - React, Flask, REST APIs
- **Study Error Handling** - Comprehensive exception handling
- **Explore APIs** - Integration with multiple services
- **Practice Python** - Modern Python best practices

### For IT Professionals
- **Network Troubleshooting** - Quick IP geolocation
- **Contact Verification** - Validate phone numbers
- **Security Research** - Check digital footprints
- **OSINT Training** - Open-source intelligence gathering

### For Everyone
- **Easy to Use** - Both GUI and CLI options
- **Fast Results** - Instant information retrieval
- **Beautiful Design** - Modern, professional interface
- **Well Documented** - Comprehensive guides included

---

## 🔄 Updates & Improvements

### Version 2.0 (Current)
- ✅ Added beautiful Web UI
- ✅ REST API backend
- ✅ Comprehensive error handling
- ✅ Mobile responsive design
- ✅ Real-time results display
- ✅ Fixed coordinate conversion bug
- ✅ Added more social platforms

### Version 1.0
- Initial CLI release
- Basic IP, phone, username tracking
- Terminal-based interface

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Ideas
- Add more social media platforms
- Implement result caching
- Add export to CSV/JSON
- Create batch processing mode
- Add user authentication
- Improve error messages
- Add more API providers

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Credits & Acknowledgments

### Original Code
- **HUNX04** - Original CLI implementation

### Improvements & Web UI
- Enhanced error handling and stability
- Beautiful web interface with React
- REST API backend with Flask
- Comprehensive documentation

### APIs Used
- **ipwho.is** - IP geolocation data
- **ipify.org** - Public IP detection
- **phonenumbers** - Phone number parsing and validation

### Design Inspiration
- Cyberpunk aesthetics
- Modern web design trends
- Sci-fi movie interfaces

---

## 📧 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/Track/issues)
- **Documentation**: Check the documentation files in the repo
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/Track/discussions)

---

## 🎓 Learn More

### Tutorials
- [Web UI Guide](WEB_UI_GUIDE.md) - Complete web interface documentation
- [CLI Setup Guide](SETUP_GUIDE.md) - Terminal version setup
- [Demo Examples](DEMO_EXAMPLES.md) - Usage examples

### Technical Docs
- [Improvements Details](IMPROVEMENTS_DETAILED.md) - Technical improvements
- [UI Showcase](UI_SHOWCASE.md) - Design philosophy

---

## 🌟 Star History

If you find this project useful, please give it a ⭐ on GitHub!

---

## 🚀 Quick Links

- [📖 Full Documentation](docs/)
- [💻 CLI Tutorial](SETUP_GUIDE.md)
- [🐛 Report Bug](https://github.com/yourusername/Track/issues/new)
- [💡 Request Feature](https://github.com/yourusername/Track/issues/new)

---

<div align="center">

### Made with ❤️ and Python

**[⬆ Back to Top](#-track---intelligence-gathering-toolkit)**

</div>

---

## 🎉 Get Started Now!

Choose your preferred method and start tracking:

### Quick Start - Web UI
```bash
git clone https://github.com/yourusername/Track.git && cd Track
pip3 install -r requirements_web.txt
python3 track_server.py
# Open http://localhost:3000
```

### Quick Start - CLI
```bash
git clone https://github.com/yourusername/Track.git && cd Track
pip3 install -r requirements.txt
python3 Track_improved.py
```

**Happy Tracking! 🔍✨**
