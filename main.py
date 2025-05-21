
import json

from Sidebar import Sidebar

from Page import Page
from FloorPlan import FloorPlan
from MyRoom import MyRoom


def readDatabase():
    with open("./db/dbV3.json", "r") as file:
        data = json.load(file)

    return data


def setSidebar(room_names):
    sidebar = Sidebar(
        title="My Home",
        components=room_names,
        debug=False
    )

    return sidebar


def mainPage():
    mainBody = FloorPlan("My Home", 6, 6)
    mainBody.add_room(0, 5, 0, 5)
    mainBody.add_room(2, 3, 0, 1)
    mainBody.add_room(0, 3, 4, 5)
    mainBody.add_room(4, 5, 0, 2)
    mainBody.add_room(4, 5, 3, 5)

    page = Page(mainBody, sidebar)


def roomPage(selectedRoom):
    index = next((i for i, room in enumerate(data["MyHome"]) if room["name"] == selectedRoom), -1)
    room = data["MyHome"][index]

    roomBody = MyRoom(room["name"], room)

    page = Page(roomBody, sidebar)


def settingsPage():
    pass




if __name__ == "__main__":
    data = readDatabase()
    # print(data)

    room_names = [room["name"] for room in data["MyHome"]]


    # selected = sidebar.selected

    if selected == "Home":
        pass


    elif selected == "Settings":
        print("Settings")


    else:
        pass

    selected = page.render()
    print(selected)
    index = next((i for i, room in enumerate(data["MyHome"]) if room["name"] == selected), -1)
    print(index)

    # print("")
    # print(index)
    # print(selected)


