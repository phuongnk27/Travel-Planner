# pip3 install customtkinter
# pip3 install tkintermapview
import tkinter
import customtkinter
import tkintermapview

MODE="System"
THEME="green"
customtkinter.set_appearance_mode(MODE)  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(THEME)  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    NAME="Travel Planner"
    WIDTH=1500
    HEIGHT=900

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize Ctk window
        self.title(App.NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.marker_list = []  #TODO marker?

        # Divide window into 2 frames left right (5x5)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.left_frame = customtkinter.CTkFrame(master=self, width=600, height=900, corner_radius=0, fg_color=None, border_color="white",border_width=5)  #TODO: REMOVE BORDER
        self.left_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        
        self.right_frame = customtkinter.CTkFrame(master=self, width=900, height=900, corner_radius=0, fg_color=None, border_color="white",border_width=5)
        self.right_frame.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

        # LEFT FRAME
        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure(1, weight=1)
        self.left_frame.rowconfigure(2, weight=1)
        self.left_frame.rowconfigure(3, weight=1)
        self.left_frame.rowconfigure(4, weight=1)
        self.left_frame.columnconfigure(0, weight=1)

        self.entry = customtkinter.CTkEntry(master=self.left_frame,
                                            placeholder_text="Starting Location", width=500)
        self.entry.grid(row=0, column=0, sticky="nw", padx=50 ,pady=50)
        self.entry.bind("<Return>", self.search_event)

        # RIGHT FRAME: Map widget
        self.right_frame.columnconfigure(0, weight=1)
        self.right_frame.rowconfigure(0, weight=1)

        self.map_widget = tkintermapview.TkinterMapView(master=self.right_frame, width=900, height=900, corner_radius=50)
        self.map_widget.grid(row=0, column=0, sticky="nsew")
        self.map_widget.set_position(53.631611, -113.323975)  #TODO: Use device's location maybe?
        self.map_widget.set_zoom(10)

    def search_event(self, event=None):
        for marker in self.marker_list:
            marker.delete()
        self.map_widget.set_address(self.entry.get())
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()