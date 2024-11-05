build:
	uv build --no-sources

fmt:
	uv run ruff check --select I --fix .
	uv run ruff format .

lint:
	uv run ruff check .
	uv run ruff format --check .

sync:
	uv sync --compile

lock:
	uv lock

upgrade:
	uv lock --upgrade

all: lock sync
	make fmt
	make lint
	# make test	

test: lint
	uv run pytest -v .
