# Zyng Core v0.1（草案）

## 1. このドキュメントの目的
- Zyng v0.1 時点での「Core 言語」の構文と振る舞いをまとめる
- 実装（core.py / runner.py）の設計意図を軽く説明する

## 2. 文の種類（Statements）

### 2.1 show 文
- 形式: `show "TEXT" :::time-meta?`
- 例:
  - `show "Now message" :::now`
  - `show "Exact time" :::at:"2025-12-03T21:00:00+09:00"`
- {var} 展開のルール:
  - `{name}` は Context.variables["name"] を展開
  - 未定義変数は `{name}` のまま残す

### 2.2 let 文
- 形式: `let name = "VALUE"`
- 例:
  - `let user = "Alice"`
- v0.1 では VALUE は常に文字列リテラル
- 将来は Expr（式）に拡張予定

## 3. time メタ

- サポートする値:
  - `now`
  - `yest`
  - `tomo`
  - `at:"ISO8601"`
- Runtime 上の扱い:
  - `now/yest/tomo` は `[now]` / `[yest]` / `[tomo]` のようなプレフィックスになる
  - `at:"..."` はそのまま `[at:"..."]` の形式で出力する

## 4. 実行モデル（簡単な説明）
- Markdown 内の ```zyng ブロックから行を抜き出す
- 行 → parse_line_to_statement → Statement
- Statement を ZyngRuntime + ZyngContext で順に実行する
