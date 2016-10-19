
all:

test:
	PYTHONPATH=.:$$PYTHONPATH python -m network_modularity.test.test_network_modularity
install:
	python setup.py install