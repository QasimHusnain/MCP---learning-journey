# import asyncio
# import websockets

# async def handler(websocket):
#     message = await websocket.recv()
#     print("Client Said:", message)
#     await websocket.send("Hello from server!,Are you there, my client?")


# async def main():
#     async with websockets.serve(handler, "localhost", 8765):
#         print("Server ready at ws://localhost:8765")
#         await asyncio.Future() #run forever


# if __name__ == "__main__":
#     asyncio.run(main())


#================For live chat===============
import asyncio            # Import asyncio for asynchronous event loop
import websockets         # Import websockets library to handle WebSocket protocol

# This function handles each client that connects
async def handler(websocket):
    print("✅ Client connected")   # Log when a new client connects

    try:
        while True:   # Keep the connection open as long as client is active
            message = await websocket.recv()          # Wait to receive a message from client
            print(f"Client said: {message}")          # Print the client’s message

            reply = f"Server received: {message}"     # Prepare a reply message
            await websocket.send(reply)               # Send reply back to client
    except websockets.ConnectionClosed:               # Handle disconnection
        print("❌ Client disconnected")                # Log when client disconnects

# Main entry point for starting the server
async def main():
    # Start the WebSocket server at localhost:8765
    async with websockets.serve(handler, "localhost", 8765):
        print("Server ready at ws://localhost:8765")   # Confirm server is running
        await asyncio.Future()   # Keep the server running forever (until manually stopped)

# Run the server
if __name__ == "__main__":
    asyncio.run(main())
