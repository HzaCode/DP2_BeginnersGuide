project = "DP2 Beginner's Guide"
author = "HzaCode"
copyright = "2025, HzaCode"
release = "1.0.0"

extensions = [
    "myst_parser",
    "sphinx_rtd_theme",
]

exclude_patterns = ["README.md"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "_static/image2.png"

html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_nav_header_background': '#2980B9',
}
