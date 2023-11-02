# Simple Web Server

This is a basic implementation of a web server in Python that handles one HTTP request at a time. The server accepts and parses HTTP requests, retrieves the requested file from the server's file system, creates an HTTP response message with headers, and sends the response directly to the client. If the requested file is not found, the server responds with a "404 Not Found" message.

## Usage

1. Place an HTML file (e.g., `HelloWorld.html`) in the same directory as the server.
2. Run the server program, ensuring it's listening on a specific port (e.g., 6789).
3. Determine the IP address of the host running the server (e.g., 128.238.251.26).
4. From another host, open a web browser and access the server using the following URL format:
   

- `<server_ip>` is the IP address of the server host.
- `<port>` is the port number you specified in the server code (e.g., 6789).
- `HelloWorld.html` is the name of the file you placed in the server directory.

5. If the file exists, the browser will display its contents. If the file is not found, you'll receive a "404 Not Found" message.

## Code

You can find the Python code for this web server in the `WebServer.py` file.

## Assumptions

- This server assumes it will receive well-formatted GET requests.
- It only handles requests for single HTML objects on the Internet.

## Optional: Multi-Threaded Web Server

The basic server provided in this repository handles one request at a time. However, if you want to implement a multi-threaded version that can serve multiple requests simultaneously, you can explore multi-threading options in Python.

Feel free to use and modify this simple web server for your projects. For detailed implementation instructions, refer to the provided code in `WebServer.py`.
