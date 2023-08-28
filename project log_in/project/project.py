import reflex as rx

class State(rx.State):
    count: int = 0

def index():
    return rx.vstack(
        rx.heading(
            "復興高中",
            color="#97AEB9",
            style={"margin-left":"-20px","margin": "20px ","margin-right":"-260px"}  
        ),
        rx.heading(
            "自主學習點名系統",
            color="#97AEB9",
            style={"margin-left":"-50px","margin": "-20px ","margin-right":"-180px"}  
        ),
        rx.box(
        bg="#97AEB9",
        border_radius="sm",
        width="30%",
        height="0.5%",
        style={"margin-left":"-50px","margin": "-20px ","margin-right":"320px"}
        ),
        rx.box(
        bg="#97AEB9",
        border_radius="sm",
        width="40%",
        height="0.5%",
        style={"margin-left":"-50px","margin": "-20px ","margin-right":"280px"}
        ),
        rx.box(
        bg="#97AEB9",
        border_radius="sm",
        width="50%",
        height="0.5%",
        style={"margin-left":"-50px","margin": "-20px ","margin-right":"220px"}
        ),
        rx.button(
            "登入",
            color="#FFFFFF",
            border_radius="0.5em",
            bg="#698694",
            size="lg",
            style={"margin": "300px", "width": "250px","height":"100px", "font-size": "40px","box_shadow": "rgba(0,0,0,0.6) 8px 6px"},  
        ),
        rx.box(
        bg="#97AEB9",
        border_radius="sm",
        width="50%",
        height="0.5%",
        style={"margin-right":"-40px","margin": "-20px ","margin-left":"160px"}
        ),
        rx.box(
        bg="#97AEB9",
        border_radius="sm",
        width="40%",
        height="0.5%",
        style={"margin-right":"-40px","margin": "-20px ","margin-left":"220px"}
        ),
        rx.box(
        bg="#97AEB9",
        border_radius="sm",
        width="30%",
        height="0.5%",
        style={"margin-right":"-40px","margin": "-20px ","margin-left":"260px"}
        ),
    style={"background-color": "#FFFAF0", "height": "100vh", "display": "flex", "align-items": "center", "justify-content": "center"},
    )

app = rx.App()
app.add_page(index)
app.compile()
