# import asyncio
# import websockets

# async def hello():
#     url = "ws://localhost:8765"
#     async with websockets.connect(url) as websocket:
#         await websocket.send("Hello from client!THis is Ali, Are you there?")
#         reply = await websocket.recv()
#         print(f"Server replied: {reply}")


# if __name__ == "__main__":
#     asyncio.run(hello())

#=========================live chat========================
import asyncio            # Import asyncio to run asynchronous (non-blocking) code
import websockets         # Import the websockets library for WebSocket communication

async def chat():  
    uri = "ws://localhost:8765"   # Define the WebSocket server address (protocol, host, port)

    # Connect to the WebSocket server and keep the connection open
    async with websockets.connect(uri) as websocket:
        print("✅ Connected to server")   # Confirm that connection to server is successful

        while True:   # Loop so the client can keep sending/receiving messages
            msg = input("You: ")         # Ask user to type a message in terminal
            await websocket.send(msg)    # Send the typed message to the WebSocket server

            reply = await websocket.recv()     # Wait and receive a message from the server
            print(f"Server: {reply}")          # Print the reply from the server to the terminal

# Run the chat() coroutine until it finishes (keeps running until stopped manually)
asyncio.run(chat())
