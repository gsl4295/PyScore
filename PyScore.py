import dearpygui.dearpygui as dpg

class GUIManager:
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.window_width = int(self.width / 2)
        self.scoreboard_height = int(self.height / 4)
        self.settings_height = self.scoreboard_height * 3
        self.initial_t1_color = [0, 130, 0, 255]
        self.initial_t2_color = [0, 130, 130, 255]
        self.color_white = [255, 255, 255, 255]
        self.alignment_width = 16

    @staticmethod
    def score_up(sender, app_data, user_data):
        """
        Adds 1 to a team's score.
        :param sender:
        :param app_data:
        :param user_data:
        :return: None
        """
        specifier = f"team{str(user_data)}_score"
        try:
            current_score = int(dpg.get_value(specifier))
        except ValueError:
            current_score = 0
        current_score += 1
        dpg.set_value(specifier, value=current_score)

    @staticmethod
    def score_down(sender, app_data, user_data):
        """
        Subtracts 1 from a team's score.
        :param sender:
        :param app_data:
        :param user_data:
        :return: None
        """
        specifier = f"team{str(user_data)}_score"
        try:
            current_score = int(dpg.get_value(specifier))
        except ValueError:
            current_score = 0
        current_score -= 1
        dpg.set_value(specifier, value=current_score)

    @staticmethod
    def set_score(sender, app_data, user_data):
        """
        Sets a team's score to a text input
        :param sender:
        :param app_data:
        :param user_data:
        :return: None
        """
        specifier = f"team{str(user_data)}_score"
        try:
            current_score = int(app_data)
        except ValueError:
            current_score = 0
        dpg.set_value(specifier, current_score)

    @staticmethod
    def color_picker(sender, app_data, user_data):
        """
        Sets a theme to a color inputted from an on-screen color picker item.
        :param sender: Item that called back
        :param app_data: RGBA color values
        :param user_data: Defines which team's color to be changed
        :return: None
        """
        red = app_data[0] * 255
        green = app_data[1] * 255
        blue = app_data[2] * 255
        alpha = app_data[3] * 255

        specifier = f"team{user_data}_color_theme"
        dpg.set_value(specifier, [red, green, blue, alpha])

    @staticmethod
    def rename_teams(sender, app_data, user_data: str):
        """
        Renames teams based on an on-screen text input.
        :param sender:
        :param app_data:
        :param user_data:
        :return: None
        """
        if app_data == "":
            app_data = f"Team {user_data}"
        dpg.set_value(f"team{user_data}_name", f"{app_data}")

    @staticmethod
    def define_fonts():
        """
        Sets themes to use any font.
        :return: None
        """
        with dpg.font_registry():
            space_mono_regular = dpg.add_font("fonts/SpaceMono-Regular.ttf", 30)
            space_mono_scoreboard_scale = dpg.add_font("fonts/SpaceMono-Bold.ttf", size=100)
            #space_mono_italic = dpg.add_font("fonts/SpaceMono-Italic.ttf", 30)
            #space_mono_bold = dpg.add_font("fonts/SpaceMono-Bold.ttf", 30)
            #space_mono_bolditalic = dpg.add_font("fonts/SpaceMono-BoldItalic.ttf", 30)

            dpg.bind_font(space_mono_regular)
            dpg.bind_item_font("team1_scoreboard", space_mono_scoreboard_scale)
            dpg.bind_item_font("team2_scoreboard", space_mono_scoreboard_scale)

    def define_themes(self):
        """
        Creates and initially binds all themes.
        :return: None
        """
        with dpg.theme() as main_theme: # Theme as a base for all other formatting to go off of.
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Text, self.color_white, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvAll)

        dpg.bind_theme(main_theme) # bind_theme() applies a theme to *everything*.

        with dpg.theme() as team_1_color: # This is used for team 1's accent color,
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Text, self.color_white, category=dpg.mvThemeCat_Core, tag="team1_color_theme")

        dpg.bind_item_theme("team1_name", team_1_color) # bind_item_theme, as suggested, applies a theme to only
        dpg.bind_item_theme("team1_score", team_1_color) # a specific item.

        with dpg.theme() as team_2_color: # and this one is for team 2's accent.
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Text, self.color_white, category=dpg.mvThemeCat_Core, tag="team2_color_theme")

        dpg.bind_item_theme("team2_name", team_2_color)
        dpg.bind_item_theme("team2_score", team_2_color)

        with dpg.theme() as up_button_theme: # Green color for buttons that add a point
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Button, value=[0, 100, 0, 255], category=dpg.mvThemeCat_Core)

        dpg.bind_item_theme("t1_score_up_button", up_button_theme)
        dpg.bind_item_theme("t2_score_up_button", up_button_theme)

        with dpg.theme() as down_button_theme: # and red for those that remove a point.
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Button, value=[100, 0, 0, 255], category=dpg.mvThemeCat_Core)

        dpg.bind_item_theme("t1_score_down_button", down_button_theme)
        dpg.bind_item_theme("t2_score_down_button", down_button_theme)

    def window_manager(self):
        """
        Creates all GUI items.
        :return: None
        """
        # This first window is a parent to four items, all associated with Team 1's settings.
        with dpg.window(label="Team 1 Settings", width=self.window_width, height=self.settings_height, pos=[0, self.scoreboard_height],
                        no_move=True, no_resize=True, no_close=True, no_collapse=True) as self.t1_settings:
            dpg.add_button(label="Team 1 [+1]", tag="t1_score_up_button", callback=self.score_up, user_data=1)
            dpg.add_button(label="Team 1 [-1]", tag="t1_score_down_button", callback=self.score_down, user_data=1)
            dpg.add_input_text(hint="Set score...", tag="t1_set_score", callback=self.set_score, user_data=1)
            dpg.add_input_text(hint="Rename...", tag="t1_rename", callback=self.rename_teams, user_data=1)
            dpg.add_color_edit(tag="t1_color_picker", default_value=self.color_white, callback=self.color_picker, user_data=1)

        # Note the "callback=" argument. This has the button call a function to do whatever you want in the
        # background along with some optional user_data.
        with dpg.window(label="Team 2 Settings", width=self.window_width, height=self.settings_height, pos=[self.window_width, self.scoreboard_height],
                        no_move=True, no_resize=True, no_close=True, no_collapse=True) as self.t2_settings:
            dpg.add_button(label="Team 2 [+1]", tag="t2_score_up_button", callback=self.score_up, user_data=2)
            dpg.add_button(label="Team 2 [-1]", tag="t2_score_down_button", callback=self.score_down, user_data=2)
            dpg.add_input_text(hint="Set score...", tag="t2_set_score", callback=self.set_score, user_data=2)
            dpg.add_input_text(hint="Rename...", tag="t2_rename", callback=self.rename_teams, user_data=2)
            dpg.add_color_edit(tag="t2_color_picker", default_value=self.color_white, callback=self.color_picker, user_data=2)

        with dpg.window(label="Scoreboard", width=self.width, height=self.scoreboard_height, pos=[0, 0],
                        no_move=True, no_resize=True, no_close=True, no_collapse=True, no_title_bar=True, no_scrollbar=True):
            with dpg.group(horizontal=True, tag="team1_scoreboard") as self.team1_scores:
                dpg.add_spacer(width=15)
                dpg.add_text(default_value="0", tag="team1_score")
                dpg.add_text(default_value=" - ")
                dpg.add_text(default_value="Team 1", tag="team1_name")
            with dpg.group(horizontal=True, tag="team2_scoreboard") as self.team2_scores:
                dpg.add_spacer(width=15)
                dpg.add_text(default_value="0", tag="team2_score")
                dpg.add_text(default_value=" - ")
                dpg.add_text(default_value="Team 2", tag="team2_name")

    def keyboard_manager(self):
        """
        Creates a registry that listens for all keyboard inputs
        :return: None
        """
        with dpg.handler_registry():
            dpg.add_key_press_handler(key=dpg.mvKey_NumPad7, callback=self.score_up, user_data=1)
            dpg.add_key_press_handler(key=dpg.mvKey_NumPad1, callback=self.score_down, user_data=1)

            dpg.add_key_press_handler(key=dpg.mvKey_NumPad9, callback=self.score_up, user_data=2)
            dpg.add_key_press_handler(key=dpg.mvKey_NumPad3, callback=self.score_down, user_data=2)

    def main_loop(self):
        dpg.create_context() # Start the main GUI process

        self.window_manager()
        self.define_fonts()
        self.define_themes()
        self.keyboard_manager()
        self.color_picker(sender="", app_data=self.color_white, user_data=1) # Use initial color scheme already
        self.color_picker(sender="", app_data=self.color_white, user_data=2) # loaded onto the color pickers

        dpg.create_viewport(title='Scoreboard', width=self.width, height=self.height)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

if __name__ == "__main__":
    manager = GUIManager()
    manager.main_loop()
