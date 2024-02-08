/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html', // Path to your Flask templates
        './templates/**/*.j2', // Path to your Flask templates
        './path/to/other/html/or/js/files/**/*.html',
        './path/to/other/html/or/js/files/**/*.js',
    ],
    theme: {
        // colors: {
        //     'black': '#000',
        //     'white': '#fff',
        //
        // },
        fontFamily: {
            serif: ['roboto-serif', 'serif']
        },
        extend: {
            opacity: ['disabled'],
            cursor: ['disabled'],
            colors: {
                'black': '#000',
                'white': '#fff',
                'custom-lavender': {
                    'light': '#bfc1ff',
                    'default': '#9498FF',
                    'dark': '#585bb7'
                },
                'grenadier': {
                    '50': '#fff5ed',
                    '100': '#ffe9d5',
                    '200': '#ffcea9',
                    '300': '#ffac72',
                    '400': '#fd7e3a',
                    '500': '#fc5b13',
                    '600': '#e23d09',
                    '700': '#c42d0a',
                    '800': '#9c2510',
                    '900': '#7d2111',
                    '950': '#440e06',
                },

            },
            gradientColorStops: {
                'primary': '#fd7e3a',
                'secondary': '#e23d09',
                'hover-primary': '#fc5b13',
                'hover-secondary': '#c42d0a',
            },
            madWidth: {
                'custom' : '500px'
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('autoprefixer'),
        ["prettier-plugin-tailwindcss"],
        require('tailwind-gradients'),
    ],
}
