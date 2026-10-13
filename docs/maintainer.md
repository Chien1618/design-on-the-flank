# Maintainer guide

## Source of truth

Edit `skills/design-on-the-flank/SKILL.md`, its references, and its example. Edit the short ChatGPT wrapper in `adapters/chatgpt-instructions.txt`. Do not edit generated files in `downloads/` manually.

Use `VERSION` and the matching skill metadata version. Rebuild and validate:

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

For the example, when dependencies are already available, run `node scripts/check-example.cjs /path/to/node_modules` with a directory containing esbuild, react and react-dom. This uses mocked Framer registration and does not replace Canvas/Preview testing.

Python 3 and its standard library are sufficient for packaging. The ZIP uses a fixed timestamp so unchanged source produces the same bytes. All downloads share the same content version. The knowledge file inlines every reference and the example because a chat application cannot be expected to follow local skill links.

## Release

1. Update the source, version, changelog, and real verification status.
2. Run the build, validator, and meaningful checks for any example changes.
3. Commit source and downloads. The downloads directory is intentionally tracked for website use.
4. Push to the GitHub repository and verify every public download works without login.
5. Tag a release after live application testing. A release can attach the ZIP, instructions, knowledge, example, and manifest from `downloads/`.
6. Upload the same files to the website, use `web/README.md` to map pages/buttons, and show the version.

Do not label an untested application “verified”. Keep a dated record with the application/model, prompt, generated TSX, checks, and issues. New versions require users to update their installed/uploaded copies; there is no automatic sync.

## Repository identity

The install guides target `Chien1618/design-on-the-flank` on branch `main`. If the repository moves, update both platform install prompts and the website raw-download example. No account identifier is embedded in the portable skill itself.

## Usage terms

`LICENSE.md` grants end users permission to use the skill and example for personal/commercial component work, while reserving redistribution of the collection. It does not declare the repository open source. The owner can choose broader terms before a later release.

## Scope deliberately left for later

The private source's machine paths, local esbuild location, and BT Grotesk breakpoint preset are not included in the public skill. This release does not bundle third-party skill libraries, paid assets, original workspace components, API credentials, or a full Three.js/WebGL reference library. The new example is original to this package.

## Behavioral acceptance scenarios

For each supported AI application, start with a fresh installation/Project and record actual results:

1. **New card:** ask for text, colors, padding, corners, and a text toggle. Verify the output is one file and each control works in Framer.
2. **Conversion:** supply a React sample with local CSS. Verify the result includes styles in the TSX and explains any changed behavior.
3. **Update:** change one visual detail on a configured instance. Verify prop keys and saved content survive.
4. **No terminal:** ask in a plain chat environment. Verify the AI returns complete code and does not claim it ran checks.
5. **Missing asset:** request a component needing an uploaded image. Verify the component shows a useful empty state and explains the image selector.

Check two instances, narrow layout, keyboard interaction when applicable, and Preview behavior. Structural validation alone does not complete these scenarios.
