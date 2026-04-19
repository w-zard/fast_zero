# fast-zero

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.
For scanners that don't support `uv.lock` yet, `requirements.txt` is exported
from the lockfile for compatibility.

```bash
uv sync --group dev
uv run task run
uv run task test
uv export --format requirements.txt --no-dev --no-editable --no-emit-project --locked -o requirements.txt
```
