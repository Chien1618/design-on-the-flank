# Claude ZIP fix — 2026-10-14

- Merge each library module into one file inside the Claude ZIP (422 → 38 files) so it passes Claude's 200-file upload limit. Repository sources are unchanged.
- Fail the build above the limit and check every link and anchor inside the ZIP.

# 0.2.0

- Port the handoff into on-demand Framer, plugin and ten Three.js modules; exclude UI/UX Pro Max.
- Include all eight official GreenSock GSAP skills with MIT attribution and pinned source commit.
- Split 26 source documents into 384 linked topics with integrity mappings.
- Add Framer-specific GSAP/Three.js lifecycle, prop update and one-file delivery guidance.
- Replace the flattened chat bundle with a topic index and per-module fallback downloads.
- Rewrite onboarding and website copy around complex components. Move the card fixture out of the distributed package.

# Changelog

## Documentation update — 2026-10-13

- Rewrote the README and website copy around concrete Codex and ChatGPT steps.
- Made one-file attachment the default ChatGPT path; Project setup is optional.
- Moved maintainer details out of the main reading flow. Skill contents and download version remain 0.1.0.

## 0.1.0 — 2026-10-13

- Standardized the private workspace instructions around one-file Framer TSX delivery.
- Removed machine paths, mandatory local tooling, and fixed typography presets.
- Added shared rules for working controls, useful defaults, updates, and truthful verification.
- Added Claude ZIP and a flattened knowledge file for chat-based applications.
- Added Vietnamese setup guides, Framer insertion instructions, prompts, troubleshooting, and website copy for nontechnical users.
- Added a simple card example and a documented acceptance checklist.

This release does not include a full Three.js, WebGL, Rive, or Framer plugin library. Such requests need additional verified implementation knowledge.
