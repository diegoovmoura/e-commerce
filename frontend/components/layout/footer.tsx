import Link from 'next/link'
import { Github, Twitter, Mail, Heart } from 'lucide-react'
import { Button } from '../ui/button'
import { Input } from '../ui/input'
import { cn } from '../../lib/utils'

interface FooterProps {
  className?: string
}

export function Footer({ className }: FooterProps) {
  return (
    <footer className={cn('bg-primary-800 text-primary-50', className)}>
      <div className="container-custom py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Brand Section */}
          <div className="col-span-1 md:col-span-2">
            <Link href="/" className="flex items-center space-x-2 mb-4">
              <div className="w-8 h-8 bg-gradient-to-r from-primary-500 to-primary-400 rounded-lg flex items-center justify-center">
                <span className="text-primary-900 font-bold text-lg">E</span>
              </div>
              <span className="text-xl font-bold">ECommerce</span>
            </Link>
            <p className="text-primary-200 mb-6 max-w-md">
              Your trusted platform for discovering and purchasing products from local businesses. 
              Connect with vendors and find unique items in your community.
            </p>
            
            {/* Newsletter Signup */}
            <div className="mb-6">
              <h4 className="text-lg font-semibold mb-3">Stay Updated</h4>
              <div className="flex flex-col sm:flex-row gap-2">
                <Input 
                  placeholder="Enter your email"
                  className="bg-primary-700 border-primary-600 text-primary-50 placeholder:text-primary-300"
                />
                <Button variant="secondary" className="whitespace-nowrap">
                  Subscribe
                </Button>
              </div>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Quick Links</h4>
            <nav className="flex flex-col space-y-2">
              <Link href="/products" className="text-primary-200 hover:text-primary-50 transition-colors">
                Products
              </Link>
              <Link href="/businesses" className="text-primary-200 hover:text-primary-50 transition-colors">
                Businesses
              </Link>
              <Link href="/categories" className="text-primary-200 hover:text-primary-50 transition-colors">
                Categories
              </Link>
              <Link href="/deals" className="text-primary-200 hover:text-primary-50 transition-colors">
                Deals
              </Link>
            </nav>
          </div>

          {/* Support */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Support</h4>
            <nav className="flex flex-col space-y-2">
              <Link href="/help" className="text-primary-200 hover:text-primary-50 transition-colors">
                Help Center
              </Link>
              <Link href="/contact" className="text-primary-200 hover:text-primary-50 transition-colors">
                Contact Us
              </Link>
              <Link href="/shipping" className="text-primary-200 hover:text-primary-50 transition-colors">
                Shipping Info
              </Link>
              <Link href="/returns" className="text-primary-200 hover:text-primary-50 transition-colors">
                Returns
              </Link>
            </nav>
          </div>
        </div>

        {/* Bottom Section */}
        <div className="border-t border-primary-700 mt-8 pt-8 flex flex-col md:flex-row items-center justify-between">
          <div className="flex items-center space-x-1 text-primary-200 mb-4 md:mb-0">
            <span>Made with</span>
            <Heart className="w-4 h-4 text-red-500 fill-current" />
            <span>for local businesses</span>
          </div>
          
          {/* Social Links */}
          <div className="flex items-center space-x-4">
            <Button variant="ghost" size="icon" className="text-primary-200 hover:text-primary-50 hover:bg-primary-700">
              <Github className="w-5 h-5" />
            </Button>
            <Button variant="ghost" size="icon" className="text-primary-200 hover:text-primary-50 hover:bg-primary-700">
              <Twitter className="w-5 h-5" />
            </Button>
            <Button variant="ghost" size="icon" className="text-primary-200 hover:text-primary-50 hover:bg-primary-700">
              <Mail className="w-5 h-5" />
            </Button>
          </div>
        </div>

        {/* Copyright */}
        <div className="text-center mt-8 pt-4 border-t border-primary-700">
          <p className="text-primary-300 text-sm">
            © 2025 ECommerce Platform. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  )
}