📌 README.md (for websocket_demo_project)
# Poetry-based WebSocket Demo Project


This is a simple **Python WebSocket demo** using [asyncio](https://docs.python.org/3/library/asyncio.html) and the [websockets](https://websockets.readthedocs.io/) library.  
It demonstrates how a client and server establish a **WebSocket handshake** and then exchange messages.

---

## 🔹 Key Concepts
- **Handshake**: Client requests an HTTP `Upgrade`, server responds, and the connection switches to WebSocket.
- **Full-duplex**: After handshake, both client and server can send/receive messages anytime.
- **Data types**: WebSockets can carry strings, JSON, XML, or even binary data.

---

## 🔹 Project Setup
This is a **Poetry-based project**.  
Dependencies are defined in `pyproject.toml`.  
Main libraries used:
- `websockets` (for WebSocket protocol)
- `asyncio` (for async event loop, built into Python)

---

## 🔹 Project Structure


websocket_demo_project/
│
├── websocket-demo/
│ ├── server.py # WebSocket server
│ ├── client.py # WebSocket client
│ └── init.py
│
├── pyproject.toml # Poetry config
└── README.md


---

## 🔹 Run the Demo

### Start the server
```bash
poetry run python websocket-demo/server.py

Start the client (new terminal)
poetry run python websocket-demo/client.py

🔹 Example Flow
   [Client]                                [Server]
      |                                        |
      | --- HTTP Upgrade Request ------------> |
      | <--- 101 Switching Protocols --------- |   (Handshake ✅)
      |                                        |
      | ---- "Hello Server!" ----------------> |
      | <--- "Server received: Hello Server!"- |
      |                                        |