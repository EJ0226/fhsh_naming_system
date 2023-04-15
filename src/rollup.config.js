import vue from 'rollup-plugin-vue'
import commonjs from '@rollup/plugin-commonjs'
import resolve from '@rollup/plugin-node-resolve'
import babel from '@rollup/plugin-babel'
import json from '@rollup/plugin-json'
import postcss from 'rollup-plugin-postcss'
import replace from '@rollup/plugin-replace'

export default {
  input: 'src/main.js',
  output: {
    file: 'bundle.js',
    format: 'cjs',
  },
  plugins: [
    vue({
      css: true,
      compileTemplate: true,
    }),
    commonjs(),
    resolve(),
    babel({
      babelHelpers: 'bundled',
      exclude: 'node_modules/**',
    }),
    json(),
    postcss({
      plugins: [],
      extract: false,
      minimize: true,
      sourceMap: 'inline',
    }),
    replace({
      'process.env.NODE_ENV': JSON.stringify('production'),
    }),
  ],
  external: ['vue'],
}
