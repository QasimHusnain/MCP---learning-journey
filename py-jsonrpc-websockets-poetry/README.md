### README.md (for py-jsonrpc-websockets-poetry)
# py-jsonrpc-websockets-poetry

A **mini RPC framework** built with **Python**, **WebSockets**, and **JSON-RPC 2.0**, wrapped with **Poetry** for dependency management.

This project demonstrates how to build a simple **Remote Procedure Call (RPC)** system where a client can call server functions like `add`, `subtract`, or `multiply` over a WebSocket connection.

---

## 🚀 Features

- JSON-RPC 2.0 compliant request/response format  

- WebSocket-based real-time communication  

- Dictionary of methods auto-dispatches function calls  

- Error handling for unknown methods  

- Poetry-powered project setup and dependency management

---

## 📂 Project Structure

py-jsonrpc-websockets-poetry/

│

├── server.py # WebSocket JSON-RPC server

├── client.py # Client that sends RPC requests

├── pyproject.toml # Poetry project configuration

└── poetry.lock # Locked dependencies

yaml

Copy code

---

## ⚙️ Installation & Commands

```bash

git clone https://github.com/<your-username>/mcp-learning-journey.git   # clone repo to your computer

cd mcp-learning-journey/py-jsonrpc-websockets-poetry                   # go inside project folder

poetry install                                                          # install dependencies from pyproject.toml

poetry add websockets                                                   # add 'websockets' library into the project

▶️ Usage

bash

Copy code

poetry run python server.py   # start the WebSocket JSON-RPC server

                             # output: "RPC WebSocket Server running on ws://localhost:8700"

poetry run python client.py   # run client and send RPC requests to the server

                             # output: results of add, subtract, multiply + error for unknown method

🧠 How it Works

Server (server.py)

Keeps a dictionary of functions (add, subtract, multiply).

Listens for JSON messages over WebSockets.

Dispatches the request to the correct function and returns a JSON response.

Client (client.py)

Connects to the server over WebSockets.

Sends JSON-RPC formatted requests.

Prints the server's responses.

📖 Think of it like ordering food at a restaurant:

The client is you giving your order.

The server is the chef preparing the dish.

The menu is the dictionary of available functions (add, subtract, etc).

If you ask for something not on the menu (divide), you'll get an error.

🛠️ Tech Stack

Python 3.11+

WebSockets for real-time communication

JSON-RPC 2.0 for request/response structure

Poetry for dependency and environment management

📌 Next Steps

Add more RPC methods (e.g., divide, power, sqrt).

Implement authentication before allowing RPC calls.

Build a simple frontend to call RPC methods from a browser.

📝 License

This project is for educational purposes as part of my MCP learning journey.

pgsql

Copy code