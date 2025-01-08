# Task Manager

A simple command-line task management application written in Python that allows users to create, update, and track tasks with different statuses.

## Features

- Create new tasks with descriptions
- Update existing task descriptions
- Delete tasks
- Mark tasks as "In Progress" or "Done"
- List tasks filtered by status
- Persistent storage using JSON
- Track creation and update timestamps for each task

## Requirements

- Python 3.x
- No external dependencies required (uses only built-in Python libraries)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Ahmed-sa3ed/Task-Manager.git
cd task-manager
```

2. Run the application:
```bash
python task_manager.py
```

## Usage

The application supports the following commands:

- `add "Task description"` - Add a new task
- `update <id> "New description"` - Update task description
- `delete <id>` - Delete a task
- `mark-in-progress <id>` - Mark task as in progress
- `mark-done <id>` - Mark task as done
- `list [done|todo|in-progress]` - List tasks filtered by status
- `exit` - Exit the program

### Examples

```bash
# Add a new task
add "Complete the project documentation"

# Update task description
update <1> "Update the project documentation with new features"

# Mark task as in progress
mark-in-progress <1>

# Mark task as done
mark-done <1>

# List all todo tasks
list [todo]

# Delete a task
delete <1>
```

## Data Storage

Tasks are stored in a JSON file (`Tasks.json`) in the same directory as the script. The file is automatically created when the first task is added and updated with each modification.

## Task Properties

Each task contains the following information:
- ID: Unique identifier
- Description: Task description
- Status: Current status (Todo/In-progress/Done)
- CreatedAt: Timestamp when the task was created
- UpdatedAt: Timestamp when the task was last modified

## Error Handling

The application includes basic error handling for:
- Invalid command formats
- Non-existent task IDs
- Missing task descriptions
- Invalid status filters

## Contributing

Feel free to open issues or submit pull requests for any improvements or bug fixes.

## License

This project is open source and available under the [MIT License](LICENSE).
