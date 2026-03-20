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
      'sm': '640px',   // mobile large
      'md': '768px',   // tablet
      'lg': '1024px',  // small laptop
      'xl': '1280px',  // desktop
      '2xl': '1536px', // large screen
    },
    extend: {},
  },
  plugins: [],
}