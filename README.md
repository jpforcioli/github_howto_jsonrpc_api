# How to get the HTML version of this?

- [How to get the HTML version of this?](#how-to-get-the-html-version-of-this)
  - [Linux with python3](#linux-with-python3)
    - [Clone the git project](#clone-the-git-project)
    - [Install sphinx](#install-sphinx)
    - [To generate the HTML documentation](#to-generate-the-html-documentation)
    - [To read the HTML documentation](#to-read-the-html-documentation)
  - [Readthedoc](#readthedoc)
  - [Build HTML files using Docker](#build-html-files-using-docker)
    - [To read the HTML documentation from Docker Server](#to-read-the-html-documentation-from-docker-server)

## Linux with python3

### Clone the git project

```shell
git clone https://git.fndn.fortinet.net/fortimanager/howto_jsonrpc_api.git
```

### Install sphinx

```shell
cd howto_jsonrpc_api
mkdir -p _build
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pip --upgrade
python3 -m pip install sphinx
python3 -m pip install sphinx_tabs
python3 -m pip install sphinx_toolbox
python3 -m pip install sphinxcontrib.images
python3 -m pip install sphinx_copybutton
python3 -m pip install sphinx_design
# Ignore the possible error produce by the above command
python3 -m pip install sphinx_book_theme
```

### To generate the HTML documentation

```shell
make html
```

### To read the HTML documentation

Now you can open file:

```txt
_build/html/index.html
```

with your browser.

## Readthedoc

```txt
cp -rv *rst Makefile make.bat README.md datas _images _static conf.py images index.rst .readthedocs.yaml requirements.txt ../github_howto_jsonrpc_api/
```

## Build HTML files using Docker

```shell
cd howto_jsonrpc_api
docker build -t sphinx-docs .
docker run --rm -p 8000:8000 sphinx-docs
```

### To read the HTML documentation from Docker Server

Now you can open following link in your browser:

[http://127.0.0.1:8000/index.html](http://127.0.0.1:8000/index.html)