# Zyng Project

Zyng は、「人間が読めて、機械が厳密に扱える」Zynglish ベースの言語／ツールチェインです。  
まずは **README 内の ```zyng コードブロックだけを実行できるツール** として開発を進めています（Phase A）。

- Phase A のゴール:  
  - README をそのまま「軽いスクリプト／テスト」として実行できるようにすること  
  - コア予約語を 20 語程度に抑えた最小言語として形にすること

---

## Demo: Run this README

この README 自体が Zyng のデモになっています。  
以下の ```zyng コードブロックだけが実行され、通常の文章は無視されます。

```zyng
show "Hello from README" :::important
```

（実行方法は現時点のスクリプト構成に応じて、例: `python zyng_v0.4_md.py README.md` など）

---

## Design Principles

Zyng / Zynglish は、「人間が読めて、機械が厳密に扱える」簡略英語ベースの言語です。  
仕様書・テスト・公文書・日常文を、ひとつのコアから書けることを目標に設計しています。

### 1. Core の意味は削らない

- 動詞や時間語などの **意味のインベントリは削らずに設計** する。
- 一方で、綴りは `yest` / `tomo` のように **短く・発音可能な形に最適化** してよい。
- つまり、「何を表現できるか」は守り、「どう綴るか」を削る。

### 2. 三層構造（Core / State / Nature）

- **Core**  
  - 約 20 語程度の予約語と、最小限の文法から成る「意味のコア」。  
  - 例: `show`, `read`, `write`, `use`, `let`, `yest`, `tomo`, `now` など。
- **State**  
  - 公文書・仕様・契約など、「曖昧さを嫌うテキスト」を書くためのレイヤー。  
  - Core の語彙と、厳格に管理された略語のみを使用する。
- **Nature**  
  - 物語・会話・ミームなど、創作的なテキストのためのレイヤー。  
  - 短縮や造語を制限しない。広く使われた表現は将来 Core / State に昇格しうる。

### 3. 記法は `: / :: / :::` に集約する

- `:` は単語の属性、`::` は列（リスト）の属性、`:::` は文全体のメタ情報・制御を表す。
- 制御構文やモード指定をできるだけ `:::` に寄せ、**新しいキーワードを増やさない**。
- 例:  
  - `Mi use pool :::yest`  
  - `show result :::json`  
  - `show log :::test`

### 4. 人間が読めて、機械が厳密に扱える

- 文は、英語に似た形で「なんとなく読める」ことを重視する。  
- 同時に、パーサーとツールチェインが構文と意味を **一意に解釈できる** ことを優先する。
- README や仕様書をそのまま実行・検証できることを、最初のユースケースとして設計する。

### 5. 英語「らしさ」と、一貫性のバランス

- Zynglish は英語をベースにするが、「正しい英語」を目指すのではなく、  
  **論理と一貫性を優先した簡略英語** を目指す。
- 例: 場所やサービス、API などの利用をすべて `use` で統一する。  
  - `Mi use pool :::yest`  
  - `use db :::now`
- 英語としての違和感よりも、「少ない語彙で同じパターンを繰り返せるか」を重視する。

---

## Core Keywords (v0.1)

Zyng / Zynglish のコア予約語一覧です。  
このうち ✓ が付いているものは、Phase A（README Runner + 変数 + read/write/use）で実際に使用されるサブセットです。

### Literals

| Keyword  | Category | Phase A | 説明 |
|---------|----------|:-------:|------|
| `true`  | literal  |   ✓     | 真を表す論理値。条件分岐やフラグとして使う。 |
| `false` | literal  |   ✓     | 偽を表す論理値。条件分岐やフラグとして使う。 |
| `null`  | literal  |   ✓     | 値が存在しない状態を表す特殊値。Python の `None` に相当。 |

### Core Verbs

| Keyword  | Category | Phase A | 説明 |
|---------|----------|:-------:|------|
| `show`  | verb     |   ✓     | 値やメッセージを表示・ログ出力する。`show "Hello"` のように使う。 |
| `read`  | verb     |   ✓     | ファイルやストリームなどからデータを読む。`read "users.json" as users`。 |
| `write` | verb     |   ✓     | データをファイルやストリームに書き出す。`write users to "users.json"`。 |
| `use`   | verb     |   ✓     | モジュール・リソース・場所・サービスを利用する。`use db`, `Mi use pool :::yest`。 |
| `let`   | verb     |   ✓     | 変数を導入・代入する。`let user = "Alice"` のように使う。 |

### Time Words

| Keyword  | Category  | Phase A | 説明 |
|---------|-----------|:-------:|------|
| `yest`  | time word |   ✓     | 「昨日」を表す時制属性。`:::yest` を付けて昨日の出来事を示す。 |
| `tomo`  | time word |   ✓     | 「明日」を表す時制属性。`:::tomo` を付けて明日の出来事を示す。 |
| `now`   | time word |   ✓     | 「今この瞬間」を表す。`:::now` で現在時点の操作・状態を明示する。 |

（`today` は「時制指定なしのデフォルト」として概念的に存在するが、通常は明示的には書かない。）

### Control Keywords (reserved for future versions)

| Keyword     | Category | Phase A | 説明 |
|------------|----------|:-------:|------|
| `if`       | control  |         | 条件分岐の開始を表す。将来のバージョンで導入予定。 |
| `else`     | control  |         | `if` の条件が偽のときに実行する分岐。将来導入予定。 |
| `for`      | control  |         | 繰り返し処理（反復）を表す。将来導入予定。 |
| `while`    | control  |         | 条件が真の間、処理を繰り返すループ構文。将来導入予定。 |
| `return`   | control  |         | 関数から値を返して処理を終了する。将来導入予定。 |
| `break`    | control  |         | ループを途中で抜けるための制御。将来導入予定。 |
| `continue` | control  |         | ループ内で残り処理をスキップし、次の反復へ進む。 |

### Structure Keywords (reserved)

| Keyword | Category  | Phase A | 説明 |
|--------|-----------|:-------:|------|
| `func` | structure |         | 関数定義を行うキーワード。`func name ... { ... }` 形式を想定。 |
| `type` | structure |         | 型や構造体・レコードを定義するためのキーワード。 |

---

## Phase A Status

Phase A では、上記 Core Keywords のうち主に

- `true`, `false`, `null`
- `show`, `read`, `write`, `use`, `let`
- `yest`, `tomo`, `now`

だけを実装・利用します。  
それ以外のキーワード（`if`, `func` など）は **予約されていますが、まだ構文としては利用できません**。

今後は：

1. README 内の ```zyng ブロックを安定して実行できる CLI ツールとして整える  
2. Core 文法のサブセット（Phase A 用ミニ文法）を仕様として固定する  
3. サンプルリポジトリとテスト（README as Code）を整備する  

という順番で進めていきます。
