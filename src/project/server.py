"""
Server Between the Board and Controller
"""


import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Enable CORS so the separate HTML pages can connect cleanly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Stores active WebSocket connections by their role
active_connections: dict[str, set[WebSocket]] = {
    "controller": set(),
    "board": set()
}

# Declare Base Directory
BASE_DIR = Path(__file__).resolve().parent

# Game Launcher HTML page
@app.get("/")
async def get_index():
    return HTMLResponse(content="""
        <h1>Tetris Game Launcher</h1>
        <ul>
            <li><a href="/board" target="_blank">Open Game Board Window</a></li>
            <li><a href="/controller" target="_blank">Open Controller Window</a></li>
        </ul>
    """, status_code=200)

# Board HTML page
@app.get("/board")
async def get_board():
    with open(BASE_DIR / "board.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

# Controller HTML page
@app.get("/controller")
async def get_controller():
    with open(BASE_DIR / "controller.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

# connect Websocket and add to active_connections
async def connect_client(websocket: WebSocket, role: str):
    await websocket.accept()
    if role in active_connections:
        active_connections[role].add(websocket)
        print(f"Client connected as: {role} (Total: {len(active_connections[role])})")

# remove Websocket from active_connections
def disconnect_client(websocket: WebSocket, role: str):
    if role in active_connections and websocket in active_connections[role]:
        active_connections[role].remove(websocket)
        print(f"Client disconnected from: {role}")

# Sends message to active_boards and removes inactive ones
async def broadcast_to_boards(message: str):
    disconnected_boards = set()
    for board in active_connections["board"]:
        try:
            await board.send_text(message)
        except Exception:
            disconnected_boards.add(board)

    for dead_board in disconnected_boards:
        active_connections["board"].remove(dead_board)

# Accepts websocket connections and routes messages from controllers to
# boards using helper functions
@app.websocket("/ws/{role}")
async def websocket_endpoint(websocket: WebSocket, role: str):
    if role not in active_connections:
        await websocket.close(code=4000, reason="Invalid role.")
        return

    await connect_client(websocket, role)

    try:
        while True:
            data = await websocket.receive_text()
            if role == "controller":
                await broadcast_to_boards(data)

    except WebSocketDisconnect:
        disconnect_client(websocket, role)
    except Exception as e:
        print(f"Error in connection loop: {e}")
        disconnect_client(websocket, role)

# Main fuction that calls run through localhost:8000
if __name__ == "__main__":
    import uvicorn
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("LOCALHOST")))
