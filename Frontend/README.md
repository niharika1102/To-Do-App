# To-do Application Frontend

A clean and modern To-do application built with vanilla JavaScript, HTML, and CSS. This frontend interfaces with a REST API backend to provide a complete task management solution.

## Features

- Create new todos
- Mark todos as complete/incomplete
- Edit existing todos
- Delete todos
- Responsive design
- Modern UI with animations
- Popup modal for editing todos

## Technologies Used

- HTML5
- CSS3
- Vanilla JavaScript
- Font Awesome Icons
- Google Fonts (Rubik)

## Project Structure

- `index.html`: The main HTML file that includes the structure of the application.
- `style.css`: The CSS file that styles the application.
- `script.js`: The JavaScript file that handles the application logic.

## Setup and Installation

1. Clone the repository
2. Ensure the backend server is running on `http://localhost:8000`
3. Open `index.html` in a web browser

## API Integration

The frontend communicates with the backend through the following endpoints:

- `GET /todos` - Fetch all todos
- `POST /todos` - Create a new todo
- `PUT /todos/{id}` - Update a todo
- `DELETE /todos/{id}` - Delete a todo

## UI Components

### Main Components
- Header with title
- Todo input field with add button
- Todo list container
- Edit popup

### Todo Item Features
- Checkbox for completion status
- Todo text
- Edit button
- Delete button

### Styling Features
- Soft color palette
- Rounded corners
- Hover effects
- Smooth transitions
- Responsive design

## Usage

1. **Adding a Todo**
   - Type your todo in the input field
   - Click "Add"

2. **Completing a Todo**
   - Click the circle icon next to the todo

3. **Editing a Todo**
   - Click the edit (pencil) icon
   - Modify the text in the popup
   - Click "Save"

4. **Deleting a Todo**
   - Click the trash icon

## Browser Support

The application is compatible with modern browsers including:
- Chrome
- Firefox
- Safari
- Edge