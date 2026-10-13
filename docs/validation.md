# Validation status — 0.2.0

Checked 2026-10-13.

## Packaging checks

- 26 source documents: 18 from the handoff after exclusion, 8 from the official GSAP repository.
- 20 original skills and 6 reference documents split into 384 topics. UI/UX Pro Max is excluded.
- Source manifest preserves original hashes and adapted-body hashes; topic reconstruction is checked after relative link repairs.
- Local links, topic coverage, source licenses, download hashes and exact ZIP/source equality are checked by `scripts/validate.py`.
- Chat entry is an index with public links. Its fallback downloads contain one selected module each, not the entire library.

## What this does not verify

The known upstream horizontal-scroll snippet errors are documented in the integration rules; source excerpts remain unchanged for traceability. Imported examples have not all been compiled or run. Source preservation is not a compatibility certification. GSAP/Three.js snippets must be adapted using the Framer integration reference.

The complete install → generation → Framer Canvas/Preview workflow has not been tested in fresh Codex, Claude, Claude Code or ChatGPT sessions. No live visual, GPU performance or model-generated component acceptance is claimed.

The retained legacy fixture's prior syntax/render checks used mocked Framer registration and React 19.2.4. That check does not establish Framer's React compatibility or validate advanced effects.
