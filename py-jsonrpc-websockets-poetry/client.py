import asyncio           # for async event loop
import websockets        # to connect to websocket server
import json              # for JSON encoding/decoding

# Helper function to make RPC calls
async def rpc_call(method, params, req_id):
    async with websockets.connect("ws://localhost:8700") as websocket:  # connect to server
        request = {
            "jsonrpc": "2.0",    # JSON-RPC version
            "method": method,    # which method to call (string)
            "params": params,    # list of parameters for method
            "id": req_id         # unique ID for this request
        }
        await websocket.send(json.dumps(request))   # send request to server

        response = await websocket.recv()           # wait for server’s response
        return json.loads(response)                 # convert JSON string to Python dict

# Main function to test multiple calls
async def main():
    print(await rpc_call("add", [10, 5], 1))        # call add(10,5)
    print(await rpc_call("subtract", [20, 7], 2))   # call subtract(20,7)
    print(await rpc_call("multiply", [3, 4], 3))    # call multiply(3,4)
    print(await rpc_call("divide", [8, 2], 4))      # invalid method, should return error

asyncio.run(main())   # run client event loop
