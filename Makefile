.PHONY: doc

doc:
	make -C docs html
	@echo "open file://`pwd`/docs/_build/html/index.html"
