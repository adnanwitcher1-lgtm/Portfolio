# 🚀 Django Personal Portfolio Website

A professional, dynamic, and fully responsive portfolio website built using the **Django Web Framework**. This project allows developers to showcase their technical skills, projects, and experience with a sleek dark-theme UI.

---

## 🌟 Features

- **Dynamic Project Showcase:** Add, update, or remove projects directly from the Django Admin panel.
- **Project Links:** Integrated buttons for GitHub repository and Live demo links.
- **Responsive Design:** Built with **Bootstrap 5**, ensuring it looks great on desktops, tablets, and mobile phones.
- **Contact System:** A functional contact form that saves messages to the database for later review.
- **Profile Management:** Easily update profile pictures and personal details via the backend.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Icons:** Font Awesome 6
- **Database:** SQLite (can be migrated to PostgreSQL/MySQL)

---

## 🚀 Getting Started

To run this project locally, follow these steps:

### 1. Clone the repository
```bash
git clone [https://github.com/adnanwitcher1-lgtm/Portfolio.git](https://github.com/adnanwitcher1-lgtm/Portfolio.git)
cd Portfolio# Portfolio A dynamic and fully responsive Personal Portfolio Website built with Django and Python. It features a custom admin dashboard to manage projects, profile settings, and contact messages. Integrated with Bootstrap 5 for a sleek dark-themed UI and a functional contact form.
2. Set up a Virtual Environment
Bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Mac/Linux:
source venv/bin/activate
3. Install Dependencies
(Note: Create a requirements.txt if you haven't, or install manually)

Bash
pip install django pillow
4. Apply Migrations
Bash
python manage.py makemigrations
python manage.py migrate
5. Create a Superuser (Admin)
Bash
python manage.py createsuperuser
6. Run the Server
Bash
python manage.py runserver
