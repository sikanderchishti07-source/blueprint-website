/** Tailwind config for BluePrint — brand colours from the logo. */
module.exports = {
  content: ['../site/*.html', '../site/js/*.js', './arabic.py'],
  theme: {
    extend: {
      fontFamily: { sans: ['DM Sans', 'sans-serif'], display: ['Plus Jakarta Sans', 'sans-serif'] },
      colors: {
        bp: { ink: '#0b2f38', dark: '#0a6f80', primary: '#0e93a8', soft: '#45bbce', light: '#e6f5f8', olive: '#647542', sage: '#a3b56f', green: '#102e20' }
      },
      animation: { 'float': 'float 6s ease-in-out infinite', 'slide-up': 'slideUp 0.8s ease-out forwards', 'fade-in': 'fadeIn 0.3s ease-out forwards' }
    }
  }
};
