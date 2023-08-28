
import reflex as rx

class InputBlurState(rx.State):
    text: str = " "

    def set_text(self, text: str):
        self.text = text.upper()

def index():
    return rx.vstack(
        rx.text(InputBlurState.text),
        #rx.image(src="magnifying-glass-solid 1.png", width="10px", height="auto"),
        rx.input(
            placeholder="                Search",
            font_size="1.2em",
            on_blur=InputBlurState.set_text,
            border_radius="6em",
            border_color="#698694",
            style={"height":"60px","top":"-100px","width":"-200px"}
        ),
        rx.button(
            "學生1",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"20", "font-size": "30px","top":"-80px"},
            border_radius="1em",
        ),
        rx.button(
            "學生2",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"20", "font-size": "30px","top":"-60px"},
            border_radius="1em",
        ),
        rx.button(
            "學生3",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"20", "font-size": "30px","top":"-40px"},
            border_radius="1em",
        ),
        rx.button(
            "學生4",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"20", "font-size": "30px","top":"-20px"},
            border_radius="1em",
        ),
        rx.button(
            "學生5",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"20", "font-size": "30px","top":"0px"},
            border_radius="1em",
        ),
        rx.button(
            "學生6",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"20", "font-size": "30px","top":"20px"},
            border_radius="1em",
        ),
        rx.button(
            "學生7",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"20", "font-size": "30px","top":"40px"},
            border_radius="1em",
        ),
        rx.button(
            "學生8",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"20", "font-size": "30px","top":"60px"},
            border_radius="1em",
        ),
        rx.button(
            "學生9",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"20", "font-size": "30px","top":"100px"},
            border_radius="1em",
        ),
        rx.button(
            "學生10",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"20", "font-size": "30px","top":"120px"},
            border_radius="1em",
        ),
        rx.button(
            "學生11",
            color="#000000",
            bg="#FFFFFF",
            style={"width":"350px","height":"20", "font-size": "30px","top":"140px"},
            border_radius="1em",
        ),
    style={"background-color": "#FFFAF0", "height": "145vh", "display": "flex", "align-items": "center", "justify-content": "center"},
    )
app = rx.App()
app.add_page(index)
app.compile()
