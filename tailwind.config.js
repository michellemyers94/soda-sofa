/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html', // Path to your Flask templates
    './path/to/other/html/or/js/files/**/*.html',
    './path/to/other/html/or/js/files/**/*.js',
  ],
  theme: {
    colors: {
      'black': '#000',
      'white': '#fff',
      'custom-orange': {
        'light': '#ef6f47',
        'default': '#E23D09',
        'dark': '#853b24'
      },
    },
    fontFamily: {
      serif: ['roboto-serif']
    },
    extend: {},
  },
  plugins: [],
}
