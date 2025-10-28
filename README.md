# Weather-Tourism-App-Using-Django

🌦️ Weather and Tourism App using Django

🧭 “Discover weather, explore places — plan smarter with my Django project.”

This project is a Weather and Tourism App Using Django built completely using Django and command-line setup.
It shows real-time weather updates and tourist places around your chosen city or location.
Users can select their favorite destinations and get a ready-made travel itinerary — all in one place.

---
<img width="520" height="500" alt="image" src="https://github.com/user-attachments/assets/f5c7530a-839f-413e-9dc0-3d23f6a696db" />
<img width="520" height="500" alt="image" src="https://github.com/Users/yamun/OneDrive/Pictures/Screenshots/Screenshot(171).png"/>
<img width="520" height="500" alt="image" src="https://github.com/user-attachments/assets/f5c7530a-839f-413e-9dc0-3d23f6a696db" />
💪 My Effort & Motivation

I built this project from scratch using command prompt, without using any automatic project generators or templates.
I practiced all key steps manually:

* Creating and linking Django apps
* Connecting APIs
* Designing templates
* Configuring URLs and views
* Testing the project from the terminal

This helped me understand how Django works internally and improved my full-stack development skills.

---

⚙️ Features

✅ Real-Time Weather Info and Temperature — fetches live weather details using the OpenWeatherMap API
✅ Tourist Places Around You — displays beautiful destinations with images
✅ Local time — Displays current date and time in a clear format
✅ country flag— The app displays the country flag based on the user’s selected city or current location.
✅ Responsive UI — built using HTML, CSS for better experience

---

🛠️ Technologies Used

| Part       | Technology                        |
| ---------- | --------------------------------- |
| Backend    | Django (Python)                   |
| Frontend   | HTML, CSS,                        |
| Database   | SQLite                            |
| API        | OpenWeatherMap (for weather data) |
| Tools Used | Command Prompt, VS Code           |

---

🧩 Project Structure


amma/
│
├── manage.py
├── weather_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── weather/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── templates/weather.html
│
├── weather_project/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── templates/tourism/
│       ├── places.html
│       └── itinerary.html
│
└── static/
    ├── css/
    ├── Html
    

---

⚡ Setup and Run (Command Prompt Steps)

1️⃣ Create and Activate Virtual Environment

cmd
python -m venv venv
venv\Scripts\activate
----
2️⃣ Install Django

cmd
pip install django

---
3️⃣ Create Django Project & Apps (done manually)

cmd
django-admin startproject weather_tourism_project
cd weather_tourism_project
python manage.py startapp weather
python manage.py startapp tourism

---
4️⃣ Apply Migrations

bash
python manage.py makemigrations
python manage.py migrate

---

5️⃣ Run the Development Server

bash
python manage.py runserver

---

6️⃣ View in Browser

Visit 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

🔑 API Setup

* Go to [https://openweathermap.org/api](https://openweathermap.org/api)
* Create an account and get your **API key**
* Add it in your Django settings file like this:

python
WEATHER_API_KEY = "your_api_key_here"

📸 Screenshots (Optional Section)
|![Wether details and tourism places]("C:\Users\yamun\OneDrive\Pictures\Screenshots\Screenshot (170).png") | 
![]("C:\Users\yamun\OneDrive\Pictures\Screenshots\Screenshot (171).png") |
![]("C:\Users\yamun\OneDrive\Pictures\Screenshots\Screenshot (172).png") |

---

🧠 What I Learned

* Complete Django project flow (apps, templates, URLs, models, views)
* Handling API data in Python
* How to structure multi-app Django projects
* Debugging and running apps via command prompt
* Building a real-world, data-driven web app

---

Developed By
Yamuna
🌍 Python & Django Developer
💼 [LinkedIn Profile](https://www.linkedin.com/in/yamunamca/)]| 🐙 [GitHub Profile]((https://github.com/yamunaraguthu))

---
 🪪 License

This project is open-source and available under the **MIT License**.
Feel free to use or modify it for learning and development purposes.

---
