install:
	poetry install

build:
	poetry build

publish:
	poetry publish

lint:
	poetry run flake8 src

blast:
	poetry run blast

prepare:
	poetry run prepare

mapping:
	poetry run mapping

primer:
	poetry run primer

splitter:
	poetry run splitter

start-gui:
	poetry run start-gui
