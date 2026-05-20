## Correccion de la clave del admin en texto puro
Lo corregi y lo deje asi, deberia funcionar, verdad?
```py
def create_default_admin():
    admin = db.get_user_by_email("administrador@bionews.cl")
    if not admin:
        pwd = os.getenv("DEFAULT_ADMIN_PASSWORD")
        hashed_pw = hash_password(pwd)
        db.create_user("Administrador", "administrador@bionews.cl", hashed_pw, role="admin")
```