/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html', // Path to your Flask templates
        './templates/**/*.j2', // Path to your Flask templates
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
            'custom-lavender': {
                'light': '#bfc1ff',
                'default': '#9498FF',
                'dark': '#585bb7'
            }
        },
        fontFamily: {
            serif: ['roboto-serif', 'serif']
        },
        extend: {
            opacity: ['disabled'],
            cursor: ['disabled'],
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
    ],
}
