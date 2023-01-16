# Curso Django

Una especie de copia de instagram, solo subiendo posts y manejando usuarios

Este repositorio es lo trabajado durante el curso de django de platzi

## Comandos
```bash
> python3 -m venv venv
> source venv/bin/activat
> pip install -r requirements.txt
> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
> python manage.py shell
```

Estando en la shell interactiva de django:

```python
from django.contrig.auth.models import User
from users.models import Profile

u = User.object.get(id=1)
p = Profile.object.create(u)
```

Al final se ejecuta el servidoc común y corriente
```bash
> python manage.py runserver
```
