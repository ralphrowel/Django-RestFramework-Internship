from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version="v1",
        description="""
        Authentication: Bearer <token>
        Base URL: http://127.0.0.1:8000/
        status codes: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found

        Run tests with: pytest lib/tests/test_tasks.py
        Reset DB: python manage.py flush && python manage.py migrate
        Create superuser: python manage.py createsuperuser
        Swagger UI at /swagger/
        ReDoc UI at /redoc/
        """,
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="ralphrowel00@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
