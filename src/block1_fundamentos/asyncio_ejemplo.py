"""Async / await: servidor simple de chat con asyncio."""
import asyncio


async def manejar_cliente(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f"Conectado {addr}")
    while True:
        data = await reader.read(100)
        if not data:
            break
        mensaje = data.decode()
        print(f"Recibido de {addr}: {mensaje}")
        writer.write(data)
        await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main():
    servidor = await asyncio.start_server(manejar_cliente, "127.0.0.1", 8888)
    async with servidor:
        await asyncio.sleep(0.2)  # tiempo para pruebas


if __name__ == "__main__":
    asyncio.run(main())
