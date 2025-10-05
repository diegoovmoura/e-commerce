/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Your custom color palette
        primary: {
          50: '#f0ebd8',  // Light cream
          100: '#e8dfc2',
          200: '#ddd1a3',
          300: '#d1c284',
          400: '#c4b165',
          500: '#748cab', // Mid-tone blue-gray
          600: '#3e5c76', // Deep blue-gray
          700: '#1d2d44', // Dark blue
          800: '#0d1321', // Darkest navy
          900: '#0a0f1a', // Extra dark
        },
        // Semantic colors using your palette
        background: '#f0ebd8',      // Light cream background
        foreground: '#0d1321',      // Dark navy text
        card: '#ffffff',            // White cards
        'card-foreground': '#1d2d44', // Dark blue text on cards
        border: '#3e5c76',          // Deep blue-gray borders
        input: '#f0ebd8',          // Light cream inputs
        ring: '#748cab',           // Mid-tone focus rings
        muted: {
          DEFAULT: '#3e5c76',      // Deep blue-gray muted
          foreground: '#748cab',   // Mid-tone muted text
        },
        accent: {
          DEFAULT: '#748cab',      // Mid-tone accent
          foreground: '#0d1321',   // Dark navy on accent
        },
        destructive: {
          DEFAULT: '#dc2626',      // Red for errors
          foreground: '#ffffff',   // White text on red
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'Consolas', 'monospace'],
      },
      fontSize: {
        '2xs': '0.625rem',    // 10px
        'xs': '0.75rem',      // 12px
        'sm': '0.875rem',     // 14px
        'base': '1rem',       // 16px
        'lg': '1.125rem',     // 18px
        'xl': '1.25rem',      // 20px
        '2xl': '1.5rem',      // 24px
        '3xl': '1.875rem',    // 30px
        '4xl': '2.25rem',     // 36px
        '5xl': '3rem',        // 48px
        '6xl': '3.75rem',     // 60px
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '128': '32rem',
      },
      animation: {
        'fade-in': 'fadeIn 0.3s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'slide-down': 'slideDown 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
      boxShadow: {
        'soft': '0 2px 8px rgba(13, 19, 33, 0.1)',
        'medium': '0 4px 12px rgba(13, 19, 33, 0.15)',
        'hard': '0 8px 24px rgba(13, 19, 33, 0.2)',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}