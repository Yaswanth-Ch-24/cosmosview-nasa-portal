# CosmosView — NASA Astronomy Portal

> **Full Stack Web Application | Team Lead | 2025**  
> A fully documented web portal integrating multiple NASA APIs — APOD, Mars Rover, and more.

---

## 🔍 Project Overview

**CosmosView** is a full-stack web application that brings NASA's astronomy data to life. Built with Python and Django, it integrates multiple NASA public APIs to deliver astronomy photos, Mars rover imagery, and space exploration data — with date-range search and a personal Favorites module.

---

## ✨ Features

- 🌌 **APOD (Astronomy Picture of the Day)** — browse NASA's daily astronomy image with full explanation
- 🔴 **Mars Rover Photos** — explore images from Curiosity, Opportunity, and Spirit by date/camera
- 📅 **Date-range search** — filter content by custom date ranges
- ⭐ **Favorites module** — save and revisit your favourite space images
- 📱 **Responsive UI** — works on desktop and mobile
- 📖 **Fully documented** — API integration docs and setup guide included

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite (dev) / PostgreSQL (prod) |
| APIs | NASA APOD API, NASA Mars Rover Photos API |
| Auth | Django session-based authentication |
| Deployment | (Render / Railway / PythonAnywhere) |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- NASA API Key (free at [api.nasa.gov](https://api.nasa.gov))

### Installation

```bash
git clone https://github.com/Yaswanth-Ch-24/cosmosview.git
cd cosmosview
pip install -r requirements.txt
```

### Configuration

```bash
# Create .env file
echo "NASA_API_KEY=your_api_key_here" > .env
echo "SECRET_KEY=your_django_secret_key" >> .env
```

### Run

```bash
python manage.py migrate
python manage.py runserver
# Visit http://localhost:8000
```

---

## 📁 Repository Structure

```
cosmosview/
├── cosmosview/             # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apod/                   # APOD app
│   ├── views.py
│   ├── models.py
│   └── templates/
├── mars_rover/             # Mars Rover app
│   ├── views.py
│   └── templates/
├── favorites/              # Favorites module
│   ├── models.py
│   └── views.py
├── static/                 # CSS, JS, images
├── templates/              # Base templates
├── requirements.txt
└── README.md
```

---

## 🔗 NASA APIs Used

### APOD — Astronomy Picture of the Day
```
GET https://api.nasa.gov/planetary/apod?api_key=KEY&date=YYYY-MM-DD
```

### Mars Rover Photos
```
GET https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=YYYY-MM-DD&api_key=KEY
```

---

## 📸 Screenshots

> Add screenshots of your app here after deployment

---

## 👤 Author

**Chlliboina Yaswanth**  
B.Tech Electrical & Electronics Engineering  
Dr. Lankapalli Bullayya College of Engineering, Visakhapatnam  
📧 yaswanth2452005@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/yaswanth-chlliboina/)

---

## 📄 License

MIT License — free to use and modify with attribution.
