# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .

ifdef $(READTHEDOCS_OUTPUT)
BUILDDIR	  =$(READTHEDOCS_OUTPUT)/html
else
BUILDDIR      = _build
endif

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
#	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -vv
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
commit: 
	git add .
	git commit -m "${MSG}"
	git push

rtd: 
	cp -rv *rst scripts Makefile make.bat README.md datas _images _static conf.py images index.rst .readthedocs.yaml requirements.txt ../github_howto_jsonrpc_api/
	cd ../github_howto_jsonrpc_api; make commit MSG="$$\(git log -1 --pretty=format:\%B\)"

livehtml:
	sphinx-autobuild --port=0 --open-browser "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)