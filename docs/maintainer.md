# Maintaining the package

The installable entry point is `skills/design-on-the-flank/SKILL.md`. It routes to small topic files under `references/library/`. Do not flatten the library into the entry skill or read every topic during a component task.

## Sources

The supplied handoff contributes 12 skills and 6 references after excluding UI/UX Pro Max. GreenSock contributes 8 official skills. See [attribution](../skills/design-on-the-flank/ATTRIBUTION.md) and `source-manifest.json` for provenance and hashes.

To regenerate imported topics, pass explicit local source paths:

```sh
python3 scripts/import_library.py --handoff /path/to/handoff.md --gsap /path/to/gsap-skills --framerlabs /path/to/framerlabs
```

Review upstream content and licensing before updating. The importer repairs relative links and splits on headings outside code fences. It rejects unexpected source counts and locally edited topic bodies. Keep upstream corrections in a reviewed import change; put Framer adaptation guidance in `references/advanced-integration.md`.

## Build

Update VERSION, matching SKILL metadata and the changelog, then run:

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

Python's standard library is sufficient. ZIP timestamps are deterministic. The ZIP includes the whole library; the chat entry contains a router and public links. Module TXT downloads are an offline fallback for one selected subject, with common Framer rules and the upstream license. Do not attach all modules to every chat.

The old card is retained only as `tests/fixtures/FlankCard.tsx` for structural regression checks. It is not distributed as a user example. When needed, `node scripts/check-example.cjs /path/to/node_modules` requires existing esbuild, react and react-dom; it mocks Framer and cannot verify the platform.

## Release and acceptance

Commit sources and rebuilt downloads, push, and verify public artifact hashes. Keep [validation status](validation.md) accurate. Updating GitHub does not update already installed skills.

Before declaring live compatibility, test a fresh install on each claimed platform: request a particle field with editable uniforms, a GSAP scroll scene, conversion of existing code and an update preserving configured props. Exercise two instances, resize, reduced motion, missing assets and cleanup in Framer Canvas/Preview. Record actual prompts, output and failures. Plugin tasks require their own workflow.

Original package material uses the root usage license; upstream documents keep their MIT rights and notices. Do not apply the package redistribution restriction to MIT documents.
