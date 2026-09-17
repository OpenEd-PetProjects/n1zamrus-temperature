.PHONY: test

test:
	python3 -m unittest discover --start-directory tests --pattern 'test_*.py' --verbose
