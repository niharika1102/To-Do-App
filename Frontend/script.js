function createTodoElement(todo) {
  const completed = todo.completed
    ? "fa-solid fa-circle-check"
    : "fa-regular fa-circle";
  const textClass = todo.completed ? "todo-text completed-text" : "todo-text";

  const todoHTML = `
        <li class="todo-item" data-id="${todo.id}">
          <i class="${completed} check-icon"></i>
          <span class="${textClass}">${todo.title || todo.todo}</span>
          <i class="fas fa-edit edit-icon"></i>
          <i class="fas fa-trash delete-icon"></i>
        </li>
      `;

  const template = document.createElement("template");
  template.innerHTML = todoHTML.trim();
  const todoElement = template.content.firstElementChild;

  // Add event listeners
  todoElement.querySelector(".check-icon").onclick = function () {
    toggleTodo(todo.id, this);
  };

  todoElement.querySelector(".edit-icon").onclick = function () {
    updateTodo(todo.id, todoElement.querySelector(".todo-text"));
  };

  todoElement.querySelector(".delete-icon").onclick = function () {
    deleteTodo(todo.id);
  };

  return todoElement;
}

function addTodo() {
  const todoInput = document.getElementById("todo-input");
  const todoList = document.getElementById("todo-list");

  if (!todoInput || !todoInput.value.trim()) {
    alert("Please enter a task!");
    return;
  }

  fetch("http://localhost:8000/todos/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title: todoInput.value.trim(),
      completed: false,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      const newTodoElement = createTodoElement(data);
      todoList.appendChild(newTodoElement);
      todoInput.value = "";

      getTodos();
    })
    .catch((error) => console.error("Error:", error));
}

function getTodos() {
  fetch("http://localhost:8000/todos")
    .then((response) => response.json())
    .then((todos) => {
      const todoList = document.getElementById("todo-list");
      todoList.innerHTML = "";

      if (Array.isArray(todos) && todos.length > 0) {
        todos.forEach((todo) => {
          const todoElement = createTodoElement({
            id: todo.id,
            title: todo.title, // Make sure this matches your backend property name
            completed: todo.completed,
          });
          todoList.appendChild(todoElement);
        });
      } else {
        todoList.innerHTML = `
              <li class="error-message">
                All done for the day... Sit back and relax!
              </li>
            `;
      }
    })
    .catch((error) => {
      console.error("Error fetching todos:", error);
      alert("Failed to load todos");
    });
}

function toggleTodo(id, iconElement) {
  const todoText = iconElement.nextElementSibling;
  const currentState = iconElement.classList.contains("fa-solid");

  fetch(`http://localhost:8000/todos/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title: todoText.textContent, // Keep the existing title
      completed: !currentState, // Toggle the state
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      if (data.completed) {
        // Change to completed state
        iconElement.classList.remove("fa-regular", "fa-circle");
        iconElement.classList.add("fa-solid", "fa-circle-check");
        todoText.classList.add("completed-text");
      } else {
        // Change to uncompleted state
        iconElement.classList.remove("fa-solid", "fa-circle-check");
        iconElement.classList.add("fa-regular", "fa-circle");
        todoText.classList.remove("completed-text");
      }
    })
    .catch((error) => {
      console.error("Error toggling todo:", error);
      alert("Failed to update todo status. Please try again.");
    });
}

function deleteTodo(id) {
  fetch(`http://localhost:8000/todos/${id}`, {
    method: "DELETE",
  })
    .then((response) => response.json())
    .then((data) => {
      const todoList = document.getElementById("todo-list");
      todoList.removeChild(todoList.firstChild);
    })
    .catch((error) => console.error(error));
}

function updateTodo(id, todoTextElement) {
  const currentText = todoTextElement.textContent;
  const popup = document.getElementById("edit-popup");
  const input = document.getElementById("edit-todo-input");
  const saveBtn = document.getElementById("save-edit-btn");
  const cancelBtn = document.getElementById("cancel-edit-btn");

  // Show popup and set current value
  popup.style.display = "flex";
  input.value = currentText;
  input.focus();

  // Handle save
  const handleSave = () => {
    const newText = input.value;
    if (newText.trim() !== "" && newText !== currentText) {
      const todoItem = todoTextElement.closest(".todo-item");
      const isCompleted = todoItem
        .querySelector(".check-icon")
        .classList.contains("fa-circle-check");

      fetch(`http://localhost:8000/todos/${id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: newText.trim(),
          completed: isCompleted,
          id: id,
        }),
      })
        .then((response) => {
          if (!response.ok) {
            return response.json().then((error) => {
              throw new Error(error.detail || "Failed to update todo");
            });
          }
          return response.json();
        })
        .then((data) => {
          todoTextElement.textContent = data.title;
          console.log("Todo updated successfully:", data);
          closePopup();
        })
        .catch((error) => {
          console.error("Error updating todo:", error);
          alert("Failed to update todo: " + error.message);
        });
    } else {
      closePopup();
    }
  };

  // Handle close
  const closePopup = () => {
    popup.style.display = "none";
    input.value = "";
    // Remove event listeners
    saveBtn.removeEventListener("click", handleSave);
    cancelBtn.removeEventListener("click", closePopup);
    input.removeEventListener("keypress", handleKeyPress);
  };

  // Handle enter key
  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSave();
    }
  };

  // Add event listeners
  saveBtn.addEventListener("click", handleSave);
  cancelBtn.addEventListener("click", closePopup);
  input.addEventListener("keypress", handleKeyPress);
}

document.addEventListener("DOMContentLoaded", function () {
  getTodos();
});
