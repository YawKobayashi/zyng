# Zyng Progress (暫定)

このファイルは、Zyng プロジェクトの進捗と、当面のロードマップを簡潔にまとめたメモです。  
数値はあくまで目安であり、仕様や実装が進むにつれて更新していきます。

---

## 1. 大きなゴールと進捗感

- **Goal 0: フレーミング＆哲学**
  - 内容: WHY_ZYNG / 設計思想 / 目的と非目的の整理
  - 状態: 主要な文書と考え方は出そろっており、大きくブレない土台ができている。
  - 進捗目安: **80%**

- **Goal 1: v0.1 Core 言語のコア**
  - 内容: `show` / `let` / time メタ、Context / Runtime / runner、テスト、最小限のドキュメント。
  - 状態:
    - Core runtime ＋ AST（`Show` / `Let`）実装済み。
    - Markdown runner 実装済み（`python -m zyng.runner <file.md>`）。
    - pytest ベースの最小テスト（runtime / parse_line）追加済み。
    - Core 仕様草案（`docs/zyng_core_v0.1.md`）作成済み。
    - Examples（`examples/`）に最小サンプルあり。
    - PyPI に `zyng==0.1.0` として公開済み。
  - 進捗目安: **90%**

- **Goal 2: v0.2 他人が輸入できる最小単位**
  - 内容: examples の拡充 / Core 仕様 doc の肉付け / 導入ガイド（他開発者向け）。
  - 状態:
    - 基本的な examples と spec はすでに存在。
    - 「他人が設計に参加しやすい説明」はまだ薄い。
  - 進捗目安: **20%**

- **Goal 3: v0.3 LLM フロントエンド実用ライン**
  - 内容: Zyng から LLM（API / ローカル）を実際に叩くサンプルや薄いラッパー。
  - 状態: 構想レベル。コードとしてはまだほぼ手付かず。
  - 進捗目安: **5%**

---

## 2. 完了したこと（v0.1.0）

v0.1.0 として区切れるレベルで完了している項目。

- Core:
  - `ZyngContext` / `ZyngRuntime` と AST（`Show` / `Let`）の実装。
  - Markdown runner（`zyng/runner.py`）からの実行パス。
- Parser / Lexer（v0.1 時点）:
  - `show "TEXT" :::time-meta` / `let name = "VALUE"` を扱う簡易パーサ。
- Tests:
  - `tests/test_runtime.py`（`Let` → `Show` の基本動作）。
  - `tests/test_parse_line.py`（`parse_line_to_statement` の基本動作）。
- Docs:
  - WHY_ZYNG（設計思想）
  - Core 仕様草案: `docs/zyng_core_v0.1.md`
  - README / README.ja に Project status / Examples / Contributors 情報。
- Examples:
  - `examples/` に、Core 構文と time メタを使った最小サンプル。
- 配布:
  - `pyproject.toml` の version を **0.1.0** に更新。
  - PyPI に `zyng==0.1.0` を公開。

---

## 3. 直近 TODO（v0.1.x / v0.2）

当面は、0.1.0 のコアを壊さずに精度を上げつつ、  
「他人が参加しやすいレベル」までドキュメントと実装を整える。

### 3-1. v0.1.x ライン（品質向上）

- [ ] `core.py` / `runner.py` のコメント整理  
      - 設計意図と将来の拡張ポイント（Expr / 本格 Lexer など）を一行コメントで明文化。
- [ ] 簡易 Lexer 改善  
      - 文字列中の `:::` を誤検知しないようにする（`show "Hello ::: World"` 問題の緩和）。
      - 将来的に `lexer.py` へ切り出せる構造にしておく。
- [ ] テスト強化  
      - 未定義変数 `{missing}` の扱いなど、エッジケースを追加。
      - time メタ（`now` / `yest` / `tomo` / `at:"..."`）の組み合わせテスト。

### 3-2. v0.2 ライン（他開発者が輸入しやすい形）

- [ ] `docs/zyng_core_v0.1.md` の肉付け  
      - もう少し実例を増やし、設計哲学との対応関係を明示。
- [ ] `examples/` の拡充  
      - 少し長めの「タイムラインログ」例。
      - 将来の LLM 連携を見据えた「疑似ワークフロー」例。
- [ ] 導入ガイド（開発者向け）  
      - 「自分のプロジェクトに Zyng を埋め込むには？」という視点のガイドを docs に追加。
- [ ] Issues / TODO の公開整理  
      - Lexer 強化 / 新構文候補 / LLM 連携などを Issue として切り出し、他人が参加しやすい形にする。

---

## 4. メモ

- 進捗％は「感覚のスナップショット」であり、厳密な計測ではない。
- 仕様や実装を変えたときは、ここも一緒に更新して「いま何を目指しているか」を同期させる。
- 将来、他の開発者にプロジェクトを渡すときの「現在地の説明」としても利用する。
- v0.1.0 は「Core が一応まともに動いて、PyPI にも出た最初の区切り」として扱う。
