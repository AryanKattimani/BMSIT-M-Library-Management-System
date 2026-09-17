# Test checklist

## Static checks completed in this build environment

- Python modules compile with `py_compile`.
- SQLite schema is created by `connect()` on first app construction.
- Seed data contains the supplied 24 catalogue records, 9 users, 12 transactions, 4 recommendations, 5 notices, and 4 initial audit entries.
- Frontend source retains the supplied UI and routes; password demo literals were removed from the browser copy because authentication is now server-side.

## Windows acceptance test

1. Build both EXEs with `build.bat` on Windows.
2. Double-click `BMSIT-Library.exe`.
3. Verify browser opens automatically on an available localhost port.
4. Log in with each role.
5. Student: locator, borrowed books, renewal once, recommendation, profile, notifications.
6. Teacher: locator, issued books, recommendation, profile, notifications.
7. Librarian: inventory add/edit/deactivate, CSV import/export, issue, return, overdue, reminder, reports, recommendations.
8. Admin: users, role change, activation/deactivation, audit, settings, backup and restore.
9. Close and reopen the EXE; verify database state persists.
10. Create a backup and restore it on a fresh installation.
11. Run `BMSIT-Library-Server.exe`; connect from another LAN device using the displayed port and server IP.
12. Verify both devices see the same book/loan changes.
