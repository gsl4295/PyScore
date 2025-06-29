# PyScore
![GitHub Release #](https://img.shields.io/github/v/release/gsl4295/PyScore?include_prereleases&sort=date&display_name=tag)
![GitHub Commits](https://img.shields.io/github/commit-activity/t/gsl4295/PyScore)
![GitHub Issues](https://img.shields.io/github/issues/gsl4295/PyScore)<br>
Simple python-powered scoreboard for use with my online webcasts.

<img src="/images/GUI.png" width=500 /><br>

### Setup
- My setup uses the `space_mono` font family. If you want to replicate the image above,
  - Download it [here](https://) on Google Fonts.
  - Then, move the .ttf files over into a new `fonts/` directory at the root of this project.

### Features
- User-inputted:
  - Team names
  - Team colors
  - Score
    - +1, -1, or by text input

| Hotkeys  | Team 1  | Team 2  |
|:--------:|:-------:|:-------:|
| Score +1 | numpad7 | numpad9 |
| Score -1 | numpad1 | numpad3 |

- Streaming-friendly output section
  - Background (for using color key): `#252526`
  - Find an example of how I'm using this program in `images/OBS-overlay-example.png`
