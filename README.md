# 📚 PDF Learner - AI Question Generator

[![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red.svg)](https://github.com/ayushgatla)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/ayushgatla)

> Transform any PDF into an interactive learning experience with AI-powered question generation and instant feedback.

![PDF Learner Demo](https://via.placeholder.com/800x400/1a1b26/7aa2f7?text=PDF+Learner+Demo)

## ✨ Features

### 🤖 AI-Powered Question Generation

- Upload any PDF and get instant questions
- Multiple question formats: MCQ, Short Answer, Long Answer
- Context-aware questions based on your content

### 📊 Smart Answer Evaluation

- **Split-screen feedback interface** - See your answer and AI feedback side-by-side
- Real-time grading with detailed explanations
- Color-coded feedback (✅ Correct, ⚠️ Needs Work, 🔴 Missed)
- Percentage scores with progress visualization

### 💬 Chat Management

- Multiple conversation threads
- Delete and manage chats easily
- Persistent chat history
- Clean, minimal UI inspired by modern chat apps

### 🎨 Modern UI/UX

- Dark theme with Tokyo Night color palette
- Smooth animations and transitions
- Responsive design for all devices
- Icon-based question type toggles

## 🚀 Quick Start

### Prerequisites

```bash
- Modern web browser (Chrome, Firefox, Safari)
- Text editor (VS Code recommended)
- Basic knowledge of HTML/CSS/JavaScript
```

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/ayushgatla/pdf-learner.git
cd pdf-learner
```

2. **Open in browser**

```bash
# Just open index.html in your browser
# No build process required!
```

3. **Start learning**

- Upload a PDF
- Toggle question types (MCQ, Short, Long)
- Answer questions and get instant feedback

## 📁 Project Structure

```
pdf-learner/
│
├── index.html              # Main HTML file
├── style.css              # Custom styles & Tailwind directives
├── app.js                 # Core application logic
│
├── assets/                # Images and icons
│   ├── background.jpg
│   ├── photos.jpg
│   └── icons/
│
└── README.md             # You're here!
```

## 🛠️ Tech Stack

| Technology             | Purpose                          |
| ---------------------- | -------------------------------- |
| **HTML5**              | Structure                        |
| **CSS3**               | Styling                          |
| **Tailwind CSS**       | Utility-first styling            |
| **Vanilla JavaScript** | Application logic                |
| **Font Awesome**       | Icons                            |
| **PDF.js**             | PDF parsing (planned)            |
| **DeepSeek API**       | AI question generation (planned) |

## 🎯 Roadmap

- [x] Basic chat interface
- [x] Multiple question types
- [x] Split-screen feedback UI
- [x] Chat deletion
- [x] Modern toggle buttons
- [ ] DeepSeek API integration
- [ ] PDF text extraction
- [ ] User authentication
- [ ] Progress tracking & analytics
- [ ] Export conversation history
- [ ] Difficulty level selection
- [ ] Dark/Light theme toggle
- [ ] Mobile app version

## 🤝 Contributing

Contributions are what make the open-source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 💡 Feature Ideas

- Multi-language support
- Voice input for answers
- Collaborative learning mode
- Gamification elements
- Integration with other LLM APIs

## 📝 Usage Example

```javascript
// Upload a PDF
pdfUpload.addEventListener("change", (e) => {
  const file = e.target.files[0];
  // Questions are automatically generated based on toggles
});

// Submit answer and get AI feedback
function submitAnswer(idx, type) {
  const answer = document.getElementById(`answer-${idx}`).value;
  // AI analyzes and provides detailed feedback
}
```

## 🎨 UI Screenshots

### Question Types Toggle

![Question Types](https://via.placeholder.com/600x200/16161e/7aa2f7?text=MCQ+|+Short+|+Long)

### Split-Screen Feedback

![Feedback Interface](https://via.placeholder.com/800x400/1a1b26/9ece6a?text=Your+Answer+|+AI+Feedback)

### Chat Management

![Chat List](https://via.placeholder.com/300x400/16161e/7aa2f7?text=Chat+List+with+Delete)

## ⚙️ Configuration

### Tailwind CSS

This project uses Tailwind via CDN for rapid prototyping:

```html
<script src="https://cdn.tailwindcss.com"></script>
```

For production, consider building with PostCSS for better performance.

### API Integration (Coming Soon)

```javascript
// Example API configuration
const API_CONFIG = {
  endpoint: "YOUR_API_ENDPOINT",
  apiKey: "YOUR_DEEPSEEK_API_KEY",
  model: "deepseek-chat",
};
```

## 🐛 Known Issues

- Mock feedback currently used (AI API integration pending)
- PDF parsing not yet implemented
- No data persistence (localStorage planned)
- Some mobile responsiveness improvements needed

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👨‍💻 Author

**Ayush Gatla**

- Website: [ayushgatla.github.io](https://ayushgatla.github.io)
- GitHub: [@ayushgatla](https://github.com/ayushgatla)
- LinkedIn: [Ayush Gatla](https://www.linkedin.com/in/ayush-gatla-575335324/)
- Instagram: [@ayushgatla](https://www.instagram.com/ayushgatla/)

## 🙏 Acknowledgments

- [Tailwind CSS](https://tailwindcss.com/) - For making styling not painful
- [Font Awesome](https://fontawesome.com/) - For beautiful icons
- [Tokyo Night Theme](https://github.com/enkia/tokyo-night-vscode-theme) - For color inspiration
- [DeepSeek](https://www.deepseek.com/) - For AI capabilities (planned)

## 💬 Support

If you like this project, please give it a ⭐️ on GitHub!

For bugs or feature requests, please [open an issue](https://github.com/ayushgatla/pdf-learner/issues).

---

<div align="center">
  <p>Made with ❤️ and ☕ by Ayush Gatla</p>
  <p>
    <a href="https://github.com/ayushgatla">GitHub</a> •
    <a href="https://www.linkedin.com/in/ayush-gatla-575335324/">LinkedIn</a> •
    <a href="https://www.instagram.com/ayushgatla/">Instagram</a>
  </p>
</div>
