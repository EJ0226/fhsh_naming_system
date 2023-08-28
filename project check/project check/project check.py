
import reflex as rx

class State(rx.State):
    pass


def index() :
    return rx.vstack(
        rx.button(
            "←",
            bg="#FFFAF0",
            color="#000000",
            font_size="48px",
            style={"top":"-100","left":"-150px"}
        ),
        rx.box(
            "班級 31116",
            color="#000000",
            font_size="30px",
            style={"top":"40"}
        ),
        rx.box(
            "姓名 楊沁璇",
            color="#000000",
            font_size="30px",
            style={"top":"40"}
        ),
        rx.box(
            "學號 11035032",
            color="#000000",
            font_size="30px",
            style={"top":"40"}
        ),
        rx.box(
            " ",
            bg="#000000",
            width="70%",
            style={"height":"300px"}
        ),
        rx.hstack(
            rx.button(
                "X",
                border_radius="3em",
                color="#698694",
                bg="#FFFFFF",
                style={"height":"70px","width":"100px","top":"50","right":"30"}

            ),
            rx.button(
                "✓",
                border_radius="3em",
                color="#FFFFFF",
                bg="#698694",
                style={"height":"70px","width":"100px","top":"50","left":"30"}
            )
        ),
        rx.button(
            "複點錯誤",
            border_radius="3em",
            bg="#3D3D3D",
            color="#FFFFFF",
            style={"height":"50px","width":"200px","top":"70"}
        ),
    style={"background-color": "#FFFAF0", "height": "100vh", "display": "flex", "align-items": "center", "justify-content": "center"},
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
