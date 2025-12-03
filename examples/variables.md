# Zyng variables example

変数 (`let`) と `{var}` 展開だけに絞ったシンプルな例です。

```zyng
let user = "Alice"
let project = "Zyng"

show "User: {user}" :::now
show "Working on: {project}"
show "Unknown variable: {missing_var}"
