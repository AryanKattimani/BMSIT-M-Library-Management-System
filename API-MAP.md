# Frontend → Backend integration map

The supplied frontend's existing views and interactions are preserved. The following data-changing functions now call Flask instead of mutating only browser memory.

| Existing frontend action | Backend endpoint |
|---|---|
| `doLogin` | `POST /api/auth/login` |
| `doLogout` | `POST /api/auth/logout` |
| `fgSend` | `POST /api/auth/forgot-password` |
| `fgFinish` | `POST /api/auth/reset-password` |
| `renewTxn`, `renewTxnB` | `POST /api/loans/:id/renew` |
| `submitRec` | `POST /api/recommendations` |
| `markNotice`, `markAllNotices` | `PATCH /api/notifications/:id/read` |
| `saveProf`, phone update | `PATCH /api/users/:id` |
| `invSave` | `POST /api/books` / `PATCH /api/books/:id` |
| `invDelete` | `DELETE /api/books/:id` |
| `invImport` | `POST /api/import/inventory` |
| `issueConfirm` | `POST /api/loans` |
| `doReturn` | `POST /api/loans/:id/return` |
| `sendReminder` | `POST /api/loans/:id/remind` |
| `repAct` | `PATCH /api/recommendations/:id` |
| `toggleActive`, `confirmRole` | `PATCH /api/users/:id` |
| `setFlag` | `PATCH /api/settings` |
| `doBackup` | `GET /api/backup` |
| `doRestore` | `POST /api/restore` |
| CSV exports | `GET /api/export/*` |

## Read-side synchronization

After authentication and after each mutating operation, the frontend calls `GET /api/bootstrap`. That response repopulates the existing `S.users`, `S.books`, `S.txns`, `S.recs`, `S.notices`, `S.audits`, and `S.flags` structures used by the existing rendering code.

This keeps the existing view/render code intact while moving persistence and authorization to Flask.

## Existing frontend business rules retained

- Student loan duration: 14 days.
- Student overdue fine: ₹1/day.
- Teacher/faculty loans have no due date and no due-date fine.
- Student renewal is allowed once and extends the due date by 14 days.
- Inventory uses racks 1–67 and sections A–F.
- Return condition supports normal, damaged, and lost handling.
- Fine waiver requires a documented reason.
