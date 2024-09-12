# Scrum Backend Project

## Project Description
Dieses Projekt ist ein Backend für ein Scrum-Management-System, das mit Django entwickelt wurde. Es ermöglicht die Verwaltung von Aufgaben, Kontakten und Benutzern innerhalb eines Scrum-Teams.

## Features
- Benutzerregistrierung und -authentifizierung (mit CustomUser)
- Verwaltung von Aufgaben mit Status (ToDo, In Progress, Done)
- Zuweisung von Kontakten zu Aufgaben
- Aufgabenreihenfolge festlegen und verzögerte Aufgaben markieren

## Installation

### Voraussetzungen
- Python 3.x
- Django
- Git

### Setup Schritte
1. Klone das Repository:
    ```bash
    git clone https://github.com/Seldir193/scrum-backend.git
    ```

2. Wechsle ins Projektverzeichnis:
    ```bash
    cd dein-repository
    ```

3. Erstelle und aktiviere ein virtuelles Environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Für Mac/Linux
    .\venv\Scripts\activate   # Für Windows
    ```

4. Installiere die benötigten Pakete:
    ```bash
    pip install -r requirements.txt
    ```

5. Führe die Datenbankmigrationen durch:
    ```bash
    python manage.py migrate
    ```

6. Starte den lokalen Server:
    ```bash
    python manage.py runserver
    ```

## Usage
Nachdem der Server gestartet wurde, kannst du auf das Admin-Panel unter `http://127.0.0.1:8000/admin/` zugreifen.

## Contribution
Beiträge sind willkommen! Erstelle einen Fork des Projekts, führe Änderungen durch und erstelle einen Pull Request.

## License
Dieses Projekt ist lizenziert unter der MIT License - siehe die [LICENSE](LICENSE) Datei für Details.
