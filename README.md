# 🔍 Candidate Profile Analyzer

> **AI-Powered Due Diligence Through Digital Footprint Analysis**

A comprehensive Streamlit application that leverages AI agents to analyze candidates' online presence for hiring and partnership decisions. This tool performs ethical OSINT (Open Source Intelligence) research using publicly available data to provide insights into a person's professional background, reputation, and cultural fit.

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [AI Agents](#-ai-agents)
- [Analysis Reports](#-analysis-reports)
- [API Requirements](#-api-requirements)
- [Privacy & Ethics](#-privacy--ethics)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### 🎯 **Core Capabilities**

- **Multi-Agent Analysis**: 6 specialized AI agents working in coordination
- **Comprehensive Research**: Social media, professional networks, and web presence
- **Professional Assessment**: Career history, skills, and achievements analysis
- **Reputation Monitoring**: Risk detection and controversy identification
- **Cultural Fit Evaluation**: Team compatibility assessment
- **Narrative Generation**: Comprehensive life story compilation

### 🖥️ **User Interface**

- **Modern Design**: Gradient backgrounds with smooth animations
- **Responsive Layout**: Mobile-friendly interface
- **Real-time Progress**: Visual progress tracking during analysis
- **Interactive Results**: Expandable sections with download options
- **Secure Configuration**: Password-protected API key management

### 📊 **Output Formats**

- **Markdown Reports**: Professional, formatted documentation
- **Individual Downloads**: Separate files for each analysis type
- **Complete Package**: Comprehensive report compilation
- **Interactive Display**: Web-based result viewing

## 🏗️ Architecture

### Agent-Based System

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Research Agent │    │Profile Analyzer │    │Narrative Writer │
│                 │    │                 │    │                 │
│ OSINT Expert    │    │ Pattern Analyst │    │ Biographer      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│Professional     │    │Reputation       │    │Cultural Fit     │
│Analyst          │    │Checker          │    │Evaluator        │
│                 │    │                 │    │                 │
│ HR Tech Expert  │    │ Risk Investigator│    │ Culture Expert  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Data Flow

1. **Input Collection**: Name, company, location
2. **Agent Coordination**: CrewAI orchestrates multi-agent workflow
3. **Parallel Processing**: Agents work simultaneously on different aspects
4. **Data Synthesis**: Results compiled into comprehensive reports
5. **Output Generation**: Formatted reports with download capabilities

## 🚀 Installation

### Prerequisites

- Python 3.8+
- pip package manager
- Internet connection for API access

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/candidate-profile-analyzer.git
   cd candidate-profile-analyzer
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Project structure**
   ```
   candidate-profile-analyzer/
   ├── app.py                          # Main Streamlit application
   ├── requirements.txt                # Python dependencies
   ├── src/
   │   └── social_activity_of_a_person/
   │       ├── crew.py                 # CrewAI implementation
   │       ├── agents.yaml             # Agent definitions
   │       └── tasks.yaml              # Task configurations
   └── README.md                       # This file
   ```

## ⚙️ Configuration

### Required API Keys

The application requires two API keys for operation:

1. **Google Gemini API Key**

   - Get from: [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Used for: AI-powered analysis and content generation

2. **Serper API Key**
   - Get from: [Serper.dev](https://serper.dev)
   - Used for: Web search capabilities

### Environment Setup

Set your API keys either through:

- **UI Configuration**: Use the sidebar settings in the app
- **Environment Variables**: Set `GEMINI_API_KEY` and `SERPER_API_KEY`
- **Direct Assignment**: Configure within the application

## 🎮 Usage

### Starting the Application

```bash
streamlit run app.py
```

### Step-by-Step Process

1. **Launch Application**: Open in your browser (typically `http://localhost:8501`)
2. **Configure API Keys**: Enter your Gemini and Serper API keys in the sidebar
3. **Enter Candidate Details**:
   - Full name of the person
   - Company/institution affiliation
   - Geographic location
4. **Start Analysis**: Click "🚀 Start Analysis" button
5. **Monitor Progress**: Watch real-time progress updates
6. **Review Results**: Explore generated reports in expandable sections
7. **Download Reports**: Save individual or complete analysis packages

### Sample Input

```
Full Name: Om Anand
Company: IIT Bhilai
Location: Bihar, India
```

## 🤖 AI Agents

### 1. **Research Agent** 🔍

- **Role**: Social Research Agent
- **Expertise**: OSINT (Open Source Intelligence)
- **Function**: Gathers public data from social media, news, and web platforms
- **Output**: Comprehensive digital footprint analysis

### 2. **Profile Analyzer** 🧠

- **Role**: Behavioral Pattern Analyst
- **Expertise**: Digital psychology and pattern recognition
- **Function**: Detects behavioral patterns and lifestyle insights
- **Output**: Behavioral analysis and personality indicators

### 3. **Narrative Writer** ✍️

- **Role**: Personal Biographer
- **Expertise**: Storytelling and narrative construction
- **Function**: Creates engaging life stories from factual data
- **Output**: Comprehensive biographical narrative

### 4. **Professional Analyst** 💼

- **Role**: Work & Skills Investigator
- **Expertise**: Career assessment and professional evaluation
- **Function**: Analyzes job history, skills, and career progression
- **Output**: Professional background assessment

### 5. **Reputation Checker** 🚨

- **Role**: Digital Risk Investigator
- **Expertise**: Risk assessment and controversy detection
- **Function**: Identifies potential red flags and reputation risks
- **Output**: Risk assessment and reputation analysis

### 6. **Cultural Fit Evaluator** 👥

- **Role**: Cultural Fit Evaluator
- **Expertise**: Organizational psychology and culture assessment
- **Function**: Evaluates team compatibility and cultural alignment
- **Output**: Cultural fit assessment with recommendations

## 📊 Analysis Reports

### Generated Reports

1. **📌 Research Summary** (`research_task.md`)

   - Overview of online presence
   - Key findings and digital footprint
   - Platform analysis and content review

2. **💼 Professional Background** (`professional_background.md`)

   - Career history and achievements
   - Skills assessment and endorsements
   - Professional network analysis

3. **🚨 Reputation Check** (`reputation_check.md`)

   - Risk assessment and red flags
   - Controversy detection
   - Public perception analysis

4. **🧠 Behavior & Pattern Analysis** (`analysis_task.md`)

   - Behavioral insights and patterns
   - Lifestyle and interest analysis
   - Personality indicators

5. **👥 Cultural Fit Evaluation** (`cultural_fit.md`)

   - Team compatibility assessment
   - Communication style analysis
   - Organizational alignment evaluation

6. **📘 Final Life Story** (`life_story.md`)
   - Comprehensive biographical narrative
   - 500-800 word detailed report
   - Complete personal and professional profile

## 🔑 API Requirements

### Gemini API (Google AI)

- **Purpose**: Powers AI agents for analysis and content generation
- **Pricing**: Free tier available with usage limits
- **Documentation**: [Google AI Documentation](https://ai.google.dev/docs)

### Serper API

- **Purpose**: Provides web search capabilities for data gathering
- **Pricing**: Free tier with 2,500 searches/month
- **Documentation**: [Serper Documentation](https://serper.dev/docs)

### Rate Limits

- Gemini: Varies by model and tier
- Serper: 2,500 searches/month (free tier)

## 🔒 Privacy & Ethics

### Ethical Guidelines

- **Public Data Only**: Analyzes only publicly available information
- **No Personal Data Storage**: No permanent storage of personal information
- **Transparency**: Clear disclosure of data sources and methods
- **Purpose Limitation**: Designed for legitimate hiring and partnership decisions

### Data Handling

- **Temporary Processing**: Data processed only during analysis session
- **No Permanent Storage**: Results not stored on servers
- **User Control**: Users control all data downloads and retention
- **API Compliance**: Adheres to API terms of service

### Legal Considerations

- **Compliance**: Designed to comply with privacy regulations
- **Legitimate Interest**: Supports legitimate business interests
- **User Responsibility**: Users responsible for lawful use
- **Data Minimization**: Collects only necessary information

## 🛠️ Technical Specifications

### Dependencies

```
streamlit>=1.28.0
crewai>=0.28.0
langchain>=0.1.0
google-generativeai>=0.3.0
requests>=2.31.0
python-dotenv>=1.0.0
```

### System Requirements

- **Memory**: Minimum 2GB RAM
- **Storage**: 1GB free space
- **Network**: Stable internet connection
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)

### Performance

- **Analysis Time**: 2-5 minutes per candidate
- **Concurrent Users**: Depends on server specifications
- **Scalability**: Horizontal scaling supported

## 🤝 Contributing

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include type hints where appropriate

### Issues and Bugs

- Report issues on GitHub
- Include reproduction steps
- Provide system information
- Attach relevant logs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CrewAI**: Multi-agent orchestration framework
- **Streamlit**: Web application framework
- **Google AI**: Gemini API for language processing
- **Serper**: Web search API service

## 📞 Support

For support, questions, or feature requests:

- **GitHub Issues**: [Create an issue](https://github.com/yourusername/candidate-profile-analyzer/issues)
- **Documentation**: Check this README and code comments
- **Community**: Join discussions in GitHub Discussions

---

<div align="center">

**Built with ❤️ for ethical candidate evaluation**

[⭐ Star this project](https://github.com/yourusername/candidate-profile-analyzer) | [🐛 Report Bug](https://github.com/yourusername/candidate-profile-analyzer/issues) | [🚀 Request Feature](https://github.com/yourusername/candidate-profile-analyzer/issues)

</div>
