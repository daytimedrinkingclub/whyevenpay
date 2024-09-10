# Whyevenpay

- A listing directory for AI tools

## Logic

- Why pay 
  - For each tool we will understand why should we pay
- When to pay 
  - For each tool we will understand when to pay
- Why not pay
  - For each tool we will understand why not to pay

## Tech Stack

- Python flask and jinja2
- Tailwind CSS
- HTML
- Javascript
- Supabase Database
- Flask forms for tool submission form


### Folder Structure
```bash
freeaifinder/
│
├── app/
│   ├── __init__.py # app initialization
│   ├── routes.py # routes for the app
│   ├── data_service.py # data service for the app
│   ├── forms.py # forms for the app
│   ├── static/ # static files for the app
│   │   ├── css/ # css files for the app
│   │   │   └── custom.css # custom css for the app
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── base.html # base template for all pages
│       ├── about.html # about page
│       ├── index.html # home page
│       ├── submission.html # submission page
│       └── tool_details.html # tool details page
│
├── .env.template
├── venv/ # local virtual environment
├── config.py
├── requirements.txt
├── .gitignore
└── run.py
```