import vue from 'rollup-plugin-vue';
import babel from 'rollup-plugin-babel';
import commonjs from 'rollup-plugin-commonjs';
import resolve from 'rollup-plugin-node-resolve';

export default {
  input: 'src/main.js',
  output: {
    file: 'dist/bundle.js',
    format: 'cjs',
  },
  plugins: [
    resolve({
      mainFields: ['module', 'main'],
    }),
    commonjs({
      include: /node_modules/,
      namedExports: {
        'node_modules/lodash/lodash.js': [
          'get',
          'isEmpty',
          'isEqual',
          'cloneDeep',
        ],
      },
    }),
    vue({
      css: true,
      compileTemplate: true,
    }),
    babel({
      exclude: 'node_modules/**',
      presets: ['@babel/preset-env'],
    }),
  ],
};
