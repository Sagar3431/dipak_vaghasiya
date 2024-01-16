// src/components/ProductList.js
import React from 'react';
import styled from 'styled-components';

const StyledProductList = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  padding: 2rem;
`;

const ProductCard = styled.div`
  border: 1px solid #ccc;
  padding: 1rem;
  margin: 1rem;
  max-width: 300px;
`;

const ProductList = () => {
  // You can fetch products data from an API or use local data
  const products = [
    { id: 1, name: 'Product 1', price: 19.99 },
    { id: 2, name: 'Product 2', price: 29.99 },
    { id: 3, name: 'Product 3', price: 19.99 },
    { id: 4, name: 'Product 4', price: 29.99 },
    // Add more products as needed
  ];

  return (
    <StyledProductList>
      {products.map((product) => (
        <ProductCard key={product.id}>
          <h3>{product.name}</h3>
          <p>${product.price.toFixed(2)}</p>
          <button>Add to Cart</button>
        </ProductCard>
      ))}
    </StyledProductList>
  );
};

export default ProductList;
