# CS2 AI Bot

🎯 **AI bot for Counter-Strike 2 using machine learning and computer vision for autonomous gameplay.**

A personal learning project exploring game AI development, computer vision, and real-time decision making.

## 🚀 Project Overview

This project aims to create an AI bot that can play Counter-Strike 2 autonomously using:
- **Computer Vision** for game state recognition
- **Machine Learning** for decision making
- **Input Automation** for game interaction
- **Real-time Processing** for responsive gameplay

⚠️ **Important**: This is purely for educational purposes and local testing only.

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.8+** - Main programming language
- **OpenCV** - Computer vision and image processing
- **PyTorch/TensorFlow** - Machine learning framework (TBD)
- **NumPy** - Numerical computations
- **Pillow (PIL)** - Image manipulation

### Game Integration
- **CS2 Game State Integration (GSI)** - Game data access
- **Screen Capture** - Real-time game state capture
- **Input Automation** - Mouse/keyboard control

## 📁 Project Structure

```
cs2_ai_bot/
├── src/
│   ├── computer_vision/     # Image processing and object detection
│   ├── ml_models/          # Machine learning models
│   ├── game_integration/   # CS2 integration and GSI
│   ├── input_controller/   # Mouse/keyboard automation
│   └── core/               # Main bot logic
├── data/
│   ├── training/           # Training data and datasets
│   ├── models/             # Saved ML models
│   └── screenshots/        # Captured game screenshots
├── config/
│   ├── settings.yml        # Bot configuration
│   └── keybinds.yml        # Key bindings and controls
├── tests/                  # Unit tests
├── docs/                   # Documentation
└── notebooks/              # Jupyter notebooks for experimentation
```

## 🎯 Development Roadmap

### Phase 1: Foundation (Current)
- [x] Project setup and structure
- [ ] Screen capture implementation
- [ ] Basic computer vision pipeline
- [ ] CS2 GSI integration

### Phase 2: Core AI
- [ ] Enemy detection model
- [ ] Map awareness system
- [ ] Basic movement AI
- [ ] Weapon handling logic

### Phase 3: Advanced Features
- [ ] Strategic decision making
- [ ] Team coordination (if applicable)
- [ ] Performance optimization
- [ ] Advanced ML models

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nagorixs0/CS2-AI-Bot.git
   cd CS2-AI-Bot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure CS2 GSI**
   - Follow setup guide in `docs/cs2_gsi_setup.md`

## 🎮 Usage

```bash
# Start the AI bot
python -m src.main

# Training mode
python -m src.train --mode collect_data

# Testing specific components
python -m src.test_vision
```

## 📚 Learning Resources

### Recommended Reading
- [CS2 Game State Integration Documentation](docs/gsi_documentation.md)
- [Computer Vision for Games](docs/computer_vision_guide.md)
- [Real-time AI Decision Making](docs/ai_architecture.md)

### Helpful Projects
- [igsmo/CSGO-Bot](https://github.com/igsmo/CSGO-Bot) - ML bot for CS:GO

## 🤝 Contributing

This is a learning project, but suggestions and educational contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## ⚖️ Legal & Ethics

- **Educational Purpose Only**: This project is for learning game AI development
- **Local Testing Only**: Not intended for online/competitive play
- **Respect Game ToS**: Always comply with CS2 terms of service
- **No Cheating**: This is not designed for competitive advantage

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Goals

- Learn computer vision techniques
- Understand real-time AI systems
- Explore game AI architecture
- Practice ML model development
- Build a complete AI system from scratch

---

**Happy coding! 🚀**
