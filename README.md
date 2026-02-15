# LLM

Hands-on experiments and code while following **Build a Large Language Model (From Scratch)** by **Sebastian Raschka** (Manning).

## Lab

The `Lab/` directory holds Jupyter notebooks (e.g. `main.ipynb`) for running and tweaking the book’s examples. Use the project’s venv as the kernel so PyTorch (ROCm) and other deps are available.

## Setup

**Prerequisites:** [uv](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh` or `pip install uv`).

From the project root:

```bash
uv sync
```

Activate the venv: `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\Activate.ps1` (Windows PowerShell). Run code with `python main.py` or `uv run python main.py`.

## Add dependencies

```bash
uv add <package-name>
```

PyTorch is installed from a ROCm index (see `pyproject.toml`); other packages come from PyPI.

## Troubleshooting (AMD / ROCm)

**`HIP error: invalid device function`** — The PyTorch ROCm wheel was built for different GPU architectures than yours (e.g. RX 7800 XT is gfx1101). Use a newer index that supports your arch: in `pyproject.toml`, change the PyTorch index URL to `https://download.pytorch.org/whl/rocm6.4` (or the latest ROCm version listed on [pytorch.org](https://pytorch.org)), then run `uv sync` again.
