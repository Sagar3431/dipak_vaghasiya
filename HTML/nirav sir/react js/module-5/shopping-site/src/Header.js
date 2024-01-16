// src/components/Header.js
import React from 'react';
import styled from 'styled-components';

const StyledHeader = styled.header`
  background-color: #333;
  color: #fff;
  padding: 1rem;
  text-align: center;
`;

const Header = () => {
  return (
    <StyledHeader>
      <h1>Shopping Site</h1>
    </StyledHeader>
  );
};

export default Header;
