import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

/**
 * Utility function to merge Tailwind CSS classes
 * Handles conflicts and ensures proper class precedence
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

/**
 * Color palette utilities
 */
export const colors = {
  navy: {
    900: '#0d1321',
    800: '#1d2d44',
  },
  blueGray: {
    700: '#3e5c76',
    500: '#748cab',
  },
  cream: {
    100: '#f0ebd8',
  },
} as const

/**
 * Design tokens
 */
export const designTokens = {
  colors,
  spacing: {
    xs: '0.5rem',    // 8px
    sm: '0.75rem',   // 12px
    md: '1rem',      // 16px
    lg: '1.5rem',    // 24px
    xl: '2rem',      // 32px
    '2xl': '3rem',   // 48px
    '3xl': '4rem',   // 64px
  },
  borderRadius: {
    sm: '0.25rem',   // 4px
    md: '0.5rem',    // 8px
    lg: '0.75rem',   // 12px
    xl: '1rem',      // 16px
  },
  shadows: {
    soft: '0 2px 8px rgba(13, 19, 33, 0.1)',
    medium: '0 4px 12px rgba(13, 19, 33, 0.15)',
    hard: '0 8px 24px rgba(13, 19, 33, 0.2)',
  },
} as const

export type ColorPalette = typeof colors
export type DesignTokens = typeof designTokens