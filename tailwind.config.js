const colors = require('tailwindcss/colors')
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    './web/templates/base/*.html',
    './web/templates/*.html'
  ],
  theme: {
    extend: {
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        black: colors.black,
        white: colors.white,
        'neutral': {
          50: '#fafafa',
          100: '#f5f5f5',
          200: '#e5e5e5',
        },
      },
    },
    fontFamily: {
      'inconsolata': ['inconsolata','sans-serif'],
      'inter': ['inter']
    },
    screens: {
      'xxs': '1px',
      'xs': '475px',
      ...defaultTheme.screens,
    },
  },
  plugins: [],
}
