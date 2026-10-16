# Trimly ✂️ | Full-Stack URL Shortener

![Trimly Logo](./frontend/public/logo.jpg)

Trimly is a modern, high-performance URL shortener built with a decoupled architecture. It features a React-based frontend for a seamless user experience, powered by a robust Django REST API backend and a PostgreSQL database.

**Live Frontend:** [https://trimly-ui.vercel.app](https://trimly-ui.vercel.app)  
**Live API Endpoint:** `https://trimly-backend-w8ge.onrender.com/api/`

---

## ✨ Features
- **Instant URL Shortening:** Convert long, bulky URLs into clean, shareable Trimly links.
- **QR Code Generation:** Automatically generates a scannable QR code for every shortened link.
- **Click Analytics:** Built-in tracking system to monitor how many times a destination URL has been visited.
- **Decoupled Architecture:** Frontend and backend are completely separated, communicating securely via RESTful API endpoints and strict CORS policies.
- **Fully Responsive UI:** A minimalist, aesthetic interface optimized for both desktop and mobile devices.

---

## 🛠️ Tech Stack
**Frontend:**
- React (Vite)
- CSS3 / Flexbox
- Hosted on Vercel

**Backend:**
- Python / Django REST Framework
- PostgreSQL Database
- Gunicorn (WSGI HTTP Server)
- Hosted on Render

---

## 🚀 Local Setup & Installation

If you'd like to run Trimly on your local machine, follow these steps:

### 1. Clone the repository
```bash
git clone [https://github.com/obasi-1/trimly.git](https://github.com/obasi-1/trimly.git)
cd trimly