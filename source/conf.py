# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Pharmagest'
copyright = '2023, Vincent Deguin'
author = 'Vincent Deguin'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

comments_config = {
   "utterances": {
      "repo": "https://github.com/Deugz/Encyclopedia-Home",
      "optional": "config",
   }
}

comments_config = {
   "hypothesis": True
}



extensions = [
  
  "myst_parser",
  "sphinx_design",
  "sphinx_comments",
  "sphinx_new_tab_link",
  "sphinx_book_theme",
  "sphinx_togglebutton",
  "sphinx_thebe",
]

myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_heading_anchors = 2



templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/Logo/Logo-Equasens.jpg"
html_favicon = "_static/Logo/Logo-Equasens.jpg"
html_static_path = ['_static']

html_theme_options = {
    "external_links": [
        {
            "url": "",
            "name": "&nbsp &nbsp &nbsp &nbsp 💫 Logiciel ID &nbsp",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "",
            "name": "&nbsp &nbsp &nbsp &nbsp 💫 ID.Decisionel &nbsp",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "",
            "name": "&nbsp &nbsp &nbsp &nbsp 💫 ID.Mobilité &nbsp",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "",
            "name": "&nbsp &nbsp &nbsp &nbsp 💫 OFFIMSS &nbsp",
            "attributes": {"target": "_blank"},
        },

    ],
    "header_links_before_dropdown": 10,    
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Deugz/Encyclopedia-Home",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Home",
            "url": "https://deugz.github.io/Encyclopedia-Home/build/html/index.html",
            "icon": "fa-solid fa-house",
        },
        {
            "name": "Profile",
            "url": "https://deugz.github.io/nb-profile/_build/html/intro.html",
            "icon": "fa-solid fa-user",
        },
        {
            "name": "Blog",
            "url": "https://deugz.github.io/ab-blog/_website/index.html",
            "icon": "fa-solid fa-blog",
        },
        {
            "name": "Tools",
            "url": "https://deugz.github.io/nb-tools/_build/html/intro.html",
            "icon": "fa-solid fa-screwdriver-wrench",
        },
    ],
    

    "logo": {
        "text": " &nbsp Pharmagest &nbsp &nbsp ",
        "image_dark": "_static/Logo/Logo-Equasens.jpg",
        "alt_text": " &nbsp Pharmagest &nbsp &nbsp",
    },
    
    
    "navbar_start": ["navbar-logo"],
    
}


html_css_files = ["css/custom_style.css",]
html_js_files = []

    
