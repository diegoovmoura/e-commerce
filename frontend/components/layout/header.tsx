'use client'

import Link from 'next/link'
import { useState } from 'react'
import { Menu, X, ShoppingCart, User, Search } from 'lucide-react'
import { Button } from '../ui/button'
import { Input } from '../ui/input'
import { cn } from '../../lib/utils'

interface HeaderProps {
  className?: string
}

export function Header({ className }: HeaderProps) {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return (
    <header className={cn('bg-background border-b border-primary-200 sticky top-0 z-50', className)}>
      <div className="container-custom">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-gradient-to-r from-primary-600 to-primary-500 rounded-lg flex items-center justify-center">
              <span className="text-primary-50 font-bold text-lg">E</span>
            </div>
            <span className="text-xl font-bold text-foreground">ECommerce</span>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center space-x-8">
            <Link href="/" className="nav-link">
              Home
            </Link>
            <Link href="/products" className="nav-link">
              Products
            </Link>
            <Link href="/businesses" className="nav-link">
              Businesses
            </Link>
            <Link href="/about" className="nav-link">
              About
            </Link>
          </nav>

          {/* Search Bar */}
          <div className="hidden lg:flex flex-1 max-w-md mx-8">
            <div className="relative w-full">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground w-4 h-4" />
              <Input
                placeholder="Search products..."
                className="pl-10 bg-primary-50 border-primary-200"
              />
            </div>
          </div>

          {/* Desktop Actions */}
          <div className="hidden md:flex items-center space-x-4">
            <Button variant="ghost" size="icon" className="relative">
              <ShoppingCart className="w-5 h-5" />
              <span className="absolute -top-2 -right-2 bg-primary-600 text-primary-50 text-xs rounded-full w-5 h-5 flex items-center justify-center">
                3
              </span>
            </Button>
            <Button variant="ghost" size="icon">
              <User className="w-5 h-5" />
            </Button>
            <Button asChild>
              <Link href="/auth/login">Login</Link>
            </Button>
          </div>

          {/* Mobile Menu Button */}
          <Button
            variant="ghost"
            size="icon"
            className="md:hidden"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </Button>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className="md:hidden py-4 border-t border-primary-200">
            <div className="flex flex-col space-y-4">
              {/* Mobile Search */}
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground w-4 h-4" />
                <Input
                  placeholder="Search products..."
                  className="pl-10 bg-primary-50 border-primary-200"
                />
              </div>
              
              {/* Mobile Navigation Links */}
              <nav className="flex flex-col space-y-2">
                <Link href="/" className="nav-link">
                  Home
                </Link>
                <Link href="/products" className="nav-link">
                  Products
                </Link>
                <Link href="/businesses" className="nav-link">
                  Businesses
                </Link>
                <Link href="/about" className="nav-link">
                  About
                </Link>
              </nav>
              
              {/* Mobile Actions */}
              <div className="flex items-center justify-between pt-4 border-t border-primary-200">
                <div className="flex items-center space-x-4">
                  <Button variant="ghost" size="icon" className="relative">
                    <ShoppingCart className="w-5 h-5" />
                    <span className="absolute -top-2 -right-2 bg-primary-600 text-primary-50 text-xs rounded-full w-5 h-5 flex items-center justify-center">
                      3
                    </span>
                  </Button>
                  <Button variant="ghost" size="icon">
                    <User className="w-5 h-5" />
                  </Button>
                </div>
                <Button asChild>
                  <Link href="/auth/login">Login</Link>
                </Button>
              </div>
            </div>
          </div>
        )}
      </div>
    </header>
  )
}