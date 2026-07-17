from fastapi import FastAPI

from .routes import admin, invoices, orders, profiles, search, sessions, users


def create_app() -> FastAPI:
    app = FastAPI(
        title="App Backend",
        version="1.8.0",
        openapi_version="3.1.0",
    )
    app.include_router(users.router)
    app.include_router(orders.router)
    app.include_router(invoices.router)
    app.include_router(search.router)
    app.include_router(sessions.router)
    app.include_router(profiles.router)
    app.include_router(admin.router)
    return app


app = create_app()

