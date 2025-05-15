

import streamlit as st

from main import readDatabase
from Slider import SliderWidget


class MyRoom:
    def __init__(self, title, data):
        self.title = title
        self.devices = data["devices"]


    # def renderSlider(self, slider):
    #     slider(
    #         label="Select a Value", 
    #         min_value=0, max_value=100, default_value=75, 
    #         session_key="slider1",
    #     )


    def render(self, slider):
        # Título da Página
        if self.title[-1] == "a":
            st.title(f"Minha {self.title}:")
        else:
            st.title(f"Meu {self.title}:")

        st.divider()

        # Subtítulo da Página
        if len(self.devices) == 0:
            st.markdown("Sem dispositivos no momento...")
        else:
            # st.header("Dispositivos:")
            for device in self.devices:
                if device["type"] in ["lamp"]:
                    st.markdown(f"- {device['name']} ({device['brightness']})")





if __name__ == "__main__":

    data = readDatabase()

    room = data["MyHome"][3]

    sala = MyRoom(room["name"], room)

    slider = SliderWidget(
        label="Select a Value", 
        min_value=0, max_value=100, default_value=75, 
        session_key="slider1",
    )

    sala.render(slider)