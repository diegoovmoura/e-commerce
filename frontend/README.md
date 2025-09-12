# Frontend README.md

# E-commerce Platform Frontend

This is the frontend part of the E-commerce platform built using Next.js. It provides a user interface for browsing and purchasing products.

## Getting Started

To get started with the frontend application, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd ecommerce-platform/frontend
   ```

2. **Install dependencies**:
   ```
   npm install
   ```

3. **Run the development server**:
   ```
   npm run dev
   ```

4. **Open your browser**:
   Navigate to `http://localhost:3000` to view the application.

## Folder Structure

- `pages/`: Contains the main pages of the application.
  - `index.tsx`: The homepage of the application.
  - `products.tsx`: Displays a list of products fetched from the backend API.
  
- `components/`: Contains reusable components.
  - `ProductCard.tsx`: Represents a single product card.

- `public/`: Contains static assets such as images and icons.

## API Integration

The frontend communicates with the backend API to fetch product data. Ensure that the backend server is running to access the product listings.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.