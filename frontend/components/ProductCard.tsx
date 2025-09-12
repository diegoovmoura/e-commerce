import React from 'react';

interface ProductCardProps {
    id: number;
    title: string;
    description: string;
    price: number;
    imageUrl: string;
}

const ProductCard: React.FC<ProductCardProps> = ({ id, title, description, price, imageUrl }) => {
    return (
        <div className="product-card" key={id}>
            <img src={imageUrl} alt={title} className="product-image" />
            <h2 className="product-title">{title}</h2>
            <p className="product-description">{description}</p>
            <p className="product-price">${price.toFixed(2)}</p>
            <button className="add-to-cart">Add to Cart</button>
        </div>
    );
};

export default ProductCard;