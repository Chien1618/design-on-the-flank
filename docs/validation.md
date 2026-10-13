# Verification status

Version: 0.1.0. Report date: 2026-10-13.

This is an initial preview release. Do not present it as tested on every AI platform.

| Check | Status |
|---|---|
| Skill frontmatter and resource structure | Passed official quick validator and local reference checks |
| Generated downloads, ZIP contents, hashes, version consistency | Passed |
| Local Markdown links and machine-path removal | Passed |
| Example TSX parse check | Passed esbuild with platform imports external |
| Example rendered defaults and prop changes in isolated React check | Passed with React 19.2.4 and mocked Framer registration; seven props, empty strings, zero/false, and incoming width checked |
| Real Framer type definitions | Not tested |
| Framer Canvas and Preview | Not tested |
| Clean Codex skill installation and generation | Not tested |
| Clean Claude Code skill installation and generation | Not tested |
| Claude skill ZIP upload and generation | Not tested |
| ChatGPT Project setup and generation | Not tested |

Installation routes were checked against official provider documentation. Menu wording, account availability, and model behavior can change. The included example uses platform imports only; successful parsing does not establish runtime compatibility.

See the [maintainer guide](maintainer.md) for the behavioral scenarios required before claiming full platform verification.
