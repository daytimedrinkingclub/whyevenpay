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
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   ├── static/
│   │   ├── css/
│   │   │   └── custom.css
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── base.html
│       └── index.html
│
├── migrations/
├── .env.template
├── venv/ # local virtual environment
├── config.py
├── requirements.txt
├── .gitignore
└── run.py
```