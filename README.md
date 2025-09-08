# Django REST Framework Blog API

A robust blog API built with Django REST Framework featuring OAuth2 authentication, image uploads, and comprehensive CRUD operations.

## Features

- **Blog Management**: Create, read, update, and delete blog posts
- **User Authentication**: OAuth2 with Google integration and custom user registration
- **Image Upload**: Support for post images with media handling
- **Search & Filtering**: Advanced search and filtering capabilities
- **API Documentation**: Swagger/ReDoc integration for API documentation
- **Custom Permissions**: Author-only edit permissions with flexible access control
- **Categories**: Organize posts with category management

## Tech Stack

- **Backend**: Django 5.2.6, Django REST Framework 3.16.1
- **Authentication**: OAuth2, Social Auth (Google)
- **Documentation**: drf-yasg (Swagger/OpenAPI)
- **Database**: SQLite (development)
- **Image Processing**: Pillow
- **Testing**: Django Test Framework with coverage

## Quick Start

1. **Clone the repository**
   ```bash
   git clone git@github.com:adityaxxz/BlogApp.git
   cd BlogApp
   ```
 > I've used uv which is rust-based and 100x faster than pip

2. **Set up virtual environment**
   ```bash
   pip install uv
   uv venv
   source .venv/bin/activate  # Linux
   .venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Blog Posts
- `GET /api/` - List all published posts
- `GET /api/posts/{slug}/` - Get specific post by slug
- `GET /api/search/` - Search posts `(use search/?search=)`
- `POST /api/admin/create/` - Create new post (authenticated)
- `PUT /api/admin/edit/{id}/` - Update post (authenticated)
- `DELETE /api/admin/delete/{id}/` - Delete post (authenticated)

### Authentication
- `POST /api/user/register/` - User registration
- `POST /auth/token/` - OAuth2 token endpoint

### Documentation
- `/swagger/` - Swagger UI
- `/redoc/` - ReDoc documentation

## Configuration

1. **OAuth2 Setup**: Configure Google OAuth2 credentials in `settings.py`
2. **Media Files**: Ensure media directory permissions for image uploads
3. **CORS**: Configure allowed origins for frontend integration

## Testing

```bash
python manage.py test
coverage run manage.py test
coverage html
```

## Project Structure

```
drf/
├── blog/          # Blog models and basic views
├── blog_api/      # REST API endpoints and serializers
├── users/         # Custom user model and authentication
├── core/          # Django settings and main URLs
├── media/         # Uploaded images
└── templates/     # HTML templates
```

## License

This project is open source and available under the [MIT License](LICENSE).
