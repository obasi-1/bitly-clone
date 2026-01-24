#  Bitly Clone API

A robust URL shortener service built with **Django** and **Django REST Framework**. 
This project features a collision-proof shortening algorithm, click analytics, and a fully documented REST API.

##  Key Features
- **URL Shortening Algorithm:** Generates unique 6-character codes.
- **Click Analytics:** Tracks visits using database-level `F()` expressions for race-condition safety.
- **REST API:** Full JSON endpoints for integration with other apps.
- **Auto-Documentation:** Interactive API docs via Swagger/OpenAPI.
- **Frontend UI:** A clean landing page for quick manual shortening.

##  Tech Stack
- **Backend:** Python, Django 5.x
- **API:** Django REST Framework (DRF)
- **Database:** SQLite (Dev)
- **Docs:** drf-yasg (Swagger)

##  How to Run

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/bitly-clone.git](https://github.com/YOUR_USERNAME/bitly-clone.git)
   cd bitly-clone