# ✅ CLI To-Do App

A lightweight, terminal-based task manager written in Python. Tasks persist across sessions using a local JSON file — no database, no dependencies, no fluff.

---

## Features

- 📋 List all tasks with completion status
- ➕ Add new tasks with automatic timestamps
- ✅ Mark tasks as complete
- 🗑️ Delete tasks with automatic ID re-indexing
- 💾 Auto-saves to `tasks.json` after every change

---

## Requirements

- Python 3.10+ (uses `match`/`case` syntax)

No external libraries required — only the standard library (`json`, `datetime`).

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**2. Run the app**
```bash
python todo.py
```

---

## Usage

```
A To-Do App
-------------------
1: list all tasks
2: add new tasks
3: mark as completed
4: delete task
5: exit
```

Select an option by entering its number and pressing Enter.

### Example session

```
select an option: 2
Enter a task: Buy groceries

select an option: 1
[1] Buy groceries — ❌

select an option: 3
[1] Buy groceries — ❌
enter task no. to mark complete: 1
[1] Buy groceries — ✅
```

---

## Data Storage

Tasks are saved to `tasks.json` in the project directory. Each task has the following structure:

```json
{
    "task_id": 1,
    "task_description": "Buy groceries",
    "added_on": "04/06/26 09:30:AM",
    "updated_on": "04/06/26 09:35:AM",
    "status": false
}
```

> `tasks.json` is auto-created on first use. You can add it to `.gitignore` if you don't want your tasks committed.

---
## Project Structure

```
.
├── todo.py        # Main application
├── tasks.json     # Auto-generated task storage (gitignore recommended)
└── README.md
```

---

## Known Limitations

- No `update task` feature yet (coming soon)
- Task IDs are position-based — deleting a task re-indexes everything
- No support for priorities, due dates, or categories

---

## License

MIT
