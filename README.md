## Language
<details>
<summary> English </summary>

# DnD Card Vault

**DnD Card Vault** is a Django web application for creating and storing a collection of items related to Dungeons & Dragons. Users can add, view, edit and delete entries.

*Some file and class names were retained from earlier versions of the application.*

---

## Main features

**Item collection**
* Create and browse collection entries.
* Edit and delete entries.
* View detailed information about an entry.
* Add a description, rating, tags and an image.

**Entry types**
* `card` - card; `item` - item; `character` - character; `magic` - magic.

**Filtering and sorting**
* Filter by type or minimum rating.
* Sort by name or year and choose the sort order.

**User accounts**
* Registration, sign-in and sign-out.
* Django's built-in authentication system.
* Restrict certain actions for unauthenticated users.

**API**
* Retrieve entries in JSON format.
* Create, update and delete entries through the API.
* Transfer data without HTML pages.

<details>
<summary> Project structure </summary>

* `manage.py` - runs Django management commands.
* `db.sqlite3` - SQLite database.
* `task_tracking/` - project settings and main URLs.
* `tasks/` - application logic: models, forms, views and routes.
* `templates/` - HTML page templates.
* `static/tasks/css/style.css` - interface styles.
* `media/covers/` - uploaded entry images.
* `tasks/migrations/` - database schema migrations.
* `.venv/` - local Python virtual environment.
</details>
<details>
<summary> Main files </summary>

**`task_tracking/settings.py`** - Django settings for applications, templates, database and static files; uses SQLite and has development `DEBUG` mode enabled.

**`task_tracking/urls.py`** - connects the Django administration panel and the `tasks` application routes.

**`tasks/models.py`** - defines the model used to store collection items; its name does not fully match the current project theme.

**`tasks/forms.py`** - creates a model-based form, with field labels and rating validation.

**`tasks/views.py`** - handles requests and implements list, detail, create, update and delete pages; also contains registration, authentication and JSON API handlers.

**`tasks/urls.py`** - maps application URLs to handlers.

**`tasks/admin.py`** - registers models with Django administration.

**`tasks/tests.py`** - file for automated application tests.
</details>
<details>
<summary> Templates and interface </summary>

* `templates/base.html` - shared page layout.
* `templates/tasks/book_list.html` - entry list.
* `templates/tasks/book_detail.html` - entry details.
* `templates/tasks/book_form.html` - entry form.
* `templates/tasks/book_confirm_delete.html` - deletion confirmation.
* `templates/auth/login.html` - sign-in page.
* `templates/auth/register.html` - registration page.
* `static/tasks/css/style.css` - page styling.

The project also contains `task_list.html`, `task_detail.html`, `task_create.html`, `task_update.html` and `task_delete.html`. These belong to an earlier task-manager version and may not be used by the current interface.
</details>

## Technologies

* **Backend:** Python and Django.
* **Frontend:** HTML and CSS.
* **CSS framework:** Bootstrap 5.3.8 via CDN.
* **Database:** SQLite.
* **Templates:** Django Template Language.
* **Authentication:** `django.contrib.auth` and Django sessions.
* **Version control:** Git.

---

## Demo

<details>
<summary> Home page </summary>
<img width="960" height="305" alt="1" src="https://github.com/user-attachments/assets/cb43ecf6-8779-40f6-af01-693b6d027b95" />
</details>
<details>
<summary> Registration / sign-in </summary>
<img width="213" height="140" alt="4" src="https://github.com/user-attachments/assets/b1f2781f-f67a-4c4b-9cc0-c4ac82ecad1c" />
<img width="271" height="311" alt="3" src="https://github.com/user-attachments/assets/4e320bf7-b106-473a-a7b1-a31a506f083c" />
</details>
<details>
<summary> Add a card </summary>
<img width="323.5" height="401" alt="2" src="https://github.com/user-attachments/assets/1ba24bf5-dafa-43cf-8111-ffeffacaf57c" />
</details>

## Running the project

1. Install Python.
2. Create and activate a virtual environment.
3. Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

5. Apply migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in a browser.
</details>

<details>
<summary> Ukrainian/Українська </summary>

# DnD Card Vault

**DnD Card Vault** - вебзастосунок на Django для створення та зберігання колекції об'єктів, пов'язаних із Dungeons & Dragons. Користувач може додавати записи, переглядати їх, редагувати та видаляти.

*Назви деяких файлів і класів залишилися від попередніх версій застосунку.*

---

## Основні можливості

**Колекція об'єктів**
* Створення та перегляд записів колекції.
* Редагування та видалення записів.
* Перегляд детальної інформації про запис.
* Додавання опису, рейтингу, тегів і зображення.

**Типи записів**
* `card` - картка; `item` - предмет; `character` - персонаж; `magic` - магія.

**Фільтрація та сортування**
* Фільтрація за типом або мінімальним рейтингом.
* Сортування за назвою або роком і вибір напрямку сортування.

**Облікові записи**
* Реєстрація, вхід і вихід з облікового запису.
* Вбудована система автентифікації Django.
* Обмеження доступу неавторизованих користувачів до окремих дій.

**API**
* Отримання записів у форматі JSON.
* Створення, зміна та видалення записів через API.
* Передавання даних без HTML-сторінок.

<details>
<summary> Структура проєкту </summary>

* `manage.py` - запуск команд керування Django.
* `db.sqlite3` - база даних SQLite.
* `task_tracking/` - налаштування та основні URL-адреси проєкту.
* `tasks/` - логіка застосунку: моделі, форми, обробники та маршрути.
* `templates/` - HTML-шаблони сторінок.
* `static/tasks/css/style.css` - стилі інтерфейсу.
* `media/covers/` - завантажені зображення записів.
* `tasks/migrations/` - міграції структури бази даних.
* `.venv/` - локальне віртуальне середовище Python.
</details>
<details>
<summary> Основні файли </summary>

**`task_tracking/settings.py`** - налаштування Django, застосунків, шаблонів, бази даних і статичних файлів; використовується SQLite та ввімкнено режим `DEBUG` для розробки.

**`task_tracking/urls.py`** - підключає адміністративну панель Django та маршрути застосунку `tasks`.

**`tasks/models.py`** - визначає модель зберігання об'єктів колекції; її назва не повністю відповідає поточній тематиці проєкту.

**`tasks/forms.py`** - створює форму на основі моделі, містить підписи полів і перевірку рейтингу.

**`tasks/views.py`** - обробляє запити та реалізує сторінки списку, перегляду, створення, зміни й видалення; також містить реєстрацію, автентифікацію та обробники JSON API.

**`tasks/urls.py`** - пов'язує URL-адреси з обробниками застосунку.

**`tasks/admin.py`** - підключає моделі до адміністративної панелі Django.

**`tasks/tests.py`** - файл автоматичних тестів застосунку.
</details>
<details>
<summary> Шаблони та інтерфейс </summary>

* `templates/base.html` - спільна основа сторінок.
* `templates/tasks/book_list.html` - список записів.
* `templates/tasks/book_detail.html` - детальна сторінка запису.
* `templates/tasks/book_form.html` - форма запису.
* `templates/tasks/book_confirm_delete.html` - підтвердження видалення.
* `templates/auth/login.html` - сторінка входу.
* `templates/auth/register.html` - сторінка реєстрації.
* `static/tasks/css/style.css` - оформлення сторінок.

Також є `task_list.html`, `task_detail.html`, `task_create.html`, `task_update.html` і `task_delete.html`. Вони належать до попередньої версії менеджера завдань і можуть не використовуватися поточним інтерфейсом.
</details>

## Технології

* **Backend:** Python і Django.
* **Frontend:** HTML і CSS.
* **CSS-фреймворк:** Bootstrap 5.3.8 через CDN.
* **База даних:** SQLite.
* **Шаблони:** Django Template Language.
* **Автентифікація:** `django.contrib.auth` і сесії Django.
* **Контроль версій:** Git.

---

## Демонстрація

<details>
<summary> Головна сторінка </summary>
<img width="960" height="305" alt="1" src="https://github.com/user-attachments/assets/cb43ecf6-8779-40f6-af01-693b6d027b95" />
</details>
<details>
<summary> Реєстрація / вхід </summary>
<img width="213" height="140" alt="4" src="https://github.com/user-attachments/assets/b1f2781f-f67a-4c4b-9cc0-c4ac82ecad1c" />
<img width="271" height="311" alt="3" src="https://github.com/user-attachments/assets/4e320bf7-b106-473a-a7b1-a31a506f083c" />
</details>
<details>
<summary> Додавання картки </summary>
<img width="323.5" height="401" alt="2" src="https://github.com/user-attachments/assets/1ba24bf5-dafa-43cf-8111-ffeffacaf57c" />
</details>

## Запуск проєкту

1. Встановити Python.
2. Створити й активувати віртуальне середовище.
3. Встановити залежності з `requirements.txt`:

```bash
pip install -r requirements.txt
```

5. Виконати міграції та запустити сервер:

```bash
python manage.py migrate
python manage.py runserver
```

Після цього відкрити в браузері `http://127.0.0.1:8000/`.
</details>

<details>
<summary> Rusian/Русский </summary>

# DnD Card Vault

**DnD Card Vault** - веб-приложение на Django для создания и хранения коллекции объектов, связанных с Dungeons & Dragons. Пользователь может добавлять записи, просматривать их, изменять и удалять.

*Названия некоторых файлов и классов остались от предыдущих версий приложения.

---

## Основные возможности

**Коллекция объектов**
* Создание и просмотр записей коллекции.
* Редактирование и удаление записей.
* Просмотр подробной информации об отдельной записи.
* Добавление описания, рейтинга, тегов и изображения.

**Типы записей**
* `card` - карта.
* `item` - предмет.
* `character` - персонаж.
* `magic` - магия.

**Фильтрация и сортировка**
* Фильтрация записей по типу.
* Фильтрация по минимальному рейтингу.
* Сортировка по названию или году.
* Выбор направления сортировки.

**Учётные записи**
* Регистрация пользователя.
* Вход и выход из аккаунта.
* Использование встроенной системы авторизации Django.
* Ограничение доступа к отдельным действиям для неавторизованных пользователей.

**API**
* Получение записей в формате JSON.
* Создание, изменение и удаление записей через API.
* Передача данных без использования HTML-страниц.

<details>
<summary> Структура проекта </summary>

* `manage.py` - запуск команд управления Django.
* `db.sqlite3` - база данных SQLite.
* `task_tracking/` - настройки и основные URL проекта.
* `tasks/` - логика приложения: модели, формы, обработчики и маршруты.
* `templates/` - HTML-шаблоны страниц.
* `static/tasks/css/style.css` - стили интерфейса.
* `media/covers/` - загруженные изображения записей.
* `tasks/migrations/` - миграции структуры базы данных.
* `.venv/` - локальное виртуальное окружение Python.
</details>
<details>
<summary> Основные файлы </summary>

**`task_tracking/settings.py`**
* Содержит настройки Django, приложений, шаблонов, базы данных и статических файлов.
* Используется SQLite.
* В настройках включён режим `DEBUG`, предназначенный для разработки.

**`task_tracking/urls.py`**
* Подключает административную панель Django.
* Подключает маршруты приложения `tasks`.

**`tasks/models.py`**
* Определяет модель используемую для хранения объектов коллекции.
* Название модели не полностью соответствует текущей тематике проекта.

**`tasks/forms.py`**
* Создаёт форму на основе модели.
* Содержит подписи полей и проверку рейтинга.

**`tasks/views.py`**
* Обрабатывает запросы пользователей.
* Реализует страницы списка, просмотра, создания, изменения и удаления записей.
* Содержит функции регистрации и авторизации, а также обработчики JSON API.

**`tasks/urls.py`**
* Связывает URL-адреса с обработчиками приложения.

**`tasks/admin.py`**
* Настраивает подключение моделей к административной панели Django.

**`tasks/tests.py`**
* Файл для автоматических тестов приложения.
</details>
<details>
<summary> Шаблоны и интерфейс </summary>

* `templates/base.html` - общий каркас страниц.
* `templates/tasks/book_list.html` - список записей.
* `templates/tasks/book_detail.html` - подробная страница записи.
* `templates/tasks/book_form.html` - форма записи.
* `templates/tasks/book_confirm_delete.html` - подтверждение удаления.
* `templates/auth/login.html` - страница входа.
* `templates/auth/register.html` - страница регистрации.
* `static/tasks/css/style.css` - оформление страниц.

В проекте также присутствуют шаблоны `task_list.html`, `task_detail.html`, `task_create.html`, `task_update.html` и `task_delete.html`. Они относятся к прежнему варианту менеджера задач и могут не использоваться текущей версией интерфейса.
</details>

## Технологии

* **Backend:** Python и Django.
* **Frontend:** HTML и CSS.
* **CSS-фреймворк:** Bootstrap 5.3.8 через CDN.
* **База данных:** SQLite.
* **Шаблоны:** Django Template Language.
* **Авторизация:** `django.contrib.auth` и сессии Django.
* **Контроль версий:** Git.

---

## Демонстрация 

<details>
<summary> главная страница </summary>
<img width="960" height="305" alt="1" src="https://github.com/user-attachments/assets/cb43ecf6-8779-40f6-af01-693b6d027b95" />
</details>

<details>
<summary> регистрация/вход </summary>
<img width="213" height="140" alt="4" src="https://github.com/user-attachments/assets/b1f2781f-f67a-4c4b-9cc0-c4ac82ecad1c" />
<img width="271" height="311" alt="3" src="https://github.com/user-attachments/assets/4e320bf7-b106-473a-a7b1-a31a506f083c" />
</details>

<details>
<summary> добавить карточку </summary>
<img width="323.5" height="401" alt="2" src="https://github.com/user-attachments/assets/1ba24bf5-dafa-43cf-8111-ffeffacaf57c" />
</details>

## Запуск проекта

1. Установить Python.
2. Создать и активировать виртуальное окружение.
3. Установить зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

5. Выполнить миграции и запустить сервер:

```bash
python manage.py migrate
python manage.py runserver
```

Затем открыть в браузере `http://127.0.0.1:8000/`.
</details>

<details>
<summary> German/Deutsch </summary>

# DnD Card Vault

**DnD Card Vault** ist eine Django-Webanwendung zum Erstellen und Speichern einer Sammlung von Objekten aus dem Umfeld von Dungeons & Dragons. Benutzer können Einträge hinzufügen, ansehen, bearbeiten und löschen.

*Einige Datei- und Klassennamen stammen noch aus früheren Versionen der Anwendung.*

---

## Hauptfunktionen

**Objektsammlung**
* Einträge erstellen und anzeigen, bearbeiten und löschen.
* Detaillierte Informationen zu einzelnen Einträgen anzeigen.
* Beschreibung, Bewertung, Tags und Bild hinzufügen.

**Eintragstypen**
* `card` - Karte; `item` - Gegenstand; `character` - Charakter; `magic` - Magie.

**Filtern und Sortieren**
* Nach Typ oder Mindestbewertung filtern.
* Nach Name oder Jahr sortieren und die Sortierrichtung wählen.

**Benutzerkonten**
* Registrierung, An- und Abmeldung.
* Integriertes Django-Authentifizierungssystem.
* Bestimmte Aktionen für nicht angemeldete Benutzer beschränken.

**API**
* Einträge im JSON-Format abrufen.
* Einträge über die API erstellen, ändern und löschen.
* Daten ohne HTML-Seiten übertragen.

<details>
<summary> Projektstruktur </summary>

* `manage.py` - führt Django-Verwaltungsbefehle aus.
* `db.sqlite3` - SQLite-Datenbank.
* `task_tracking/` - Projekteinstellungen und zentrale URLs.
* `tasks/` - Anwendungslogik: Modelle, Formulare, Ansichten und Routen.
* `templates/` - HTML-Seitenvorlagen.
* `static/tasks/css/style.css` - Oberflächenstile.
* `media/covers/` - hochgeladene Bilder.
* `tasks/migrations/` - Datenbankmigrationen.
* `.venv/` - lokale virtuelle Python-Umgebung.
</details>
<details>
<summary> Wichtige Dateien </summary>

**`task_tracking/settings.py`** - Django-Einstellungen für Anwendungen, Vorlagen, Datenbank und statische Dateien; SQLite wird verwendet und der Entwicklungsmodus `DEBUG` ist aktiviert.

**`task_tracking/urls.py`** - bindet die Django-Administration und die Routen von `tasks` ein.

**`tasks/models.py`** - definiert das Speichermodell für Sammlungsobjekte; der Name passt nicht vollständig zum aktuellen Projektthema.

**`tasks/forms.py`** - erstellt ein modellbasiertes Formular mit Feldbeschriftungen und Bewertungsprüfung.

**`tasks/views.py`** - verarbeitet Anfragen und implementiert Listen-, Detail-, Erstellungs-, Änderungs- und Löschseiten sowie Registrierung, Authentifizierung und JSON-API-Handler.

**`tasks/urls.py`** - ordnet URLs den Anwendungs-Handlern zu.

**`tasks/admin.py`** - bindet Modelle in die Django-Administration ein.

**`tasks/tests.py`** - Datei für automatisierte Anwendungstests.
</details>
<details>
<summary> Vorlagen und Benutzeroberfläche </summary>

* `templates/base.html` - gemeinsames Seitengerüst.
* `templates/tasks/book_list.html` - Eintragsliste.
* `templates/tasks/book_detail.html` - Detailseite eines Eintrags.
* `templates/tasks/book_form.html` - Eintragsformular.
* `templates/tasks/book_confirm_delete.html` - Löschbestätigung.
* `templates/auth/login.html` - Anmeldeseite.
* `templates/auth/register.html` - Registrierungsseite.
* `static/tasks/css/style.css` - Seitengestaltung.

Außerdem gibt es `task_list.html`, `task_detail.html`, `task_create.html`, `task_update.html` und `task_delete.html`. Diese Vorlagen gehören zu einer früheren Version des Aufgabenmanagers und werden möglicherweise nicht mehr verwendet.
</details>

## Technologien

* **Backend:** Python und Django.
* **Frontend:** HTML und CSS.
* **CSS-Framework:** Bootstrap 5.3.8 über CDN.
* **Datenbank:** SQLite.
* **Vorlagen:** Django Template Language.
* **Authentifizierung:** `django.contrib.auth` und Django-Sitzungen.
* **Versionsverwaltung:** Git.

---

## Demo

<details>
<summary> Startseite </summary>
<img width="960" height="305" alt="1" src="https://github.com/user-attachments/assets/cb43ecf6-8779-40f6-af01-693b6d027b95" />
</details>
<details>
<summary> Registrierung / Anmeldung </summary>
<img width="213" height="140" alt="4" src="https://github.com/user-attachments/assets/b1f2781f-f67a-4c4b-9cc0-c4ac82ecad1c" />
<img width="271" height="311" alt="3" src="https://github.com/user-attachments/assets/4e320bf7-b106-473a-a7b1-a31a506f083c" />
</details>
<details>
<summary> Karte hinzufügen </summary>
<img width="323.5" height="401" alt="2" src="https://github.com/user-attachments/assets/1ba24bf5-dafa-43cf-8111-ffeffacaf57c" />
</details>

## Projekt starten

1. Python installieren.
2. Eine virtuelle Umgebung erstellen und aktivieren.
3. Abhängigkeiten aus `requirements.txt` installieren:

```bash
pip install -r requirements.txt
```

5. Migrationen ausführen und den Server starten:

```bash
python manage.py migrate
python manage.py runserver
```

Anschließend `http://127.0.0.1:8000/` im Browser öffnen.
</details>

<details>
<summary> French/Français </summary>

# DnD Card Vault

**DnD Card Vault** est une application web Django permettant de créer et de conserver une collection d'objets liés à Dungeons & Dragons. L'utilisateur peut ajouter, consulter, modifier et supprimer des entrées.

*Certains noms de fichiers et de classes proviennent des versions précédentes de l'application.*

---

## Fonctionnalités principales

**Collection d'objets**
* Créer et consulter les entrées, les modifier et les supprimer.
* Afficher les informations détaillées d'une entrée.
* Ajouter une description, une note, des tags et une image.

**Types d'entrées**
* `card` - carte ; `item` - objet ; `character` - personnage ; `magic` - magie.

**Filtrage et tri**
* Filtrer par type ou par note minimale.
* Trier par nom ou par année et choisir le sens du tri.

**Comptes utilisateurs**
* Inscription, connexion et déconnexion.
* Système d'authentification intégré de Django.
* Limitation de certaines actions aux utilisateurs authentifiés.

**API**
* Récupérer les entrées au format JSON.
* Créer, modifier et supprimer des entrées via l'API.
* Transmettre des données sans pages HTML.

<details>
<summary> Structure du projet </summary>

* `manage.py` - exécute les commandes de gestion de Django.
* `db.sqlite3` - base de données SQLite.
* `task_tracking/` - paramètres du projet et URL principales.
* `tasks/` - logique de l'application : modèles, formulaires, vues et routes.
* `templates/` - modèles de pages HTML.
* `static/tasks/css/style.css` - styles de l'interface.
* `media/covers/` - images téléversées.
* `tasks/migrations/` - migrations de la base de données.
* `.venv/` - environnement virtuel Python local.
</details>
<details>
<summary> Fichiers principaux </summary>

**`task_tracking/settings.py`** - paramètres Django des applications, modèles, base de données et fichiers statiques ; SQLite est utilisé et le mode de développement `DEBUG` est activé.

**`task_tracking/urls.py`** - connecte l'administration Django et les routes de `tasks`.

**`tasks/models.py`** - définit le modèle de stockage des objets de la collection ; son nom ne correspond pas entièrement au thème actuel.

**`tasks/forms.py`** - crée un formulaire basé sur le modèle, avec les libellés et la validation de la note.

**`tasks/views.py`** - traite les requêtes et gère les pages de liste, détail, création, modification et suppression, ainsi que l'inscription, l'authentification et l'API JSON.

**`tasks/urls.py`** - associe les URL aux gestionnaires de l'application.

**`tasks/admin.py`** - configure les modèles dans l'administration Django.

**`tasks/tests.py`** - fichier des tests automatisés de l'application.
</details>
<details>
<summary> Modèles et interface </summary>

* `templates/base.html` - structure commune des pages.
* `templates/tasks/book_list.html` - liste des entrées.
* `templates/tasks/book_detail.html` - détails d'une entrée.
* `templates/tasks/book_form.html` - formulaire d'entrée.
* `templates/tasks/book_confirm_delete.html` - confirmation de suppression.
* `templates/auth/login.html` - page de connexion.
* `templates/auth/register.html` - page d'inscription.
* `static/tasks/css/style.css` - présentation des pages.

Le projet contient aussi `task_list.html`, `task_detail.html`, `task_create.html`, `task_update.html` et `task_delete.html`. Ces modèles appartiennent à une ancienne version du gestionnaire de tâches et peuvent ne plus être utilisés.
</details>

## Technologies

* **Backend :** Python et Django.
* **Frontend :** HTML et CSS.
* **Framework CSS :** Bootstrap 5.3.8 via CDN.
* **Base de données :** SQLite.
* **Modèles :** Django Template Language.
* **Authentification :** `django.contrib.auth` et sessions Django.
* **Gestion de versions :** Git.

---

## Démonstration

<details>
<summary> Page d'accueil </summary>
<img width="960" height="305" alt="1" src="https://github.com/user-attachments/assets/cb43ecf6-8779-40f6-af01-693b6d027b95" />
</details>
<details>
<summary> Inscription / connexion </summary>
<img width="213" height="140" alt="4" src="https://github.com/user-attachments/assets/b1f2781f-f67a-4c4b-9cc0-c4ac82ecad1c" />
<img width="271" height="311" alt="3" src="https://github.com/user-attachments/assets/4e320bf7-b106-473a-a7b1-a31a506f083c" />
</details>
<details>
<summary> Ajouter une carte </summary>
<img width="323.5" height="401" alt="2" src="https://github.com/user-attachments/assets/1ba24bf5-dafa-43cf-8111-ffeffacaf57c" />
</details>

## Lancer le projet

1. Installer Python.
2. Créer et activer un environnement virtuel.
3. Installer les dépendances depuis `requirements.txt` :

```bash
pip install -r requirements.txt
```

5. Exécuter les migrations et démarrer le serveur :

```bash
python manage.py migrate
python manage.py runserver
```

Ouvrir ensuite `http://127.0.0.1:8000/` dans un navigateur.
</details>

<details>
<summary> Polish/Polski </summary>

# DnD Card Vault

**DnD Card Vault** to aplikacja internetowa oparta na Django, służąca do tworzenia i przechowywania kolekcji obiektów związanych z Dungeons & Dragons. Użytkownik może dodawać wpisy, przeglądać je, edytować i usuwać.

*Nazwy niektórych plików i klas pochodzą z wcześniejszych wersji aplikacji.*

---

## Główne funkcje

**Kolekcja obiektów**
* Tworzenie, przeglądanie, edytowanie i usuwanie wpisów.
* Wyświetlanie szczegółowych informacji o wpisie.
* Dodawanie opisu, oceny, tagów i obrazu.

**Typy wpisów**
* `card` - karta; `item` - przedmiot; `character` - postać; `magic` - magia.

**Filtrowanie i sortowanie**
* Filtrowanie według typu lub minimalnej oceny.
* Sortowanie według nazwy lub roku oraz wybór kierunku sortowania.

**Konta użytkowników**
* Rejestracja, logowanie i wylogowanie.
* Wbudowany system uwierzytelniania Django.
* Ograniczenie wybranych działań dla niezalogowanych użytkowników.

**API**
* Pobieranie wpisów w formacie JSON.
* Tworzenie, modyfikowanie i usuwanie wpisów przez API.
* Przesyłanie danych bez stron HTML.

<details>
<summary> Struktura projektu </summary>

* `manage.py` - uruchamia polecenia zarządzające Django.
* `db.sqlite3` - baza danych SQLite.
* `task_tracking/` - ustawienia projektu i główne adresy URL.
* `tasks/` - logika aplikacji: modele, formularze, widoki i trasy.
* `templates/` - szablony stron HTML.
* `static/tasks/css/style.css` - style interfejsu.
* `media/covers/` - przesłane obrazy wpisów.
* `tasks/migrations/` - migracje struktury bazy danych.
* `.venv/` - lokalne wirtualne środowisko Pythona.
</details>
<details>
<summary> Główne pliki </summary>

**`task_tracking/settings.py`** - ustawienia Django dotyczące aplikacji, szablonów, bazy danych i plików statycznych; używana jest SQLite, a tryb `DEBUG` jest włączony na potrzeby programowania.

**`task_tracking/urls.py`** - podłącza panel administracyjny Django i trasy aplikacji `tasks`.

**`tasks/models.py`** - definiuje model przechowywania obiektów kolekcji; jego nazwa nie odpowiada w pełni obecnej tematyce projektu.

**`tasks/forms.py`** - tworzy formularz na podstawie modelu, zawiera etykiety pól i walidację oceny.

**`tasks/views.py`** - obsługuje żądania i strony listy, szczegółów, tworzenia, edycji oraz usuwania; zawiera też rejestrację, uwierzytelnianie i obsługę JSON API.

**`tasks/urls.py`** - łączy adresy URL z funkcjami obsługi aplikacji.

**`tasks/admin.py`** - konfiguruje modele w panelu administracyjnym Django.

**`tasks/tests.py`** - plik z automatycznymi testami aplikacji.
</details>
<details>
<summary> Szablony i interfejs </summary>

* `templates/base.html` - wspólny układ stron.
* `templates/tasks/book_list.html` - lista wpisów.
* `templates/tasks/book_detail.html` - strona ze szczegółami wpisu.
* `templates/tasks/book_form.html` - formularz wpisu.
* `templates/tasks/book_confirm_delete.html` - potwierdzenie usunięcia.
* `templates/auth/login.html` - strona logowania.
* `templates/auth/register.html` - strona rejestracji.
* `static/tasks/css/style.css` - wygląd stron.

Projekt zawiera również `task_list.html`, `task_detail.html`, `task_create.html`, `task_update.html` i `task_delete.html`. Pochodzą one ze starszej wersji menedżera zadań i mogą nie być używane przez obecny interfejs.
</details>

## Technologie

* **Backend:** Python i Django.
* **Frontend:** HTML i CSS.
* **Framework CSS:** Bootstrap 5.3.8 przez CDN.
* **Baza danych:** SQLite.
* **Szablony:** Django Template Language.
* **Uwierzytelnianie:** `django.contrib.auth` i sesje Django.
* **Kontrola wersji:** Git.

---

## Prezentacja

<details>
<summary> Strona główna </summary>
<img width="960" height="305" alt="1" src="https://github.com/user-attachments/assets/cb43ecf6-8779-40f6-af01-693b6d027b95" />
</details>
<details>
<summary> Rejestracja / logowanie </summary>
<img width="213" height="140" alt="4" src="https://github.com/user-attachments/assets/b1f2781f-f67a-4c4b-9cc0-c4ac82ecad1c" />
<img width="271" height="311" alt="3" src="https://github.com/user-attachments/assets/4e320bf7-b106-473a-a7b1-a31a506f083c" />
</details>
<details>
<summary> Dodawanie karty </summary>
<img width="323.5" height="401" alt="2" src="https://github.com/user-attachments/assets/1ba24bf5-dafa-43cf-8111-ffeffacaf57c" />
</details>

## Uruchamianie projektu

1. Zainstalować Pythona.
2. Utworzyć i aktywować środowisko wirtualne.
3. Zainstalować zależności z pliku `requirements.txt`:

```bash
pip install -r requirements.txt
```

5. Wykonać migracje i uruchomić serwer:

```bash
python manage.py migrate
python manage.py runserver
```

Następnie otworzyć w przeglądarce adres `http://127.0.0.1:8000/`.
</details>

<details>
<summary> Spanish/Español </summary>

# DnD Card Vault

**DnD Card Vault** es una aplicación web desarrollada con Django para crear y almacenar una colección de objetos relacionados con Dungeons & Dragons. El usuario puede añadir registros, consultarlos, modificarlos y eliminarlos.

*Algunos nombres de archivos y clases se conservaron de versiones anteriores de la aplicación.*

---

## Funciones principales

**Colección de objetos**
* Crear, consultar, editar y eliminar registros.
* Consultar información detallada de cada registro.
* Añadir una descripción, una valoración, etiquetas y una imagen.

**Tipos de registros**
* `card` - carta; `item` - objeto; `character` - personaje; `magic` - magia.

**Filtrado y ordenación**
* Filtrar por tipo o valoración mínima.
* Ordenar por nombre o año y elegir el sentido del orden.

**Cuentas de usuario**
* Registro, inicio y cierre de sesión.
* Sistema de autenticación integrado de Django.
* Restringir determinadas acciones a usuarios autenticados.

**API**
* Obtener registros en formato JSON.
* Crear, modificar y eliminar registros mediante la API.
* Transferir datos sin páginas HTML.

<details>
<summary> Estructura del proyecto </summary>

* `manage.py` - ejecuta los comandos de administración de Django.
* `db.sqlite3` - base de datos SQLite.
* `task_tracking/` - configuración y URL principales del proyecto.
* `tasks/` - lógica de la aplicación: modelos, formularios, vistas y rutas.
* `templates/` - plantillas de páginas HTML.
* `static/tasks/css/style.css` - estilos de la interfaz.
* `media/covers/` - imágenes cargadas de los registros.
* `tasks/migrations/` - migraciones de la base de datos.
* `.venv/` - entorno virtual local de Python.
</details>
<details>
<summary> Archivos principales </summary>

**`task_tracking/settings.py`** - configuración de Django para aplicaciones, plantillas, base de datos y archivos estáticos; utiliza SQLite y tiene activado `DEBUG` para desarrollo.

**`task_tracking/urls.py`** - conecta el panel de administración de Django e incluye las rutas de `tasks`.

**`tasks/models.py`** - define el modelo utilizado para almacenar los objetos de la colección; su nombre no coincide completamente con el tema actual.

**`tasks/forms.py`** - crea un formulario basado en el modelo, con etiquetas de campos y validación de la valoración.

**`tasks/views.py`** - procesa solicitudes e implementa páginas de lista, detalle, creación, modificación y eliminación; también incluye registro, autenticación y controladores de JSON API.

**`tasks/urls.py`** - vincula las URL con los controladores de la aplicación.

**`tasks/admin.py`** - configura los modelos en el panel de administración de Django.

**`tasks/tests.py`** - archivo para las pruebas automatizadas de la aplicación.
</details>
<details>
<summary> Plantillas e interfaz </summary>

* `templates/base.html` - estructura común de las páginas.
* `templates/tasks/book_list.html` - lista de registros.
* `templates/tasks/book_detail.html` - página de detalles de un registro.
* `templates/tasks/book_form.html` - formulario del registro.
* `templates/tasks/book_confirm_delete.html` - confirmación de eliminación.
* `templates/auth/login.html` - página de inicio de sesión.
* `templates/auth/register.html` - página de registro.
* `static/tasks/css/style.css` - diseño de las páginas.

El proyecto también contiene `task_list.html`, `task_detail.html`, `task_create.html`, `task_update.html` y `task_delete.html`. Pertenecen a una versión anterior del gestor de tareas y es posible que la interfaz actual no los utilice.
</details>

## Tecnologías

* **Backend:** Python y Django.
* **Frontend:** HTML y CSS.
* **Framework CSS:** Bootstrap 5.3.8 mediante CDN.
* **Base de datos:** SQLite.
* **Plantillas:** Django Template Language.
* **Autenticación:** `django.contrib.auth` y sesiones de Django.
* **Control de versiones:** Git.

---

## Demostración

<details>
<summary> Página principal </summary>
<img width="960" height="305" alt="1" src="https://github.com/user-attachments/assets/cb43ecf6-8779-40f6-af01-693b6d027b95" />
</details>
<details>
<summary> Registro / inicio de sesión </summary>
<img width="213" height="140" alt="4" src="https://github.com/user-attachments/assets/b1f2781f-f67a-4c4b-9cc0-c4ac82ecad1c" />
<img width="271" height="311" alt="3" src="https://github.com/user-attachments/assets/4e320bf7-b106-473a-a7b1-a31a506f083c" />
</details>
<details>
<summary> Añadir una tarjeta </summary>
<img width="323.5" height="401" alt="2" src="https://github.com/user-attachments/assets/1ba24bf5-dafa-43cf-8111-ffeffacaf57c" />
</details>

## Ejecutar el proyecto

1. Instalar Python.
2. Crear y activar un entorno virtual.
3. Instalar las dependencias de `requirements.txt`:

```bash
pip install -r requirements.txt
```

5. Ejecutar las migraciones e iniciar el servidor:

```bash
python manage.py migrate
python manage.py runserver
```

Después, abrir `http://127.0.0.1:8000/` en el navegador.
python manage.py runserver
</details>

</details>
