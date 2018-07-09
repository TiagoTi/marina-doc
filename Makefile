main:
	cd docs && mkdocs gh-deploy

run:
	cd docs && mkdocs serve --dev-addr 0.0.0.0:8081