# Contributing to Track

First off, thank you for considering contributing to Track! 🎉

The following is a set of guidelines for contributing to Track. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Style Guidelines](#style-guidelines)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

This project and everyone participating in it is governed by our commitment to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior includes:**
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate

---

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

**Bug Report Template:**
```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. Enter '...'
4. See error

**Expected behavior**
A clear description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g., macOS 12.0, Windows 11, Ubuntu 22.04]
 - Python Version: [e.g., 3.9.7]
 - Browser (for Web UI): [e.g., Chrome 96, Firefox 95]
 - Version: [e.g., 2.0]

**Additional context**
Add any other context about the problem here.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description** of the enhancement
- **Step-by-step description** of the suggested enhancement
- **Explanation** of why this enhancement would be useful
- **Examples** of how the enhancement would be used
- **Mockups** or screenshots if applicable

### Pull Requests

- Fill in the required template
- Follow the style guidelines
- Include screenshots and animated GIFs in your pull request whenever possible
- End all files with a newline
- Write clear, descriptive commit messages

---

## Style Guidelines

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

**Examples:**
```
Add username search for Spotify
Fix coordinate conversion bug in IP tracker
Update documentation for Web UI setup
```

### Python Style Guide

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with these specifics:

- Use 4 spaces for indentation (not tabs)
- Maximum line length of 100 characters
- Use descriptive variable names
- Add docstrings to functions and classes
- Add comments for complex logic

**Example:**
```python
def track_ip(ip_address):
    """
    Track IP address and return detailed information.
    
    Args:
        ip_address (str): The IP address to track
        
    Returns:
        dict: Dictionary containing IP information
        
    Raises:
        ValueError: If IP address is invalid
    """
    # Validate IP address format
    if not is_valid_ip(ip_address):
        raise ValueError("Invalid IP address format")
    
    # Fetch data from API
    response = requests.get(f"https://ipwho.is/{ip_address}", timeout=10)
    return response.json()
```

### JavaScript/React Style Guide

For the Web UI:

- Use consistent indentation (2 spaces)
- Use camelCase for variables and functions
- Use PascalCase for React components
- Add comments for complex logic
- Use const for variables that don't change

**Example:**
```javascript
const TrackApp = () => {
    const [loading, setLoading] = useState(false);
    
    // Fetch IP data from backend API
    const fetchIPData = async (ip) => {
        setLoading(true);
        try {
            const response = await fetch(`/api/ip/${ip}`);
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching IP data:', error);
        } finally {
            setLoading(false);
        }
    };
    
    return <div>...</div>;
};
```

### CSS Style Guide

- Use CSS custom properties for colors and common values
- Use meaningful class names
- Group related properties together
- Add comments for complex selectors

**Example:**
```css
:root {
    --primary-color: #00f0ff;
    --secondary-color: #ff006e;
}

.card {
    /* Layout */
    display: flex;
    flex-direction: column;
    
    /* Spacing */
    padding: 20px;
    margin: 10px;
    
    /* Appearance */
    background: var(--primary-color);
    border-radius: 8px;
    
    /* Animation */
    transition: transform 0.3s ease;
}
```

---

## Development Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Git
- Modern web browser (for Web UI development)

### Setup Steps

1. **Fork and Clone**
   ```bash
   git clone https://github.com/yourusername/Track.git
   cd Track
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   # For Web UI development
   pip install -r requirements_web.txt
   
   # For CLI development
   pip install -r requirements.txt
   ```

4. **Run Tests**
   ```bash
   # Test CLI version
   python3 Track_improved.py
   
   # Test Web UI
   python3 track_server.py
   # Then open http://localhost:3000
   ```

### Development Workflow

1. Create a new branch for your feature
   ```bash
   git checkout -b feature/my-new-feature
   ```

2. Make your changes
   - Write code
   - Add tests if applicable
   - Update documentation

3. Test your changes
   - Test CLI functionality
   - Test Web UI in browser
   - Check for errors and edge cases

4. Commit your changes
   ```bash
   git add .
   git commit -m "Add my new feature"
   ```

5. Push to your fork
   ```bash
   git push origin feature/my-new-feature
   ```

6. Create a Pull Request

---

## Pull Request Process

1. **Update Documentation**
   - Update README.md if you've added features
   - Add comments to complex code
   - Update relevant guide files

2. **Test Thoroughly**
   - Test on different operating systems if possible
   - Test both CLI and Web UI if both are affected
   - Check for edge cases and error scenarios

3. **Follow the PR Template**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update
   
   ## Testing
   Describe how you tested your changes
   
   ## Screenshots
   If applicable, add screenshots
   
   ## Checklist
   - [ ] My code follows the style guidelines
   - [ ] I have commented my code where necessary
   - [ ] I have updated the documentation
   - [ ] My changes generate no new warnings
   - [ ] I have tested my changes
   ```

4. **Wait for Review**
   - Be patient and responsive to feedback
   - Make requested changes promptly
   - Be open to suggestions

5. **Merge**
   - Once approved, your PR will be merged
   - You may be asked to rebase or squash commits

---

## Feature Request Guidelines

When requesting features:

1. **Check existing issues** - Your idea might already exist
2. **Provide use case** - Explain why this feature would be useful
3. **Be specific** - Detailed requests are more likely to be implemented
4. **Consider alternatives** - Show you've thought about different approaches

**Feature Request Template:**
```markdown
## Feature Description
Clear description of the feature

## Problem it Solves
What problem does this feature address?

## Proposed Solution
How you envision this working

## Alternatives Considered
Other approaches you've thought about

## Additional Context
Any other information, mockups, or examples
```

---

## Areas to Contribute

### High Priority
- 🐛 Bug fixes
- 📱 More social media platforms
- 🌍 Internationalization (i18n)
- ♿ Accessibility improvements
- 📊 Export functionality (CSV, JSON, PDF)

### Medium Priority
- 🎨 UI/UX improvements
- ⚡ Performance optimizations
- 📝 Documentation improvements
- 🧪 Test coverage
- 🔍 Additional data sources

### Low Priority
- 🎭 Themes and customization
- 🤖 Automation features
- 📈 Analytics and statistics
- 🔔 Notifications
- 💾 Result caching

---

## Questions?

If you have questions about contributing:

1. Check existing documentation
2. Search closed issues
3. Open a new discussion
4. Ask in your pull request

---

## Recognition

Contributors will be:
- Listed in the README
- Mentioned in release notes
- Given credit in commit messages

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Thank You!

Your contributions make Track better for everyone. Thank you for taking the time to contribute! 🙏

Happy coding! 🚀
