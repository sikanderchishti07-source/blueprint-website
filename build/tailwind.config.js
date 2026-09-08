/** Tailwind config for BluePrint — brand colours from the logo. */
module.exports = {
  content: ['../site/*.html', '../site/js/*.js'],
  theme: {
    extend: {
      fontFamily: { sans: ['DM Sans', 'sans-serif'], display: ['Plus Jakarta Sans', 'sans-serif'] },
      colors: {
        bp: { ink: '#071d55', dark: '#0a2a7a', primary: '#0f3db2', soft: '#3b62d1', light: '#e9edf9', olive: '#647542', sage: '#a3b56f', green: '#102e20' }
      },
      animation: { 'float': 'float 6s ease-in-out infinite', 'slide-up': 'slideUp 0.8s ease-out forwards', 'fade-in': 'fadeIn 0.3s ease-out forwards' }
    }
  }
};
