.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requierements.txt
relfex init
reflex export --frontend-only
rmdir /s /q public
powershell -command "Expand-Archive -Path 'C:\Users\Sotog\OneDrive\Escritorio\Ejemplo 2\Ejemplo_2\frontend.zip' -DestinationPath 'C:\Users\Sotog\OneDrive\Escritorio\Ejemplo 2\Ejemplo_2\public'"
del -f frontend.zip
deactivate