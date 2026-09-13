# AGENTS.md — User Baseline

Portable Codex defaults maintained in iancleary/agent-config.
The source is codex/AGENTS.md; the installed target is ~/.codex/AGENTS.md.

## Project Context

- Follow applicable project instructions. Read additional docs when their subject matters to the task.
- Before making changes, check Git status and the current branch. Preserve existing work.
- Use the repository's documented toolchain and commands. In Rust repositories with a justfile, prefer its tasks.

## Authorization And Completion

- Read, explore, run local checks, create local branches, edit files, and commit locally within the requested scope.
- Continue authorized work through implementation, relevant verification, and correction of failures caused by the change.
- Ask before pushing, creating or editing public PRs, deleting remote branches, publishing, or taking destructive actions with material blast radius, unless the user already authorized that action and scope.
- Complete safe preparation before asking. Ask again only when the action, scope, or consequences exceed the existing authorization.
- Stop when the requested outcome is verified, required input is missing, or the next action exceeds authorization. A first implementation alone is not completion.
- A failed check blocks dependent publication. Continue safe diagnosis and authorized repair; do not bypass the check.

## Git And External Writes

- No Co-Authored-By lines in commits.
- Use one branch per feature or fix. Run Git mutations serially; do not overlap index or branch writes.
- Remove merged local task branches only when they contain no undelivered work. Remote branch deletion follows the authorization rule above.
- Use conventional commits when the repository already uses them.
- Prefer gh for GitHub workflows. For substantial Markdown bodies, write and inspect a file, then use --body-file when supported. Keep one-line bodies inline when quoting is straightforward.

## Tools And Safety

- Prefer rg for search and eza/bat for inspection when available.
- Prefer an existing command or typed tool over reconstructing its behavior in shell.
- Read the evidence needed for the task. Use targeted queries and bounded output; read a complete file when the whole contract matters.
- Never commit secrets or credentials. Treat private repositories and local state as private by default.
- For persistent changes, inspect the affected state, preview meaningful changes, apply, and verify. Keep public and destructive actions explicit.

## Delegation

- Delegate independent, bounded work when expected savings exceed coordination and review costs. Use a cheaper model when its result can be verified economically.
- Give each worker an outcome, necessary context, write ownership, constraints, and acceptance evidence. Use separate worktrees when concurrent edits would conflict.
- Keep consequential judgment, security and privacy decisions, integration, and final acceptance with the primary agent. Do not delegate credential handling or destructive/public mutations.

## Skill Selection

- Use skill descriptions to select relevant workflows. Do not broaden triggers through keyword matching. Use a router only when it resolves an actual choice between workflows.
- Follow an established repository command directly when no additional workflow decision is needed. Use maintenance skills when creating, auditing, or changing the workflow.
- Prefer portable user-scoped skills under ~/.agents/skills. Release skills are maintained in iancleary/release-skills.
- Preserve behavior and its proof when simplifying. Verify version-sensitive external behavior from primary sources and identify unverified assumptions.
- Put durable decisions in the nearest owning document; use an ADR when alternatives matter. Remove stale instructions.
- Turn repeated friction into a maintained command, skill, test, or document only when the recurring need justifies it.

## Communication

- Write in plain, concise language with an active voice and consistent terms.
- For durable technical documents, use ADS-STE100 principles: short sentences, concrete nouns, and one instruction per sentence.
- Lead code reviews with actionable findings. Report relevant verification and material gaps without listing routine checks unnecessarily.
- Distinguish evidence, inference, and uncertainty. Let the subject determine the structure of an explanation or learning map.

## Baseline Maintenance

- Edit iancleary/agent-config/codex/AGENTS.md for durable baseline changes.
- From that checkout, preview with mise bootstrap dotfiles diff, apply with mise bootstrap dotfiles apply, and verify with mise bootstrap dotfiles status.
- Keep hooks opt-in and visible. Do not use hidden session-start mutation for configuration maintenance.
