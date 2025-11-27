## 01: セットアップ

### プロジェクトの大枠

```bash
uv init --app flask_simple_api
cd flask_simple_api
mkdir src
mkdir src/flask_simple_api
cd src/flask_simple_api
touch __init__.py __main__.py routes.py
cd ../..
```

- `src`を含む構成を採用。
- 必要なファイルも作成。


### uvの設定

```bash
uv add flask
uv add --dev ruff mypy pytest
```
- `.venv`と`uv.lock`が作成される。
- `pyproject.toml`も変更される

### `pyproject.toml`の手動編集

```toml
[tool.uv]
package = false
```

- 上記を書き込む。

### `pyproject.toml`の全貌

- ...comming soon
