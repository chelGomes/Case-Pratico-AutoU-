# Email Classification Application

## Overview
This is a Flask-based web application that automatically classifies emails as "Produtivo" (Productive) or "Não Produtivo" (Not Productive) based on their content. The app analyzes text input or uploaded files (.txt or .pdf) and provides suggested responses.

## Project Structure
```
projeto_email/
├── app.py                 # Main Flask application
├── static/               # Static assets (CSS, JS)
│   ├── script.js         # Frontend JavaScript
│   └── style.css         # Custom styles
└── templates/            # HTML templates
    └── index.html        # Main application interface
```

## Technology Stack
- **Backend**: Flask (Python 3.12)
- **File Processing**: PyPDF2 for PDF text extraction
- **Frontend**: Bootstrap 5, vanilla JavaScript
- **Production Server**: Gunicorn

## Dependencies
- flask
- pypdf2
- gunicorn

## How It Works
1. User inputs email content via text area or uploads a file (.txt or .pdf)
2. The `/analyze` endpoint processes the content
3. Classification logic checks for keywords ("trabalho", "projeto")
4. Returns category and suggested response as JSON
5. Frontend displays results with color-coded alerts

## Development
- Dev server runs on `0.0.0.0:5000`
- Configured for Replit environment with proper host settings
- Debug mode enabled in development

## Deployment
- Deployment type: Autoscale
- Production server: Gunicorn
- Command: `gunicorn --bind=0.0.0.0:5000 --reuse-port projeto_email.app:app`

## Recent Changes
- **2025-10-01**: Initial Replit setup
  - Installed Flask and PyPDF2 dependencies
  - Configured Flask to run on 0.0.0.0:5000 for Replit
  - Fixed static files folder structure
  - Configured workflow for development
  - Set up Gunicorn for production deployment
