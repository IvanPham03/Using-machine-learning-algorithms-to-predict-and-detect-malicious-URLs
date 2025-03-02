/** @type {import('tailwindcss').Config} */
const withMT = require("@material-tailwind/react/utils/withMT");

module.exports = withMT({
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    screens: {
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
    extend: {
      colors: {
        customBlue: "#07052e",
        customBlue50: "#393667",
        blackrgba50: "rgba(0, 0, 0, 0.5)",
        blackrgba70: "rgba(0, 0, 0, 0.7)"
      }
    },
  },
  plugins: [],
});
