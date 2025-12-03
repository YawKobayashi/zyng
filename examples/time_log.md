# Zyng time log example

このファイルは、Zyng の Core 構文（`let` / `show` / time メタ）の最小サンプルです。

```zyng
let user = "Alice"
show "Session started for {user}" :::now

show "Yesterday I tested Zyng" :::yest
show "Tomorrow I will refactor the parser" :::tomo
show "Exact timestamp example" :::at:"2025-12-03T21:00:00+09:00"
