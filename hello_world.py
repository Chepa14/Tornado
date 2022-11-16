import asyncio

import tornado.web

PORT = 8000


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        self.write({
            'details': 'Created!',
        })
        self.set_status(201)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


async def main():
    app = make_app()
    app.listen(PORT)
    print(f'App started on port: {PORT}')
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
