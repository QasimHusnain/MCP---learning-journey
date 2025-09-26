import asyncio          # for async event loop
import websockets       # to create websocket server
import json             # to encode/decode JSON messages

# Step 1: Define RPC methods
def add(a, b):          # add two numbers
    return a + b

def subtract(a, b):     # subtract b from a
    return a - b

def multiply(a, b):     # multiply two numbers
    return a * b

# Step 2: Register methods in a dictionary
rpc_methods = {
    "add": add,              # "add" keyword maps to add() function
    "subtract": subtract,    # "subtract" keyword maps to subtract() function
    "multiply": multiply     # "multiply" keyword maps to multiply() function
}

# Step 3: Handle incoming requests
async def handler(websocket):                  # handles client connection
    async for message in websocket:            # receive messages from client
        try:
            request = json.loads(message)      # parse JSON request into Python dict

            method = request.get("method")     # get the function name
            params = request.get("params", []) # get parameters (list), default empty
            req_id = request.get("id")         # request ID for tracking

            if method in rpc_methods:          # check if method is valid
                result = rpc_methods[method](*params)   # call the mapped function with params
                response = {
                    "jsonrpc": "2.0",          # JSON-RPC version
                    "result": result,          # return value of the function
                    "id": req_id               # same ID as request
                }
            else:                              # if method not found
                response = {
                    "jsonrpc": "2.0",
                    "error": {"code": -32601, "message": "Method not found"},
                    "id": req_id
                }

        except Exception as e:                 # handle any unexpected errors
            response = {
                "jsonrpc": "2.0",
                "error": {"code": -32000, "message": str(e)}, # error details
                "id": request.get("id", None)                 # preserve ID if possible
            }

        await websocket.send(json.dumps(response))  # send response back to client

# Step 4: Start server
async def main():
    async with websockets.serve(handler, "localhost", 8700):   # start server at ws://localhost:8765
        print("RPC WebSocket Server running on ws://localhost:8700")
        await asyncio.Future()    # keep server running forever

asyncio.run(main())  # run the event loop and start server
