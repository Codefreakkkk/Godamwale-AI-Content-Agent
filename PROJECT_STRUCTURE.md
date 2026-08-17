# Project Structure Explanation

## Overview

Godamwale AI Content Agent follows a modular AI-content-agent architecture.

The project separates:

- Streamlit user interface
- Website content extraction
- Agent control and task execution
- AI model communication
- Company knowledge management
- TF-IDF based information retrieval
- Specialized content modules
- Content quality analysis
- Generated content export

The modular structure makes the prototype easier to understand, maintain, test, and extend.

---

# Folder Structure

Godamwale-AI-Content-Agent/

├── .env
│   Stores the private OpenRouter API key.
│   This file should not be shared or committed to Git.

├── .gitignore
│   Defines files and folders that should not be committed.

├── README.md
│   Main project documentation.

├── PROJECT_STRUCTURE.md
│   Explanation of the project structure and workflow.

├── requirements.txt
│   Python dependencies required by the project.

│
├── app/
│
│   ├── streamlit_app.py
│   │   Main Streamlit user interface.
│   │   Handles website loading, task selection,
│   │   competitor website input, AI execution,
│   │   quality analysis, and file downloads.
│
│   ├── agent_controller.py
│   │   Main controller for the AI agent.
│   │   Loads company information, combines website information,
│   │   performs information retrieval, and executes the
│   │   selected AI module.
│
│   ├── ai_agent.py
│   │   Handles communication with the configured AI model
│   │   through the OpenRouter API.
│
│   ├── config.py
│   │   Central configuration file containing adjustable
│   │   AI, RAG, website, and content-processing limits.
│
│   ├── content_quality.py
│   │   Performs rule-based content quality analysis and
│   │   generates an overall quality score and suggestions.
│
│   ├── decision_engine.py
│   │   Uses the AI model as a request classifier and selects
│   │   one of the supported content modules.
│
│   ├── knowledge_base.py
│   │   Loads approved company information from the
│   │   documents/company folder.
│
│   ├── rag_system.py
│   │   Implements the current lightweight TF-IDF based
│   │   retrieval system.
│   │   Handles text chunking, TF-IDF vectorization,
│   │   similarity calculation, and relevant chunk retrieval.
│
│   ├── website_reader.py
│   │   Handles website extraction.
│   │   Fetches web pages, removes unnecessary HTML elements,
│   │   extracts visible text, discovers selected internal pages,
│   │   and calculates website statistics.
│
│   └── modules/
│
│       ├── optimization.py
│       │   Website content optimization module.
│
│       ├── outdated.py
│       │   Detects potentially outdated or unsupported
│       │   information in existing website content.
│
│       ├── blog_generator.py
│       │   Generates customer-facing business blog content
│       │   using approved company information.
│
│       ├── blog_optimizer.py
│       │   Optimizes generated blogs for the target keyword
│       │   while preserving the original topic and useful content.
│
│       ├── seo_optimizer.py
│       │   Performs SEO and AIO-oriented content analysis
│       │   and generates optimization recommendations.
│
│       ├── social_media_generator.py
│       │   Generates professional business social media content.
│
│       ├── email_generator.py
│       │   Generates professional business email content.
│
│       └── competitor_analysis.py
│           Compares supplied Godamwale website content with
│           competitor website content and identifies
│           content gaps and optimization opportunities.
│
│
├── documents/
│
│   └── company/
│       ├── company_info.txt
│       │   Approved company information.
│       │
│       └── services.txt
│           Approved information about company services.
│
│
└── output/
    Stores generated output files such as DOCX responses.

---

# Role of Major Components

## streamlit_app.py

Acts as the presentation layer of the prototype.

It allows users to:

- Enter website URLs.
- Load website content.
- Enter target keywords.
- Select content tasks.
- Enter additional instructions.
- Provide a competitor website.
- Run the AI agent.
- View generated content.
- View content-quality results.
- Download generated content.

---

## agent_controller.py

Acts as the central workflow controller.

Its responsibilities include:

1. Validate the user request.
2. Validate the selected module.
3. Load approved company information.
4. Add website information when available.
5. Create the TF-IDF retrieval database.
6. Retrieve relevant information.
7. Execute the selected AI module.
8. Return the selected module and result.

---

## ai_agent.py

Provides the common AI communication layer.

Instead of every module directly communicating with the AI provider, modules call:

ask_ai()

This keeps AI API communication centralized.

The current implementation uses the OpenRouter API through an OpenAI-compatible client.

---

## knowledge_base.py

Loads approved company information from:

documents/company/

Current files include:

- company_info.txt
- services.txt

These files provide trusted company-specific information for AI processing.

---

## website_reader.py

Handles website content extraction.

The workflow is:

Website URL

↓

HTTP Request

↓

HTML Response

↓

BeautifulSoup Parsing

↓

Remove Non-Content Elements

↓

Extract Visible Text

↓

Clean Text

↓

Discover Selected Internal Pages

↓

Combine Website Content

↓

Apply Configured Content Limit

The reader also produces page-level statistics including:

- Characters
- Estimated tokens

---

## rag_system.py

Implements the current lightweight retrieval system.

The current implementation uses:

- scikit-learn
- TfidfVectorizer
- NumPy

The workflow is:

Input Information

↓

Text Chunking

↓

TF-IDF Vectorization

↓

Query Vectorization

↓

Similarity Calculation

↓

Top Relevant Chunks

↓

Module Context

This is the current prototype implementation of retrieval.

---

## content_quality.py

Provides a basic rule-based evaluation of generated content.

The current quality score contains five categories:

- Readability
- Structure
- Paragraph Quality
- Keyword Usage
- Sentence Quality

Each category contributes up to 20 points.

The final score is displayed out of 100.

---

# AI Modules

The specialized modules are stored inside:

app/modules/

Each module is responsible for a specific content-related task.

Current modules:

### optimization.py

Improves existing website content.

### outdated.py

Identifies potentially outdated or unsupported website information.

### blog_generator.py

Generates a new business blog.

### blog_optimizer.py

Optimizes an already generated blog for a target keyword.

### seo_optimizer.py

Performs SEO and AIO-oriented analysis.

### social_media_generator.py

Generates business social media content.

### email_generator.py

Generates business email content.

### competitor_analysis.py

Compares company and competitor website content.

---

# Current Agent Workflow

For a normal content task:

User

↓

Streamlit Interface

↓

Agent Controller

↓

Company Knowledge

+

Website Information

↓

TF-IDF Retrieval

↓

Relevant Information

↓

Selected AI Module

↓

AI Model

↓

Generated Response

↓

Content Quality Analysis

↓

Display / Download

---

# Blog Workflow

The blog task uses a two-stage pipeline.

User Request

↓

Blog Generation

↓

Generated Blog

↓

Blog Optimization

↓

Optimized Blog

↓

Content Quality Analysis

↓

Final Output

The generated blog is optimized after generation rather than directly replacing the generation process.

---

# Competitor Analysis Workflow

Godamwale Website

↓

Website Content Extraction

↓

Competitor Website

↓

Competitor Content Extraction

↓

Target Keyword

↓

Competitor Analysis Module

↓

Content Comparison

↓

Content Gaps

↓

Recommendations

---

# Website Analysis Limits

The current limits are controlled through:

app/config.py

Current values include:

- Maximum websites: 10
- Maximum pages per website: 5
- Maximum website content passed to AI processing: 12,000 characters

These limits are intentionally configurable and can be changed later if required.

---

# RAG Configuration

The current retrieval configuration is controlled through:

app/config.py

Current values:

- Chunk size: approximately 500 characters
- Top retrieved results: 3

The current prototype uses TF-IDF similarity retrieval rather than a production-scale vector database.

---

# AI Configuration

AI configuration is centralized in:

app/config.py

Current values include:

- AI model
- Maximum generated tokens
- Module context limits
- Website content limits

The API key itself is stored separately in the private .env file.

---

# Adding a New AI Module

New AI capabilities should be added inside:

app/modules/

Example:

app/modules/new_feature.py

A new module should then be connected to:

1. The module validation list.
2. The agent controller.
3. The Streamlit task-selection interface if the feature is user-selectable.
4. The decision engine if automatic request classification is required.

---

# Design Principles

The project follows these principles:

- Modular architecture
- Separation of responsibilities
- Centralized AI communication
- Approved-information grounding
- Controlled AI context
- Lightweight retrieval
- Specialized AI modules
- Configurable processing limits
- Human verification for uncertain information
- Easy future expansion

---

# Current Prototype Status

The project is a functional AI content-agent prototype.

The current implementation supports:

- Website content extraction
- Multiple website input
- Website statistics
- Company knowledge loading
- TF-IDF based information retrieval
- Website content optimization
- SEO & AIO analysis
- Blog generation
- Blog optimization
- Competitor content analysis
- Social media generation
- Email generation
- Outdated content detection
- Content quality scoring
- TXT export
- DOCX export

The prototype has been tested through an end-to-end website loading and blog generation + optimization workflow.