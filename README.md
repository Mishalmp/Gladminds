
---

### Project Overview:

A project for product management using django restframework

### What I Did:

  
### How I Made It Happen:

- **Technology Used:** I used Django and Django REST Framework.
  
- **Testing and Notes:**
   - Checked everything was working using a tool called Postman.
   - Wrote down all the steps in a document so others can understand and use it later.

### What I Learned:

I found out a lot about how to make systems work better. I also learned new ways to secure systems and how to check if they're working well.







Installation process 



---

## Project Structure

The project is structured as follows:

- `backend/` - Django project folder
- `app/` - Django app for vendor management


## Setup Instructions

### 1. Create Virtual Environment

```
    python -m venv myvenv
```

### 2. Activate Virtual Environment

```
    myvenv\scripts\activate
```

### 3. Install Dependencies

Install required packages using pip:

```
    pip install django djangorestframework pillow
```

### 4. Create Django Project and App

```

    django-admin startproject backend
    django-admin startapp app
```

### 5. Configuration

#### Update `settings.py`

Add the following apps to `INSTALLED_APPS` in `backend/settings.py`:

```
    INSTALLED_APPS = [
        # ...
        'app',
        'rest_framework',

        # ...
    ]
```



### 6. URL Configuration
```
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryView,ProductView,SubcategoryView,ListSubcategoryView,ListProductView

router=DefaultRouter()
router.register('category',CategoryView)
router.register('subcategory',SubcategoryView)
router.register('product',ProductView)

urlpatterns = [
   path('',include(router.urls)),
   path('listproducts/',ListProductView.as_view()),
   path('listsubcategories/',ListSubcategoryView.as_view()),

   
]

```

### 7. Database Setup

Run Django migrations to set up the database:

```
    python manage.py makemigrations
    python manage.py migrate
```

### 8. Run Development Server

Start the development server:

```
    python manage.py runserver
```









