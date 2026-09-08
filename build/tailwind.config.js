/** Tailwind config for BluePrint — brand colours from the logo. */
module.exports = {
  content: ['../site/*.html', '../site/js/*.js'],
  theme: {
    extend: {
      fontFamily: { sans: ['DM Sans', 'sans-serif'], display: ['Plus Jakarta Sans', 'sans-serif'] },
      colors: {
        bp: { ink: '#04333a', dark: '#005a66', primary: '#007181', soft: '#2a93a3', light: '#e2f1f3', olive: '#647542', sage: '#a3b56f', green: '#102e20' }
      },
      animation: { 'float': 'float 6s ease-in-out infinite', 'slide-up': 'slideUp 0.8s ease-out forwards', 'fade-in': 'fadeIn 0.3s ease-out forwards' }
    }
  }
};
