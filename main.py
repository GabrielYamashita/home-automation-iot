
import json

# from MyRoom import MyRoom

def readDatabase():
    with open("./db/dbV3.json", "r") as file:
        data = json.load(file)

    return data






















if __name__ == "__main__":
    data = readDatabase()
    # print(data)


    rooms = []
    for room in data["MyHome"]:
        print(room)
        print("")

        # rooms.append(MyRoom(room["name"], room))
        
