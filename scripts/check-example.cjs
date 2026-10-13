// Maintainer-only check. Pass a node_modules directory containing esbuild,
// react and react-dom. Does not install packages or assert live Framer support.
const assert = require('node:assert/strict')
const path = require('node:path')
const fs = require('node:fs')
const os = require('node:os')
const { createRequire } = require('node:module')

async function main() {
    if (!process.argv[2]) throw new Error('Usage: node scripts/check-example.cjs /path/to/node_modules')
    const dependencies = createRequire(path.resolve(process.argv[2], '..', 'package.json'))
    const esbuild = dependencies('esbuild')
    const React = dependencies('react')
    const { renderToStaticMarkup } = dependencies('react-dom/server')
    const temp = fs.mkdtempSync(path.join(os.tmpdir(), 'flank-example-'))
    try {
        const outfile = path.join(temp, 'card.cjs')
        await esbuild.build({
            entryPoints: [path.resolve(__dirname, '../tests/fixtures/FlankCard.tsx')],
            outfile, bundle: true, platform: 'node', format: 'cjs',
            plugins: [{ name: 'test-platform', setup(build) {
                build.onResolve({ filter: /^react$/ }, () => ({ path: dependencies.resolve('react'), external: true }))
                build.onResolve({ filter: /^framer$/ }, () => ({ path: 'framer', namespace: 'mock' }))
                build.onLoad({ filter: /.*/, namespace: 'mock' }, () => ({
                    contents: 'export const ControlType = {String:"String",Boolean:"Boolean",Color:"Color",Number:"Number"}; export function addPropertyControls(component, controls) {component.__controls = controls;}',
                    loader: 'js',
                }))
            }}],
        })
        const Card = require(outfile).default
        const render = (props = {}) => renderToStaticMarkup(React.createElement(Card, props))
        assert.match(render(), /Your next idea starts here/)
        assert.match(render(), /Properties panel/)
        assert.match(render({ title: 'Changed title', body: 'Changed description' }), /Changed title.*Changed description/)
        assert.doesNotMatch(render({ showBody: false }), /<p/)
        assert.doesNotMatch(render({ title: '', body: '' }), /Your next idea|Properties panel/)
        const changed = render({ background: '#123456', textColor: '#abcdef', padding: 0, radius: 0 })
        for (const value of ['background:#123456', 'color:#abcdef', 'padding:0', 'border-radius:0']) assert.ok(changed.includes(value), value)
        assert.match(render({ style: { width: '50%' } }), /width:50%/)
        const controls = Card.__controls
        assert.deepEqual(Object.keys(controls).sort(), Object.keys(Card.defaultProps).sort())
        for (const [key, control] of Object.entries(controls)) assert.equal(control.defaultValue, Card.defaultProps[key], key)
        assert.equal(controls.body.hidden({ showBody: false }), true)
        assert.equal(controls.body.hidden({ showBody: true }), false)
        console.log(`PASS: example parses; default rendering, seven editable props, empty strings, false/zero values, incoming sizing, and control defaults checked with React ${React.version}. Framer registration was mocked; no live Framer verification.`)
    } finally {
        fs.rmSync(temp, { recursive: true, force: true })
    }
}
main().catch(error => { console.error(error); process.exitCode = 1 })
