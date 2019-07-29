import tkinter as Tk
from tkinter import *
import requests


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """

    #    # Ping parameters as function of OS
    #    parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"
    #
    #    # Pinging
    #    return system_call("ping " + parameters + " " + host) == 0

    #    try:
    #        response = subprocess.check_output(
    #        ['ping', '-c', '3', '10.10.0.100'],
    #        stderr=subprocess.STDOUT,  # get all output
    #        universal_newlines=True  # return string not bytes
    #        return response
    #        )
    #    except subprocess.CalledProcessError:
    #        response = None
    #
    #    return 'False'

    r = requests.get(host)
    # print(r.text)
    return r.status_code == 200


class TrafficLights:
    def __init__(self, url1, url2, url3, url4):

        window = Tk()
        window.title("Ping Indicator")



        frame = Frame(window)
        frame.pack()

        self.color = StringVar()

        self.canvas = Canvas(window, width=700, height=800, bg="white")
        self.canvas.pack()

        self.oval_one = self.canvas.create_oval(5, 50, 300, 300, fill="white")
        self.oval_two = self. canvas.create_oval(400, 50, 700, 300, fill='white')
        self.oval_three = self.canvas.create_oval(5, 400, 300, 650, fill="white")
        self.oval_four = self.canvas.create_oval(400, 400, 700, 650, fill='white')
        self.rectangle_one = self.canvas.create_rectangle(5, 5, 300, 40, fill="#001A57")
        self.rectanglefill_one = self.canvas.create_text(150, 20, fill="white", width=295,
                                                         text="Request Result: " + str(url1))
        self.rectangle_two = self.canvas.create_rectangle(400, 5, 700, 40, fill="#001A57")
        self.rectanglefill_two = self.canvas.create_text(550, 20, fill="white", width=295,
                                                         text="Request Result: " + str(url2))

        self.rectangle_three = self.canvas.create_rectangle(5, 335, 300, 370, fill="#001A57")
        self.rectanglefill_three = self.canvas.create_text(150, 350, fill="white", width=295,
                                                         text="Request Result: " + str(url3))
        self.rectangle_four = self.canvas.create_rectangle(405, 335, 700, 370, fill="#001A57")
        self.rectanglefill_four = self.canvas.create_text(550, 350, fill="white", width = 295,
                                                         text="Request Result: " + str(url4))
        # self.oval_green = self.canvas.create_oval(230, 10, 330, 110, fill="white")

        if (ping(url1) != 'False'):
            self.color.set('G')
            self.canvas.itemconfig(self.oval_one, fill="green")
            #window.title("The website returned the ping! :D")
        else:
            self.color.set('R')
            self.canvas.itemconfig(self.oval_one, fill='red')
            #window.title("The website did not return the ping :( ")
        if (ping(url2) != 'False'):
            self.color.set('G')
            self.canvas.itemconfig(self.oval_two, fill="green")
            #window.title("The website returned the ping! :D")
        else:
            self.color.set('R')
            self.canvas.itemconfig(self.oval_two, fill='red')
        if (ping(url3) != 'False'):
            self.color.set('G')
            self.canvas.itemconfig(self.oval_three, fill="green")
            # window.title("The website returned the ping! :D")
        else:
            self.color.set('R')
            self.canvas.itemconfig(self.oval_three, fill='red')
            # window.title("The website did not return the ping :( ")
        if (ping(url4) != 'False'):
            self.color.set('G')
            self.canvas.itemconfig(self.oval_four, fill="green")
            # window.title("The website returned the ping! :D")
        else:
            self.color.set('R')
            self.canvas.itemconfig(self.oval_four, fill='red')
            #window.title("The website did not return the ping :( ")
            # textbox = Text (window)

        # textbox.pack()


        window.mainloop()
TrafficLights('http://api.dataservice.duke.edu', 'https://dataservice.duke.edu/portal/#/login', 'https://google.com', 'https://amazon.com')

