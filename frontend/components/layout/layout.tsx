import { ReactNode } from 'react'
import { Header } from './header'
import { Footer } from './footer'
import { cn } from '../../lib/utils'

interface LayoutProps {
  children: ReactNode
  className?: string
  showHeader?: boolean
  showFooter?: boolean
}

export function Layout({ 
  children, 
  className, 
  showHeader = true, 
  showFooter = true 
}: LayoutProps) {
  return (
    <div className="min-h-screen flex flex-col bg-background">
      {showHeader && <Header />}
      
      <main className={cn('flex-1', className)}>
        {children}
      </main>
      
      {showFooter && <Footer />}
    </div>
  )
}

export function Container({ 
  children, 
  className,
  size = 'default' 
}: { 
  children: ReactNode
  className?: string
  size?: 'default' | 'narrow' | 'wide'
}) {
  const sizeClasses = {
    default: 'container-custom',
    narrow: 'container-narrow',
    wide: 'max-w-none mx-auto px-4 sm:px-6 lg:px-8'
  }
  
  return (
    <div className={cn(sizeClasses[size], className)}>
      {children}
    </div>
  )
}

export function Section({ 
  children, 
  className,
  variant = 'default'
}: { 
  children: ReactNode
  className?: string
  variant?: 'default' | 'muted' | 'dark'
}) {
  const variantClasses = {
    default: 'bg-background',
    muted: 'bg-primary-50',
    dark: 'bg-primary-800 text-primary-50'
  }
  
  return (
    <section className={cn('py-12 lg:py-16', variantClasses[variant], className)}>
      {children}
    </section>
  )
}