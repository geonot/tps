const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    "./index.html", // if you have one in root, typically it's in public
    "./public/index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Open Sans', ...defaultTheme.fontFamily.sans],
        headings: ['Montserrat', ...defaultTheme.fontFamily.sans],
      },
      colors: {
        primaryBlue: '#005A9C',
        secondaryTeal: '#40B0A6',
        accentOrange: '#F08C00',
        neutralDarkGray: '#333333',
        neutralMediumGray: '#767676',
        neutralLightGray: '#F5F5F5',
        successGreen: '#28A745',
        errorRed: '#DC3545',
        // white is #FFFFFF, already a default
      }
    },
  },
  plugins: [],
}
