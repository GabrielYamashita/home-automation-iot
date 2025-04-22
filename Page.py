
import streamlit as st
from FloorPlan import FloorPlan
from Sidebar import Sidebar


class Page():
    def __init__(self, main, sidebar):
        self.sidebar = sidebar
        self.main = main
        # self.title = title

    def render(self):
        self.sidebar.render()
        self.main.render()


if __name__ == "__main__":
    MyRoom = FloorPlan("My Home", 6, 6)
    MyRoom.add_room(0, 5, 0, 5)
    MyRoom.add_room(2, 3, 0, 1)
    MyRoom.add_room(0, 3, 4, 5)
    MyRoom.add_room(4, 5, 0, 2)
    MyRoom.add_room(4, 5, 3, 5)

    Sidebar = Sidebar(
        title="My Home",
        components=["Component 1", "Component 2", "Component 3"],
        debug=True
    )

    mainPage = Page(MyRoom, Sidebar)
    mainPage.render()