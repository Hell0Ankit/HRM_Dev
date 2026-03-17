/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "../templates/**/*.html",
    "../**/templates/**/*.html",
    "../static/**/*.js",
    "../static/**/*.css"
  ],
  theme: {
    screens: {
      'xs': '576px',  
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
    },
    extend: {},
  },
  plugins: [],
}