# Godamwale AI Content Agent

## Project Overview

Godamwale AI Content Agent is an AI-powered business content assistant designed to help analyze, optimize, compare, and generate professional business content.

The prototype combines website content extraction, company knowledge, retrieval-based context selection, and specialized AI content modules through a Streamlit interface.

The system is designed with a strong focus on factual grounding. Company-specific information is taken from approved company information and retrieved website content rather than being freely invented by the AI.

---

# Current Prototype Features

## 1. Website Analysis

The system can analyze multiple websites from the Streamlit interface.

Current capabilities include:

- Load up to a configured number of websites.
- Extract visible website text.
- Remove unnecessary HTML elements such as scripts, styles, navigation, headers, footers, SVGs, and other non-content elements.
- Discover selected internal pages.
- Prioritize potentially useful business-related internal pages.
- Display page-level statistics.
- Display total character count.
- Display estimated token count.
- Store extracted website content for AI processing.

### Current Website Limits

- Maximum websites: 10
- Maximum pages per website: 5
- Maximum website content passed into AI processing: 12,000 characters

These limits help control processing size and prevent excessive website crawling or AI context.

---

# 2. Website Content Optimization

The Website Content Optimization module analyzes existing website content and generates recommendations or improved content based on:

- Readability
- Clarity
- Structure
- Business relevance
- Customer-friendliness
- Approved company information

The module is designed to avoid unsupported company-specific claims.

---

# 3. SEO & AIO Analysis

The SEO & AIO module analyzes supplied website content and provides practical optimization recommendations.

The analysis can include:

- Primary keyword opportunities
- Related keyword opportunities
- Search intent
- Meta title suggestions
- Meta description suggestions
- Heading structure
- Content organization
- Readability
- Topic coverage
- Missing or weak information
- Internal linking opportunities
- FAQ opportunities
- Customer-question opportunities
- AI-search/AIO content improvements
- Priority action plan

The module does not guarantee search rankings, traffic, conversions, or AI-search visibility.

Recommendations are based primarily on the supplied website content and approved company information.

---

# 4. Blog Generation + Optimization

The prototype uses a two-stage blog pipeline.

### Stage 1 — Blog Generation

The Blog Generation module creates a customer-facing blog using:

- User-requested topic
- Target keyword
- Approved company information
- Relevant retrieved context

The generated blog includes:

- Title
- Introduction
- Main sections
- Conclusion
- Related keyword suggestions
- Suggested headings
- Basic optimization ideas
- Information requiring verification

### Stage 2 — Blog Optimization

The generated blog is then passed to the Blog Optimization module.

The optimization stage improves:

- Target keyword usage
- Readability
- Headings
- Structure
- Flow
- Repetition
- Content organization

The original topic and useful factual information are preserved.

The module is instructed not to invent unsupported:

- Services
- Locations
- Pricing
- Certifications
- Customers
- Partnerships
- Statistics
- Guarantees
- Operational capabilities
- Other company-specific claims

---

# 5. Competitor Content Analysis

The Competitor Analysis module compares Godamwale website content with supplied competitor website content around a target keyword.

It analyzes:

- Keyword coverage
- Related topics
- Service information
- Search intent
- Content strengths
- Content gaps
- Topic coverage
- Content structure
- Keyword and related-topic usage
- Suggested new content sections
- Content optimization opportunities
- Priority action plan

The module only analyzes the supplied content.

It does not claim actual Google rankings, guaranteed SEO improvements, or guaranteed AI-search visibility.

---

# 6. Content Quality Analysis

After AI-generated content is produced, the prototype calculates a basic content quality score.

The current score is based on five areas:

- Readability
- Structure
- Paragraph Quality
- Keyword Usage
- Sentence Quality

Each category contributes up to 20 points.

The final score is displayed out of 100.

The system also provides improvement suggestions when potential issues are detected.

This is a lightweight prototype-level content quality evaluator rather than a full professional SEO or readability scoring system.

---

# Knowledge Base

The prototype includes an approved company information layer.

Current company information is stored under:

documents/
└── company/
    ├── company_info.txt
    └── services.txt

The knowledge base loads .txt files from the company folder and combines their contents into a single company information context.

This information is used to ground AI-generated company-specific content.

---

# Retrieval-Augmented Generation (RAG)

The prototype includes a lightweight RAG foundation using TF-IDF similarity retrieval.

### Current RAG Workflow

Company Information
        +
Website Information
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
AI Module

### Current RAG Implementation

The prototype uses:

- scikit-learn
- TfidfVectorizer
- TF-IDF similarity
- NumPy

Current configuration:

- Approximate chunk size: 500 characters
- Top retrieved chunks: 3

The RAG system is intentionally lightweight and suitable for the current prototype.

---

# Website Content Processing

Website processing is implemented using:

- Requests
- BeautifulSoup

### Processing Workflow

Website URL
     ↓
HTTP Request
     ↓
HTML Response
     ↓
HTML Parsing
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
Apply Content Limit

The website reader:

- Normalizes URLs.
- Uses an HTTP request timeout.
- Uses a browser-like User-Agent.
- Handles failed requests.
- Extracts visible text.
- Restricts internal links to the same domain.
- Removes URL fragments.
- Prioritizes potentially useful business-related pages.
- Limits the number of pages processed.

---

# AI Integration

The prototype uses OpenRouter for AI model access.

The AI client is configured through environment variables.

Current configured model:

openai/gpt-4o

Maximum generated token limit:

2000 tokens

The application uses a centralized ask_ai() function for AI requests.

The AI integration includes basic handling for:

- Missing API key
- Missing client
- Empty prompts
- Network/API errors
- Empty responses
- Missing response choices
- Missing response messages

---

# Factual Grounding

A major design principle of the prototype is avoiding unsupported company-specific claims.

AI modules are instructed not to invent:

- Services
- Locations
- Pricing
- Discounts
- Certifications
- Statistics
- Customers
- Partnerships
- Awards
- Warehouse counts
- Operational capabilities
- Performance claims
- Guarantees

When information cannot be confirmed, the system can identify it as information requiring verification rather than assuming it to be true.

---

# Streamlit Interface

The prototype uses Streamlit as its user interface.

### Website Analysis

The interface provides:

- Website URL input
- Multiple website support
- Target keyword input
- Website loading
- Page statistics
- Character statistics
- Estimated token statistics

### Content Tasks

The user can select:

1. Website Content Optimization
2. SEO & AIO Analysis
3. Blog Generation + Optimization
4. Competitor Analysis

### Competitor Analysis

When selected, the interface provides:

- Competitor website URL input
- Competitor content extraction
- Competitor website statistics

### Additional Instructions

Users can provide additional instructions such as:

Write for Indian businesses.
Keep the content professional.
Focus on warehouse services.

### Output

The application displays:

- Selected module
- AI-generated response
- Blog generation and optimization stages
- Content quality score
- Quality breakdown
- Improvement suggestions

### Downloads

Generated final content can be downloaded as:

- TXT
- DOCX

---

# System Architecture

Streamlit UI
     ↓
Website Reader
     ↓
Company Knowledge + Website Content
     ↓
TF-IDF RAG System
     ↓
Agent Controller
     ↓
Specialized AI Module
     ↓
OpenRouter AI
     ↓
Content Quality Analysis
     ↓
Display / Download

For the Blog workflow:

Blog Generation
     ↓
Blog Optimization
     ↓
Final Content
     ↓
Quality Analysis
     ↓
Download

---

# Project Structure

Godamwale-AI-Content-Agent/
│
├── .env
├── .gitignore
├── README.md
├── PROJECT_STRUCTURE.md
├── requirements.txt
│
├── app/
│   │
│   ├── agent_controller.py
│   ├── ai_agent.py
│   ├── config.py
│   ├── content_quality.py
│   ├── decision_engine.py
│   ├── knowledge_base.py
│   ├── rag_system.py
│   ├── streamlit_app.py
│   ├── website_reader.py
│   │
│   └── modules/
│       ├── blog_generator.py
│       ├── blog_optimizer.py
│       ├── competitor_analysis.py
│       ├── email_generator.py
│       ├── optimization.py
│       ├── outdated.py
│       ├── seo_optimizer.py
│       └── social_media_generator.py
│
├── documents/
│   └── company/
│       ├── company_info.txt
│       └── services.txt
│
└── output/
    └── godamwale_ai_response.docx

---

# Configuration

Adjustable configuration values are centralized in:

app/config.py

Current configuration:

| Configuration | Value |
|---|---:|
| AI Model | openai/gpt-4o |
| Maximum AI Tokens | 2000 |
| RAG Chunk Size | 500 characters |
| Retrieved RAG Chunks | 3 |
| Maximum Pages / Website | 5 |
| Maximum Websites | 10 |
| Website AI Content Limit | 12,000 characters |
| SEO Content Limit | 8,000 characters |
| Company Information Limit | 6,000 characters |
| Module Context Limit | 6,000 characters |

These limits keep the prototype controlled and prevent unnecessarily large inputs from being processed.

---

# Technology Stack

## Frontend

- Streamlit

## Backend

- Python

## AI Integration

- OpenAI-compatible client
- OpenRouter API

## Website Processing

- Requests
- BeautifulSoup

## RAG

- scikit-learn
- TF-IDF Vectorization
- NumPy

## Document Output

- python-docx

---

# Installation

## 1. Install Dependencies

From the project directory:

py -m pip install -r requirements.txt

---

# Environment Configuration

Create a .env file in the project root.

OPENROUTER_API_KEY=your_api_key_here

The .env file should remain private and should not be committed to source control.

---

# Running the Application

From the project root:

py -m streamlit run app/streamlit_app.py

The Streamlit interface will then open in the browser.

---

# Typical Usage Workflow

## Step 1 — Load Website

Enter one or more website URLs.

Example:

https://www.godamwale.com/

Click:

🌐 Load Websites

The application extracts website content and displays statistics.

## Step 2 — Enter Target Keyword

Example:

warehouse in Kolkata

## Step 3 — Select a Task

For example:

Blog Generation + Optimization

## Step 4 — Add Instructions

Example:

Write for Indian businesses.
Keep it professional and customer-focused.

## Step 5 — Run the Agent

Click:

🚀 Run AI Agent

## Step 6 — Review Output

The application displays the selected module and generated content.

For the blog workflow, both stages are displayed:

Blog Generation
        ↓
Blog Optimization

## Step 7 — Review Quality

The application calculates a prototype content quality score and provides suggestions.

## Step 8 — Download

The final content can be downloaded as:

- TXT
- DOCX

---

# Prototype Limitations

## Website Extraction

- Only a limited number of pages are processed per website.
- Website extraction is based on visible HTML text.
- JavaScript-heavy content may not be fully captured.
- Website crawling is not a complete web crawler.

## RAG

The current RAG system uses TF-IDF similarity rather than advanced embedding-based semantic retrieval.

## AI Output

AI-generated content should still be reviewed by a human before publishing.

## Content Quality

The quality score is a lightweight rule-based prototype evaluator and should not be treated as a professional SEO or editorial score.

## Company Information

The prototype currently relies on the company information available in the configured knowledge files.

---

# Current Prototype Status

The current prototype supports:

- Website content extraction
- Multiple website input
- Website statistics
- Company knowledge retrieval
- TF-IDF based RAG retrieval
- Website content optimization
- SEO & AIO analysis
- Blog generation
- Blog optimization
- Competitor content analysis
- Content quality analysis
- TXT export
- DOCX export
- Basic AI/API error handling
- Factual grounding rules

The prototype has been tested through an end-to-end blog generation and optimization workflow.

---

# Future Improvements

Possible future production improvements include:

- More advanced semantic retrieval
- Improved website crawling
- JavaScript-rendered website support
- Persistent vector databases
- More advanced content-quality evaluation
- Automated website monitoring
- User authentication
- Database integration
- Production deployment
- Monitoring and analytics
- Advanced AI evaluation
- More sophisticated content approval workflows

These are future enhancements and are not required for the current prototype.

---

# Project Status

Current Status: Functional Prototype

The current system is a working prototype demonstrating website analysis, company-information grounding, lightweight RAG retrieval, specialized AI content modules, content-quality analysis, and content export.

The prototype can be further extended for production requirements after additional validation, security, infrastructure, and scalability work.