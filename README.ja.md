## プロジェクトの現在地

Zyng は現在 **v0.1 α段階** の、かなり初期の状態です。

- Core ランタイム（`ZyngContext` / `ZyngRuntime`）と AST（`Show` / `Let`）は実装済み。
- Markdown ランナーから `python -m zyng.runner <file.md>` で実行できます。
- `tests/test_runtime.py` / `tests/test_parse_line.py` で基本的なテストを実行できます。
- 構文・仕様はまだ変わる可能性がありますが、試してもらうには十分な状態です。

詳細:

- Core 仕様（草案）: `docs/zyng_core_v0.1.md`
- 進捗とロードマップ: `PROGRESS.md`

## Examples（サンプル）

`examples/` ディレクトリに最小のサンプルがあります。

- `examples/time_log.md`  
  `let` / `show` と time メタ（`now` / `yest` / `tomo` / `at:"..."`）の例。
- `examples/variables.md`  
  変数 `{var}` 展開と、未定義変数の扱いの例。

実行例:

```bash
python -m zyng.runner examples/time_log.md
python -m zyng.runner examples/variables.md
```

## 開発に参加する人向け（メモ）

まだかなり初期段階のため、仕様は今後も変わる予定です。

- 開発用インストール:

  ```bash
  git clone https://github.com/<your-name>/zyng.git
  cd zyng
  pip install -e .
  ```

- テスト実行:

  ```bash
  pytest
  ```

- Core ランタイムと AST: `zyng/core.py`
- Markdown ランナー: `zyng/runner.py`
- Core 言語仕様（草案）: `docs/zyng_core_v0.1.md`
