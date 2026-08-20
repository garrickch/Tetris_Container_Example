import pytest
from unittest.mock import mock_open, patch
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocketDisconnect

# Imports the FastAPI app and active_connections dictionary located in src/project/server.py
from project.server import app, active_connections

"""Create the standard FastAPI TestClient"""
client = TestClient(app)

"""Before each test, resets active_connections"""
@pytest.fixture(autouse=True)
def clear_connections():
    active_connections["controller"].clear()
    active_connections["board"].clear()
    yield


### HTTP ENDPOINT TESTS ###

"""Tests that the root launcher page returns 200 HTML."""
def test_get_index():
    response = client.get("/")
    assert response.status_code == 200
    print("Output from test_get_index test:")
    print(response.text)
    assert "<h1>Tetris Game Launcher</h1>" in response.text

"""Tests the board page works by mocking the HTML file read."""
@patch("builtins.open", new_callable=mock_open, read_data="<html>Board Screen</html>")
def test_get_board(mock_file):
    response = client.get("/board")
    assert response.status_code == 200
    assert "Board Screen" in response.text
    mock_file.assert_called_once()

"""Tests the controller page works by mocking the HTML file read."""
@patch("builtins.open", new_callable=mock_open, read_data="<html>Controller Screen</html>")
def test_get_controller(mock_file):
    response = client.get("/controller")
    assert response.status_code == 200
    assert "Controller Screen" in response.text
    mock_file.assert_called_once()


### WEBSOCKET TESTS ###

"""Tests that a bad role gets disconnected with custom code 4000."""
def test_websocket_invalid_role():
    with pytest.raises(WebSocketDisconnect) as exc_info:
        with client.websocket_connect("/ws/hacker"):
            pass
    assert exc_info.value.code == 4000

"""Tests that connection limits track properly on connect and exit."""
def test_websocket_connection_and_disconnect():
    assert len(active_connections["board"]) == 0
    # Context manager simulates connecting and then closing the socket
    with client.websocket_connect("/ws/board"):
        assert len(active_connections["board"]) == 1
    # Triggers WebSocketDisconnect internally when exiting context
    assert len(active_connections["board"]) == 0

"""Tests that messages sent by a controller land on the board socket."""
def test_websocket_broadcast_controller_to_board_01():
    # Connect a simulated game board and a simulated controller simultaneously
    with client.websocket_connect("/ws/board") as board_socket:
        with client.websocket_connect("/ws/controller") as controller_socket:
            # Controller sends the move left command
            controller_socket.send_text("MOVE_LEFT")
            # The board should receive it via broadcast
            received_data = board_socket.receive_text()
            assert received_data == "MOVE_LEFT"

"""Tests that messages sent by a controller land on the board socket."""
def test_websocket_broadcast_controller_to_board_02():
    # Connect a simulated game board and a simulated controller simultaneously
    with client.websocket_connect("/ws/board") as board_socket:
        with client.websocket_connect("/ws/controller") as controller_socket:
            # Controller sends the move up command
            controller_socket.send_text("MOVE_UP")
            # The board should receive it via broadcast
            received_data = board_socket.receive_text()
            assert received_data == "MOVE_UP"

"""Tests that messages sent by a controller land on the board socket."""
def test_websocket_broadcast_controller_to_board_03():
    # Connect a simulated game board and a simulated controller simultaneously
    with client.websocket_connect("/ws/board") as board_socket:
        with client.websocket_connect("/ws/controller") as controller_socket:
            # Controller sends the space command
            controller_socket.send_text(" ")
            # The board should receive it via broadcast
            received_data = board_socket.receive_text()
            assert received_data == " "

"""Tests that messages sent by a controller land on the board socket."""
def test_websocket_broadcast_controller_to_board_04():
    # Connect a simulated game board and a simulated controller simultaneously
    with client.websocket_connect("/ws/board") as board_socket:
        with client.websocket_connect("/ws/controller") as controller_socket:
            # Controller sends the move right command
            controller_socket.send_text("MOVE_UP")
            # The board should receive it via broadcast
            received_data = board_socket.receive_text()
            assert received_data == "MOVE_UP"
            # Controller sends the move down command
            controller_socket.send_text("MOVE_DOWN")
            # The board should receive it via broadcast
            received_data = board_socket.receive_text()
            assert received_data == "MOVE_DOWN"
