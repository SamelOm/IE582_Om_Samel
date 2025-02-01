# IE582_Om_Samel_50610520
For the Coursework and Notes
## Description of the first 2 classes
Steps: 
1. We intall all the necessary tools, those are Node.js and Python
2. For nodejs, we intsall it from nodejs webiste, and once it has downloaded, we can check the version or verify if its downloaded we can open terminal and type: "node -v"
3. and now we have to change the directory to wherever we have stored our git repo(simple_socket_browser file) , by doing : cd "the path to the folder"
4. and then type this command: "node server_secure.cjs --public" ;  this will have our server running
5. and on a seperate shell window, do Step 3 and the this command: "python3 client.py"
6. What this will do is that Python Websocket client will be connected and the server will be have a session id : my sid is nt_nBlMwWm8JAVzxAAAA
7. Then we can launch this website on our browser :  https://localhost:8080/index.html this website will have a few buttons, and functionalty of those buttons will be given by JS code
8. the client can give directional commads and write a text message on the front end and it will show in the nodejs shell window as : "direction
[ 'left' ]" and in the python window as : "I received this direction message: left"
**what i didnt understand was how we connected our phones and interacted with the system**
Now the System:


# Real-Time WebSocket Communication System

This of a **Node.js WebSocket server**, a **Python client**, and a **Front-End interface** that communicate in real time using **Socket.IO**. The system processes chat messages and direction commands.

## Features
- Real-time bi-directional communication between the front-end and Python client via Node.js server.
- WebSockets for efficient message exchange.
- Graceful shutdown handling in Python.


---

## 🚀 How to Run the System

### **1️⃣ Start the Node.js WebSocket Server**
```bash
cd server
node server.js
```
This starts an HTTPS server and WebSocket service on `localhost:8080`.

### **2️⃣ Start the Python Client**
```bash
cd client
python3 client.py
```
This connects to the WebSocket server and listens for messages.

### **3️⃣ Start the Front-End (Optional)**
You can use a simple front-end with Socket.IO to send and receive messages:
```html
<script src="https://cdn.socket.io/4.0.1/socket.io.js"></script>
<script>
    var socket = io('https://localhost:8080');
    socket.emit('chat', { data: 'Hello' });
    socket.on('reply', (data) => { console.log('Reply received:', data); });
</script>
```

---

## 🛠️ System Architecture

```plaintext
[Front-End]  →  [Node.js Server]  →  [Python Client]
    ▲                ▼                    ▼
    └──────────── Message Flow ───────────┘
```

| Component | File | Responsibility |
|-----------|------|----------------|
| **WebSocket Server** | `server.js` | Handles WebSocket connections & message forwarding |
| **Python Client** | `client.py` | Processes chat/direction messages & replies |
| **Front-End** | `index.html` (optional) | Sends/receives messages via WebSockets |

---

## 🔄 Execution Order
1. **Start the WebSocket Server (`server.js`)** → Listens for WebSocket connections.
2. **Run the Python Client (`client.py`)** → Connects to the server, listens for events.
3. **Send a message from the Front-End** → The server forwards it to the Python client.
4. **Python client processes and replies** → The server relays the reply back to the front-end.

---

## 📝 WebSocket Event Flow
| Event | Sender | Receiver | Description |
|-------|--------|----------|-------------|
| `chat` | Front-End | Python Client | Sends a chat message |
| `direction` | Front-End | Python Client | Sends a movement command |
| `reply` | Python Client | Front-End | Sends a response |
| `disconnect` | Server | Python/Client | Handles disconnections |

---

## ✅ Graceful Shutdown Handling (Python)
- The Python client ensures a **graceful exit** when terminated (`SIGINT/SIGTERM`).
- Uses the `GracefulShutdown` class to **clean up resources** before exiting.

---

## 🔧 Dependencies
### **Node.js Server**
```bash
npm install express socket.io https fs yargs
```

### **Python Client**
```bash
pip install socketio
```

---

## 📌 Future Enhancements
- [ ] Add **authentication** for secure access.
- [ ] Implement **database storage** for message logs.
- [ ] Improve **error handling** for edge cases.

---

## 📜 License
This project is open-source and free to use under the MIT License.

---

## 💬 Questions?
Feel free to reach out if you need any help! 🚀
