# Django REST Framework Authentication Setup

This document explains the setup for token-based authentication in a Django REST Framework (DRF) project and how to test it effectively.

---

## Authentication Setup

### 1. Install Required Packages
Ensure you have installed the required packages:

pip install djangorestframework djangorestframework-simplejwt

 ## 2 Update INSTALLED_APPS
Add the following to the INSTALLED_APPS section of your settings.py:
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]

## 3. Configure REST Framework
Update the REST_FRAMEWORK settings in your settings.py:
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

## 4. Migrate Changes
Run migrations to apply the authentication setup:
python manage.py migrate

## 5. Generate Tokens for Users
You can generate a token for a user in the Django shell:
python manage.py drf_create_token <username>
This will return a token for the specified user.

### Testing the API
1. Start the Development Server
Run the Django development server:
python manage.py runserver


## 2. Test Authentication
Use tools like Postman, cURL, or a browser extension (e.g., RESTClient) to test the API.

Example with cURL:
Replace <TOKEN> with the token generated earlier.
curl -H "Authorization: Token <TOKEN>" http://127.0.0.1:8000/api/protected-resource/

## Example with Postman:
Open Postman.
Enter the API endpoint URL: http://127.0.0.1:8000/api/protected-resource/.
Go to the Headers tab and add:
Key: Authorization
Value: Token <your_generated_token>
Send the request.

