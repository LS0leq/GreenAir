/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      colors: {
        "primary": "#6089BF",
        "secondary": "#89d5a8",
        "tertiary": "#F6F8F5",
        "quaternary": "#D1D8D0",
        "quinary": "#3A5D8C",
      },
      boxShadow: {
        "box": "0px 0px 34px -5px rgba(66, 68, 90, 1)",
      },
      animation: {
        fadeIn: 'fadeIn 2s ease-out',
        slideIn: 'slideIn 2s ease-out',
        fadeInDelay: 'fadeIn 2s ease-out forwards',
        fadeInDelayExtra: 'fadeIn 3s ease-out forwards',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: 0 },
          '100%': { opacity: 1 },
        },
        slideIn: {
          '0%': { transform: 'translateY(-100px)' },
          '100%': { transform: 'translateY(0)' },
        },
      },
    },
  },
  plugins: [],
}
