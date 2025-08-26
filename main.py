import asyncio
import websockets

async def handler(websocket, path):
    print(f"Cliente conectado de {websocket.remote_address}")
    try:
        async for message in websocket:
            if message == "ping":
                await websocket.send("pong")
    except websockets.exceptions.ConnectionClosed:
        print(f"Cliente {websocket.remote_address} desconectado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

async def main():
    host = "0.0.0.0"  
    port = 8765
    async with websockets.serve(handler, host, port):
        print(f"Servidor de Ping-Pong iniciado em ws://{host}:{port}")
        await asyncio.Future()  

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Servidor desligado.")