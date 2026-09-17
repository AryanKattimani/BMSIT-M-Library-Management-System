# BMSIT Library — Flask + SQLite

This project wraps the supplied `bmsit-library final frontend.html` in a local Flask REST API and SQLite database. The visual frontend is retained; its demo/in-memory mutations are replaced with API-backed persistence.

The supplied frontend already defines four role portals, the 67-rack A–F locator, 14-day student borrowing, ₹1/day student overdue fines, recommendations, notices, reports, audit views, user/role management, settings, and backup/restore. fileciteturn0file0L109-L186

## End user — Windows

### Personal / demo mode

1. Download `BMSIT-Library.exe`.
2. Double-click it.
3. Wait for the browser to open.
4. Log in.

No Python, Node.js, npm, SQLite, PostgreSQL, MySQL, MongoDB, Docker, Redis, or command prompt is required.

The live database is stored under `%APPDATA%\BMSIT-Library\bmsit_library.db` so it survives application updates.

### Library server mode

1. Run `BMSIT-Library-Server.exe` on one Windows computer.
2. Allow the Windows Firewall prompt for private/local networks if Windows asks.
3. The server computer can use the browser URL shown by the application.
4. Other devices on the same LAN open `http://SERVER-IP:PORT`.

All devices then use the same SQLite database on the server computer.

SQLite is appropriate for this deployment when the library is using one server process with network clients. It is not a substitute for a high-scale multi-server database cluster.

## Seed accounts

These are seeded from the supplied demo frontend, but passwords are stored only as secure hashes in SQLite.

| Role | ID | Password |
|---|---|---|
| Student | `10241` | `student123` |
| Student | `10242` | `student123` |
| Student | `10243` | `student123` |
| Student | `10244` | `student123` |
| Student | `10245` | `student123` |
| Teacher | `EMP201` | `teacher123` |
| Teacher | `EMP202` | `teacher123` |
| Librarian | `LIB01` | `library123` |
| Admin | `DEV01` | `dev123` |

Change production passwords immediately.

## Developer setup

1. Install Python 3.11+.
2. Open this project directory.
3. Create a virtual environment:

```bat
python -m venv .venv
.venv\Scripts\activate
```

4. Install dependencies:

```bat
python -m pip install -r requirements.txt
```

5. Run personal mode:

```bat
python launcher.py
```

6. Run LAN server mode:

```bat
python launcher.py --server
```

The database is created automatically on first launch.

## Build the Windows executables

On a Windows development machine with Python installed:

```bat
build.bat
```

This creates:

- `dist\BMSIT-Library.exe`
- `dist\BMSIT-Library-Server.exe`

PyInstaller bundles the Python runtime and Python dependencies into the executable. SQLite is provided by Python's standard library, so no SQLite installation is needed.

## API overview

Authentication:

- `POST /api/auth/login`
- `POST /api/auth/logout`
- `GET /api/auth/me`
- `POST /api/auth/forgot-password`
- `POST /api/auth/reset-password`

Books:

- `GET /api/books`
- `GET /api/books/:id`
- `POST /api/books`
- `PATCH /api/books/:id`
- `DELETE /api/books/:id`

Loans:

- `GET /api/loans`
- `GET /api/loans/:id`
- `POST /api/loans`
- `POST /api/loans/:id/return`
- `POST /api/loans/:id/renew`
- `POST /api/loans/:id/remind`

Recommendations:

- `GET /api/recommendations`
- `POST /api/recommendations`
- `PATCH /api/recommendations/:id`

Notifications:

- `GET /api/notifications`
- `PATCH /api/notifications/:id/read`
- `POST /api/notifications`

Users/admin:

- `GET /api/users`
- `POST /api/users`
- `PATCH /api/users/:id`
- `GET /api/settings`
- `PATCH /api/settings`

Inventory:

- `POST /api/import/inventory`
- `GET /api/export/inventory`
- `GET /api/export/borrowers`
- `GET /api/export/users`
- `GET /api/export/recommendations`
- `GET /api/export/circulation`
- `GET /api/export/overdue`

Backup:

- `GET /api/backup`
- `POST /api/restore`

## Security notes

- Passwords are hashed with Werkzeug's password hashing utilities.
- Session cookies are HttpOnly and SameSite=Lax.
- Role authorization is enforced in Flask; frontend role checks are not trusted.
- Audit entries are created server-side for authentication, inventory, circulation, recommendation, user, settings, backup, restore, and notification operations.
- The backup format is portable JSON and includes password hashes because a true restore must preserve user credentials. Normal API responses never return password hashes.
- Password reset codes are generated server-side. Because this is a self-contained local application without an email/SMS provider, the demo UI displays the verification code rather than sending an external message.

## Frontend preservation

`frontend/bmsit-library.html` is the supplied frontend with only its data-mutating JavaScript redirected to the local Flask API. The existing layout, colors, typography, navigation, cards, dashboards, forms, buttons, modals, dark mode, responsive structure, and role portals are not redesigned.
