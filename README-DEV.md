# Generar Archivo para Subir a PIP

```bash
pip install build --break-system-packages
python -m build
```

Se creara un tar.gz con el archivo para subir a PIP.

# Sube el paquete a PyPI con Twine

```bash
twine upload dist/*
```

🔐 La primera vez te pedirá usuario y contraseña de PyPI (no GitHub, sino la cuenta que creaste en https://pypi.org).

✅ Si todo va bien, verás un mensaje como:

```bash
Uploading distributions to https://upload.pypi.org/legacy/
Uploading mi_paquete-0.1.0-py3-none-any.whl
...
View at:
https://pypi.org/project/mi-paquete/
```


## 🧼 Buenas prácticas
Usa nombres únicos para tu paquete (puedes comprobar disponibilidad en https://pypi.org/search).

Cambia el número de versión cada vez que subas (PyPI no permite sobrescribir versiones).

Documenta bien en README.md.


## ⚠️ ¿Errores comunes?
❌ File already exists → cambia el número de versión en setup.py.

❌ 403 Forbidden → credenciales mal o no verificaste tu email.

❌ long_description mal → asegúrate de que README.md está en markdown y bien referenciado en setup.py.



## Correr los TEST

```commandline
pip install -e . --break-system-packages
```

```bash
python tests/test_chirpstack_api.py
```