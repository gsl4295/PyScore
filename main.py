import dearpygui.dearpygui as dpg

dpg.create_context()

def score_up(sender, app_data, user_data):
    specifier = f"team{str(user_data)}_score"
    current_score = int(dpg.get_value(specifier))
    current_score += 1
    dpg.set_value(specifier, value=current_score)

def score_down(sender, app_data, user_data):
    specifier = f"team{str(user_data)}_score"
    current_score = int(dpg.get_value(specifier))
    current_score -= 1
    dpg.set_value(specifier, value=current_score)

def rename(sender, app_data, user_data: str):
    dpg.set_value(f"team{user_data}_name", f"{app_data}")

with dpg.font_registry():
    space_mono_regular = dpg.add_font("fonts/SpaceMono-Regular.ttf", 30)
    space_mono_italic = dpg.add_font("fonts/SpaceMono-Italic.ttf", 30)
    space_mono_bold = dpg.add_font("fonts/SpaceMono-Bold.ttf", 30)
    space_mono_bolditalic = dpg.add_font("fonts/SpaceMono-BoldItalic.ttf", 30)

with dpg.window(label="Scorekeeping", width=407, height=300, pos=[0, 0],
                no_move=True, no_resize=True, no_close=True, no_collapse=True) as scorekeeping:
    dpg.add_button(label="Team 1 [+1]", tag="t1_score_up_button", callback=score_up, user_data=1)
    dpg.add_button(label="Team 1 [-1]", tag="t1_score_down_button", callback=score_down, user_data=1)
    dpg.add_separator()
    dpg.add_button(label="Team 2 [+1]", tag="t2_score_up_button", callback=score_up, user_data=2)
    dpg.add_button(label="Team 2 [-1]", tag="t2_score_down_button", callback=score_down, user_data=2)

with dpg.window(label="Scoreboard", width=1700, height=300, pos=[407, 0],
                no_move=True, no_resize=True, no_close=True, no_collapse=True) as scoreboard:
    dpg.add_text(default_value="Team 1", tag="team1_name", color=(255, 155, 253))
    dpg.add_text(default_value="0", tag="team1_score", color=(255, 155, 253))
    dpg.add_separator()
    dpg.add_text(default_value="Team 2", tag="team2_name", color=(155, 255, 231))
    dpg.add_text(default_value="0", tag="team2_score", color=(155, 255, 231))

with dpg.window(label="Team Names", width=408, height=300, pos=[2107, 0],
                no_move=True, no_resize=True, no_close=True, no_collapse=True) as naming:
    team1_name_input = dpg.add_input_text(hint="Team 1", callback=rename, user_data=1)
    team2_name_input = dpg.add_input_text(hint="Team 2", callback=rename, user_data=2)

dpg.bind_font(space_mono_regular)
dpg.bind_item_font(scoreboard, space_mono_bold)
dpg.bind_item_font(naming, space_mono_italic)

dpg.create_viewport(title='PyScore - Scorekeeping', width=2560, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()