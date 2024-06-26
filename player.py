from tqdm import tqdm

class Player(object):
    def __init__(self, name=None, travel_status=None):
        self.name = name
        self.travel_status = travel_status
        self.focus = 0
        self.fun = 0
        self.knowledge = 0

        if self.name.lower() == "bryan":
            print("Hi Bryan! You're bang up to the elephant!")
        elif self.name.lower() == "adam":
            print("Hi Adam, at the end of this week you are required to watch High School Musical")
        elif self.name.lower() == "sabina":
            print("HAPPY BIRTHDAY WEEK SABINA!!!!1!!")

    # methods
    def mod_focus(self, num):
        self.focus += num

    def mod_fun(self, num):
        self.fun += num

    def mod_knowledge(self, num):
        self.knowledge += num

    def check_status(self):
        max_fun = 20
        max_focus = 20
        max_knowledge = 25

        (tqdm(range(max_fun), desc="Fun:      ",
              bar_format='{desc:<12}{percentage:3.0f}%|{bar:10}|{n_fmt}/{total_fmt}{bar:-10b}')).update(self.fun)
        (tqdm(range(max_focus), desc="Focus:    ",
              bar_format='{desc:<12}{percentage:3.0f}%|{bar:10}|{n_fmt}/{total_fmt}{bar:-10b}')).update(self.focus)
        (tqdm(range(max_knowledge), desc="Knowledge:",
              bar_format='{desc:<12}{percentage:3.0f}%|{bar:10}|{n_fmt}/{total_fmt}{bar:-10b}')).update(self.knowledge)

