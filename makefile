.PHONY: start
start:
	@echo "nothing yet..."
	

.PHONY: format
format:
	@isort cheap/ && \
	flake8 cheap/ --indent-size=2 --select=F,E112,E113,E304,E502,E702,E703,E71,E72,E731,W191,W6 --statistics -j4 && \
	mypy cheap/ --ignore-missing-imports


