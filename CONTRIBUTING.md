## Contributing to Pyleecan

Pyleecan is now managed with an open-source contribution model across:

- `origin`: Alibaba Cloud Codeup repository used for day-to-day collaboration
- `upstream`: the public GitHub repository used to stay aligned with the wider project

All changes must be developed on topic branches and merged through pull requests. Direct pushes to `master` are no longer part of the normal workflow.

## Branch Strategy

Create branches from the latest `master` tip:

- `feature/<scope>-<short-description>` for user-facing features or notable improvements
- `fix/<scope>-<short-description>` for bug fixes
- `docs/<scope>-<short-description>` for documentation-only work
- `refactor/<scope>-<short-description>` for internal restructuring without behavior change
- `release/<version>` only for coordinated release preparation

Examples:

- `feature/elmer-validation-baseline`
- `fix/gui-smoke-import-guard`
- `docs/open-source-governance`

## Default Workflow

1. Start from the latest protected branch tip.
2. Open or link an issue before non-trivial work.
3. Create a topic branch locally.
4. Keep each branch focused on one problem or one coherent improvement.
5. Update tests and documentation in the same branch as the code change.
6. Push the branch to `origin`.
7. Open a pull request into `master`.
8. Merge only after review and the quality gate pass.

Recommended sync flow:

```powershell
git checkout master
git fetch origin
git pull --ff-only origin master
git fetch upstream
git checkout -b feature/<scope>-<short-description>
```

## Documentation Management

Documentation changes are required when behavior, workflows, architecture, or contributor process change.

- `README.md`: project entry point, installation, and contributor links
- `CONTRIBUTING.md`: contribution workflow and engineering policy summary
- `CHANGELOG.md`: user-visible changes grouped under `Unreleased` and released versions
- `Doc/`: architecture notes, governance, ADRs, domain guides, and migration notes

Documentation rules:

- Keep user-facing docs accurate to the current code and supported platforms.
- Add or update a `Doc/ADR/` decision record for changes that alter architecture, public interfaces, dependency policy, or module boundaries.
- Do not merge a breaking workflow change without a migration note.

## Code Management

Code changes must follow the repository layout documented in `AGENTS.md` and the repository guidelines.

- `pyleecan/Classes/`: data models and generated objects
- `pyleecan/Methods/`: domain behavior
- `pyleecan/Functions/`: shared helpers
- `pyleecan/GUI/`: desktop UI
- `pyleecan/Generator/`: generation helpers and schema metadata
- `Tests/`: mirrored coverage and regressions

Code rules:

- Format code with Black-compatible style.
- Prefer small, reviewable commits over large mixed changes.
- Add or update targeted tests for every behavior change.
- Keep optional dependency imports lazy when the feature is not universally available.
- Avoid introducing hidden side effects at import time.

## Interface Management

The following are treated as managed interfaces:

- Public Python APIs exposed through `pyleecan.Classes`, `pyleecan.Methods`, package entry points, and documented helpers
- Serialized machine, material, simulation, and configuration data formats
- GUI workflows that users depend on for machine setup, simulation, and export
- External solver coupling contracts with FEMM, GMSH, Elmer, and related tooling

Interface rules:

- Backward-compatible changes are the default expectation.
- Breaking interface changes require an ADR in `Doc/ADR/` and an explicit migration note.
- Deprecate before removal whenever reasonably possible.
- Update regression tests when changing solver output shapes, stored axes, file schemas, or GUI entry flows.

## Module Management

Each module change should preserve clear boundaries.

- Keep business logic in `Methods/`, not in tests or docs.
- Keep reusable helpers in `Functions/`, not duplicated across modules.
- Avoid circular dependencies between `Classes`, `Methods`, `Functions`, and `GUI`.
- New modules must document purpose, ownership, dependencies, and expected tests.
- Large new areas should start with an ADR or design note in `Doc/`.

## Testing Expectations

Before opening a pull request, run a relevant subset of checks. At minimum:

```powershell
python -m pytest Tests
pytest -m star Tests
tox run -e black
pre-commit run --all-files
```

For scoped changes, run the smallest relevant subset and list the exact commands in the PR.

## Commit Guidelines

Use short, imperative commit messages. Existing prefixes remain valid and are now standardized:

- `[BF]` bug fix
- `[FEAT]` new feature
- `[DOC]` documentation only
- `[REF]` refactor
- `[TEST]` tests only
- `[CI]` automation or workflow change
- `[API]` managed interface change
- `[MOD]` module or architecture change
- `[REL]` release preparation

Each commit should stay focused. Do not mix unrelated fixes, formatting noise, and generated artifacts in the same commit.

## Pull Request Expectations

Every pull request should include:

- A concise summary of the problem and solution
- Linked issue, task, or discussion
- Affected modules and interfaces
- Exact validation commands run
- Backward compatibility impact
- Screenshots for GUI changes when applicable

Merge policy:

- Prefer squash merge for routine feature branches
- Keep release branches explicit when preparing a tagged release
- Do not merge with failing CI

## Repository Settings to Enforce

The remote repository should enforce the following on `master`:

- Protected branch with no direct push
- Pull request required for merge
- At least one reviewer approval
- Required passing quality gate before merge
- Conversation resolution before merge when review threads exist

See [Doc/Open_Source_Project_Governance_CN.md](Doc/Open_Source_Project_Governance_CN.md) for the Chinese governance baseline used by this repository.
