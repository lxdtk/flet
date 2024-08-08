import flet as ft
import flet.fastapi

import uvicorn
app = flet.fastapi.FastAPI()

@app.get("/app")
async def helloWorld():
    return {"message": "ello app"}

async def subMain(page:ft.Page):
    await page.add_async(ft.Text("Hello subapp"))

app.mount("/sub_main", flet.fastapi.app(subMain))

if __name__ == "__main__":
    uvicorn.run("test:app", host="0.0.0.0", port=8080, reload=True)