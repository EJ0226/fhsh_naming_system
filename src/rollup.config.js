// rollup.config.js

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
    vue(),
    babel({
      exclude: 'node_modules/**',
      presets: ['@babel/preset-env'],
    }),
    commonjs(),
    resolve({
      // 在这里指定 axios 模块的路径
      // 你需要根据你的项目结构修改这个路径
      // 如果你已经安装了 axios，那么可以试试将路径改为 'node_modules/axios/index.js'
      mainFields: ['module', 'main', 'browser'],
      extensions: ['.mjs', '.js', '.json'],
      preferBuiltins: false,
      modulesOnly: true,
      alias: {
        axios: '/path/to/axios',
      },
    }),
  ],
};
