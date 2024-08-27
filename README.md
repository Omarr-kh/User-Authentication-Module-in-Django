# User-Authentication-Module-in-Django

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Omarr-kh/User-Authentication-Module-in-Django.git
   cd User-Authentication-Module-in-Django
2. **Install packages:**

    ```bash
    pip install -r requirements.txt
3. **Apply migration**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
4. **Run the development server**

    ```bash
    python manage.py runserver
5. **Open localhost**

    ```bash
    http://127.0.0.1:8000/

## Create a .env file at the root and fill these two variables 
```bash
  EMAIL_HOST_USER = 'your-email'
  EMAIL_HOST_PASSWORD = "your-password"
