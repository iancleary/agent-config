# Release Process

This repository uses UTC CalVer `YYYY.MM.DD.XX`. The daily serial starts at
zero, and Git tags are the version source.

Use `create-release-process` to maintain this workflow. Use the repository-local
`cut-release` skill for an ordinary release.

```sh
uv run scripts/release.py check --json
uv run scripts/release.py plan --json
uv run scripts/release.py run --dry-run --version YYYY.MM.DD.XX --expected-head COMMIT --expected-config SHA256 --json
uv run scripts/release.py run --apply --version YYYY.MM.DD.XX --expected-head COMMIT --expected-config SHA256 --json
```

Fetch origin tags before planning. Pass the plan's exact `version`,
`target_commit`, and `config_sha256` to dry-run and apply. The runner checks
that `main` is clean and matches `origin/main`, validates the CalVer value,
pushes an annotated tag, and creates a GitHub release with generated notes.
