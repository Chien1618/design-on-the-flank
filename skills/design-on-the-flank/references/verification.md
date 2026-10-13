# Verification and truthful reporting

## Always review

- The delivered code is complete and every import is available or disclosed.
- The export, runtime defaults, and control registration refer to the correct component.
- Each editable prop is consumed; defaults work without user-provided assets.
- `0` and `false` behave correctly; empty collections and text do not crash.
- Sizing follows the intended Framer layout; more than one instance can coexist.
- Browser-only work is guarded and resources are cleaned up.
- Existing prop keys and user-configured behavior are preserved when updating.

## Checks available to coding agents

Discover tools already present in the working environment. Do not assume the original author's folders exist, create an app solely for a parse check, or silently install dependencies. If esbuild is already available, a syntax/bundle check can keep `react`, `react-dom`, `framer`, and disclosed URL imports external. Write temporary output outside the source file. This checks syntax and bundling shape, not Framer API correctness or whether remote imports exist.

Run TypeScript checks when actual dependency types are available. A test with a mock `framer` module cannot prove real Framer type compatibility. Do not claim type correctness based on esbuild alone.

If browser rendering is available, check the meaningful behaviors and editable props. If the live Framer editor is available and authorized, inspect Canvas and Preview; use a disposable test page rather than changing production pages. Publishing is a separate action.

## User acceptance in Framer

Ask the user to make these simple observations if you cannot operate Framer:

1. The component appears after insertion without a red error.
2. Changing text, a color, and a numeric setting visibly works.
3. Toggle controls turn their feature on and off.
4. The layout is usable at a narrow width and with two instances on the page.
5. Preview interactions work using mouse/touch and keyboard where relevant.
6. Updating an existing file retains its configured content and settings.

## Report the actual level

Use an accurate short statement in the user's language. Examples:

- “Đã rà soát code; chưa chạy trong Framer.”
- “Đã kiểm tra cú pháp bằng esbuild; chưa kiểm tra kiểu dữ liệu hoặc chạy trong Framer.”
- “Đã kiểm tra các thay đổi props trong bản render thử; vẫn cần kiểm tra trong Framer.”
- “Đã thử trong Framer Canvas và Preview: [specific actions actually verified].”

Never transform a partial check into a guarantee that everything works. If a check fails, repair and repeat the relevant check; if blocked, give the exact remaining limitation in plain language.
