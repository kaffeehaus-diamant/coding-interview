################
Coding Interview
################


Required Software
=================

- `Python >= 3.10 <https://www.python.org/downloads/>`_
- `Node.js >= 17 <https://nodejs.org/en/download/>`_
- A text editor of your choice, e.g. `Visual Studio Code <https://code.visualstudio.com>`_


Getting Started
===============

Install the required JavaScript packages::

    # npm install

Compile the TypeScript and SCSS files::

    # npm run build

Setup the python environment on Unix::

    # python3 -m venv venv
    # . venv/bin/activate
    (venv) # python -m pip install --upgrade pip
    (venv) # pip install -r requirements.txt

or on Windows::

    > python -m venv venv
    > venv\Scripts\activate.bat
    (venv) > python -m pip install --upgrade pip
    (venv) > pip install -r requirements.txt

Start the development server::

    (venv) # python manage.py runserver

Go to http://localhost:8000/


Development
===========

Run the ``watch-css`` and ``watch-js`` commands to automatically recompile the
SCSS and TypeScript files when you change them. In Visual Studio Code you can
do this by pressing ``Ctrl`` + ``Shift`` + ``B`` (on Windows) and selecting the
appropriate build task.

Alternatively, you can just run::

    # npm run watch-css

and::

    # npm run watch-js

in two separate console windows.


Tasks
===========
* Create models for Author and Book
* Authors have a name and rank
* Books have a name, number of pages and a connection to an author
* Authors write books, so Author needs to have a connection to Book and for convenience a property "books"
* Add some authors and their books
* Under the API endpoint "/api/authors/books" expose all authors with their corresponding books

Optional
----------
* Fetch data from endpoint /api/products/ in React
* Render List of Product names in Frontend Content component