Frontend Tests:

1. End-to-End Tests (using Cypress or Playwright)

a. Test Display of Latest Toys
```javascript
describe('Homepage', () => {
  it('should display latest toys', () => {
    cy.visit('http://localhost:3000')
    cy.get('.latest-toys').should('be.visible')
    cy.get('.latest-toys').children().should('have.length', 5) // assuming 5 is the number of latest toys displayed
  })
})
```

b. Test Navigation Menu
```javascript
describe('Navigation Menu', () => {
  it('should navigate to different pages', () => {
    cy.visit('http://localhost:3000')
    cy.get('.nav-menu').within(() => {
      cy.get('Home').click()
      cy.url().should('include', '/home')
      cy.get('Catalog').click()
      cy.url().should('include', '/catalog')
      cy.get('Contact').click()
      cy.url().should('include', '/contact')
    })
  })
})
```

c. Test Search Bar
```javascript
describe('Search Bar', () => {
  it('should search and display the results', () => {
    cy.visit('http://localhost:3000')
    cy.get('.search-bar').type('Lego{enter}')
    cy.url().should('include', '/search?q=Lego')
    cy.get('.search-results').should('be.visible')
  })
})
```

Backend Tests (using pytest for Python/FastAPI):

1. API Integration Tests

a. Test Get Latest Toys API
```python
def test_get_latest_toys():
  response = client.get("/toys/latest")
  assert response.status_code == 200
  assert len(response.json()) == 5
```

b. Test Navigation Menu API
```python
def test_navigation_menu():
  response = client.get("/navigation")
  assert response.status_code == 200
  assert "Home" in response.json()
  assert "Catalog" in response.json()
  assert "Contact" in response.json()
```

c. Test Search Bar API
```python
def test_search_bar():
  response = client.get("/search?q=Lego")
  assert response.status_code == 200
  assert "Lego" in response.json()
```

2. Test Data Validation and Error Handling
```python
def test_invalid_search_query():
  response = client.get("/search")
  assert response.status_code == 400
  assert "Invalid query" in response.json()
```