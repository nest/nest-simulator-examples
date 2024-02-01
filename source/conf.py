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
    "nbsphinx"
]

templates_path = ['_templates']
exclude_patterns = []

nbsphinx_execute = "never"
nbsphinx_prolog =  """
{% set docname = env.doc2path(env.docname, base=None) %}

.. only:: html

----
{{ docname }}

 Run this example as a Jupyter notebook:

  .. card::
    :width: 25%
    :margin: 2
    :text-align: center
    :link: https://lab.ebrains.eu/hub/user-redirect/\
git-pull?repo=https%3A%2F%2Fgithub.com%2Fnest%2Fnest-simulator-examples&urlpath=lab\
%2Ftree%2Fnest-simulator-examples%2Fnotebooks%2Fnotebooks%2Ffilepath.ipynb&branch=main
    :link-alt: JupyterHub service

    .. image:: https://nest-simulator.org/TryItOnEBRAINS.png


.. grid:: 1 1 1 1
   :padding: 0 0 2 0

   .. grid-item::
     :class: sd-text-muted
     :margin: 0 0 3 0
     :padding: 0 0 3 0
     :columns: 4

     See :ref:`our guide <run_jupyter>` for more information and troubleshooting.

---

.. raw:: latex

  \\nbsphinxstartnotebook{The following document was created from 
  \\texttt{\strut{}{{ docname }}}:}

"""
nbsphinx_kernel_name =  "ebrains-23.09"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
