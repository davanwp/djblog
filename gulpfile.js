const { src, dest, watch, series, parallel } = require('gulp');
const sass = require('gulp-dart-sass');
const autoprefixer = require('gulp-autoprefixer');
const csso = require('gulp-csso');
const babel = require('gulp-babel');
const rename = require('gulp-rename');
const terser = require('gulp-terser');
const webpack = require('webpack-stream');
const sourcemaps = require('gulp-sourcemaps');
const del = require('del');
const mode = require('gulp-mode')();
const browserSync = require('browser-sync').create();
const exec = require('child_process').exec;

// clean tasks
const clean = () => {
  return del(['static/assets/dist']);
}

const cleanImages = () => {
  return del(['static/assets/dist/images']);
}

const cleanFonts = () => {
  return del(['static/assets/dist/fonts']);
}

// css task
const css = () => {
  return src('static/assets/src/scss/**/*.scss')
    .pipe(mode.development( sourcemaps.init() ))
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer())
    .pipe(mode.production( csso() ))
    // .pipe(rename('app.css'))
    .pipe(mode.development( sourcemaps.write('.') ))
    .pipe(dest('static/assets/dist/css'))
    .pipe(mode.development( browserSync.stream() ));
}

// js task
const js = () => {
  return src('static/assets/src/js/**/*.js')
    .pipe(babel({
      presets: ['@babel/env']
    }))
    .pipe(webpack({
      mode: 'development',
      devtool: 'inline-source-map'
    }))
    .pipe(mode.development( sourcemaps.init({ loadMaps: true }) ))
    .pipe(rename('app.js'))
    .pipe(mode.production( terser({ output: { comments: false }}) ))
    .pipe(mode.development( sourcemaps.write('.') ))
    .pipe(dest('static/assets/dist/js'))
    .pipe(mode.development( browserSync.stream() ));
}

// copy tasks
const copyImages = () => {
  return src('static/assets/src/images/**/*.{jpg,jpeg,png,gif,svg}')
    .pipe(dest('static/assets/dist/images'));
}

const copyFonts = () => {
  return src('static/assets/src/fonts/**/*.{svg,eot,ttf,woff,woff2}')
    .pipe(dest('static/assets/dist/fonts'));
}

const runserver = () =>{
  return exec('python manage.py runserver');
}

// watch task
const watchForChanges = () => {
  
  browserSync.init({
   /*  server: {
      baseDir: './'
    }, */
    notify: false,
    port: 8000,
    proxy: '127.0.0.1:8000'
  });

  watch('static/assets/src/scss/**/*.scss', css);
  watch('static/assets/src/js/**/*.js', js);
  watch('**/*.html').on('change', browserSync.reload);
  watch('static/assets/src/images/**/*.{png,jpg,jpeg,gif,svg}', series(cleanImages, copyImages));
  watch('static/assets/src/fonts/**/*.{svg,eot,ttf,woff,woff2}', series(cleanFonts, copyFonts));
}

// public tasks
exports.default = series(clean, parallel(css, js, copyImages, copyFonts), watchForChanges);
exports.build = series(clean, parallel(css, js, copyImages, copyFonts));
exports.runserver = runserver;