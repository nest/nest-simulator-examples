# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'nest-examples'
copyright = '2024, JM'
author = 'JM'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "nbsphinx"
]

templates_path = ['_templates']
# exclude_patterns = []

nbsphinx_execute = "never"
nbsphinx_prolog =  """
{% set docname = env.doc2path(env.docname, base=None) %}


.. only:: html

{% if "brunel" not in docname %}
.. grid:: 2

   .. grid-item-card:: Run this notebook in your browser
      :columns: 4

      .. image:: https://nest-simulator.org/TryItOnEBRAINS.png
         :target: https://lab.ebrains.eu/hub/user-redirect/\
git-pull?repo=https%3A%2F%2Fgithub.com%2Fnest%2Fnest-simulator-examples&urlpath=lab\
%2Ftree%2Fnest-simulator-examples%2Fnotebooks%2Fnotebooks%2F{{docname}}&branch=main
         :width: 300px


   .. grid-item::
     :class: sd-text-muted
     :columns: 4
     :padding: 4 0 0 0

     See :ref:`our EBRAINS guide <run_jupyter>` for more information and troubleshooting.

{%endif %}

.. grid:: 1 2 2 2

   .. grid-item-card::  Download Python file:
      :columns: 4

      :download:`{{-docname.replace(".ipynb",".py")}}`

   .. grid-item-card:: Download Jupyter notebook:
      :columns: 4

      :download:`{{ docname }}`


"""

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "nestml": ("https://nestml.readthedocs.io/en/latest/", None),
    "pynn": ("https://neuralensemble.org/docs/PyNN/", None),
    "elephant": ("https://elephant.readthedocs.io/en/latest/", None),
    "desktop": ("https://nest-desktop.readthedocs.io/en/latest/", None),
    "nest": ("https://nest-simulator.readthedocs.io/en/latest/", None),
    "gpu": ("https://nest-gpu.readthedocs.io/en/latest/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_css_files = ["css/custom.css"]
html_js_files = ["js/custom.js"]
html_theme = "sphinx_material"
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    "base_url": "https://nest-simulator.readthedocs.io/en/latest/",
    "html_minify": False,
    "html_prettify": False,
    "css_minify": True,
    # Set the color and the accent color
    "color_primary": "orange",
    "color_accent": "white",
    "theme_color": "ff6633",
    "master_doc": True,
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/nest/nest-simulator/",
    "repo_name": "NEST Simulator",
    "nav_links": [
         {"href": "https://nest-simulator.readthedocs.io/en/stable/index.html", \
                 "internal": False, "title": "NEST docs home"},
         {"href": "https://nest-simulator.readthedocs.io/en/stable/examples/index.html",\
                 "internal": False, "title": "PyNEST examples"}
         ],
    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 1,
    # If False, expand all TOC entries
    "globaltoc_collapse": True,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": True,
    "version_dropdown": False,
}

html_sidebars = {"**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]}
html_static_path = ['_static']
