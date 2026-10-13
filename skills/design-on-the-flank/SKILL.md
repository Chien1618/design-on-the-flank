---
name: design-on-the-flank
description: Create, convert, or update Framer Code Components as one complete paste-ready TSX file with working Property Controls. Use for component requests, adapting React samples to Framer, and fixing existing Framer component behavior. Intended for people who do not write code.
metadata:
  version: "0.1.0"
---

# Design on the Flank

Turn the user's description into one complete Framer Code Component that they can copy into Framer and customize visually. Follow the user's language. Explain setup in everyday words.

## Output contract

- Deliver one self-contained `.tsx` file per requested component. Keep styles and helper functions in that file. Do not scaffold an app or require a build step for the end user.
- Include React/Framer imports, an exported component, layout annotations where appropriate, runtime defaults, and `addPropertyControls` attached to the same component.
- Every advertised control must change the actual output or behavior. Use plain labels and only controls useful for this component.
- Show useful sample content on first insertion. Handle empty content, absent optional assets, and narrow widths without crashing.
- Prefer React, Framer, CSS, and browser capabilities. If a feature needs an external package, verify its Framer-compatible import and disclose it. Do not claim one-file output means offline or dependency-free.
- Do not require private keys in client-side code. For features requiring a backend, explain the additional service; provide a clearly labeled demo only if useful.
- Produce complete code, never ellipses, omitted sections, a patch alone, or “keep the rest unchanged” for a user who must copy and paste.

## Workflow

1. Identify the content, appearance, interaction, and settings the user wants. Ask only about missing information that materially changes the result. Choose reasonable visual defaults for the rest.
2. For edits or conversions, read the supplied source first. Preserve names, prop keys, saved instance behavior, callbacks, and requested animation mechanisms. If the source is unavailable, ask for the current complete code before claiming to preserve it.
3. Read [the Framer contract](references/framer-contract.md). For animation, CMS, or update bugs, also read [update and troubleshooting guidance](references/updates-and-effects.md).
4. Implement the smallest complete component satisfying the request. Use [FlankCard.tsx](assets/FlankCard.tsx) only as a small structural example, not a mandatory visual style.
5. Follow [verification guidance](references/verification.md). Check what the environment actually permits. Keep compile, type, rendered behavior, and live Framer verification distinct.
6. Return the file or one complete `tsx` code block, followed by a short note explaining how to insert it, which settings are available, any required assets/setup, and what was checked.

## Adapt to the current AI application

- With file tools: create or update the requested TSX file and provide a clickable file. If the interface cannot expose its contents conveniently, also provide the complete code block.
- With chat only: supply the full code in one block. Do not ask the user to assemble pieces, install packages in a terminal, or create a development project.
- With execution tools: run relevant checks when possible. Without those tools, inspect the code and say it has not been compiled or run in Framer.
- If reference files cannot be opened, say so and ask for the bundled knowledge file. Never pretend to have read unavailable instructions.

## Updating existing components

Update the existing file by default. Preserve the exported component identity, props, CMS selectors, Rive bindings, accessibility labels used as hooks, and callbacks unless a requested change requires otherwise. Add new props with safe defaults. Saved instances can retain old values even when defaults change.

## Handoff to a nontechnical user

Use short steps: open the Framer project → Assets → Code → create a code file → replace its starter code with the entire TSX → add the component to the page → select it and adjust settings → open Preview. Menu wording may vary.

When something fails, ask for the exact error or a screenshot and the complete current code. Return the corrected whole file. Describe controls by their visible labels, not internal variable names.

The success target is a working Framer component. Do not promise that untested output is guaranteed to work, publish the user's site, or modify unrelated projects as part of this skill.
