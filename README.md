# 🛍️ Django E-Commerce Web Application

A full-featured **E-Commerce web application** built with **Django**, providing product management, user authentication, and secure checkout.  
The app supports product images using **Pillow**, allowing admins to upload and manage product photos seamlessly.

---

## 🚀 Features

### 🧑‍💼 Admin Panel
- Add, update, or delete products.  
- Manage categories, users, and orders.  
- Upload product images using **Pillow**.  
- Dashboard for viewing sales, orders, and user activity.

### 🛒 Users
- Register, log in, and manage profiles with **Django Authentication**.  
- Browse products by category or search.  
- Add products to the cart and place orders securely.  
- View order history and track purchase status.  

### 💳 Cart & Checkout
- Persistent shopping cart linked to user session.  
- Order summary before checkout.  
- Supports multiple payment methods (can be extended).  

### 🖼️ Media & Images
- Uses **Pillow** to process and display product images.  
- Uploaded images stored in the `media/` directory.  

---

## 🧑‍💻 Tech Stack

- **Framework:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite / MySQL (configurable)  
- **Authentication:** Django’s built-in `auth` system  
- **Image Handling:** Pillow  
- **Deployment:** Gunicorn / Nginx (optional)
## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/django-ecommerce.git
cd django-ecommerce
### Create and activate a virtual environment
python -m venv env
source env/bin/activate  # for Linux/Mac
env\Scripts\activate

### Apply migrations
python manage.py makemigrations
python manage.py migrate

### Create a superuser
python manage.py createsuperuser

### Run the development server
python manage.py runserver
