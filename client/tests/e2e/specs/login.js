// https://docs.cypress.io/api/introduction/api.html

describe('User can login', () => {
  it('Can login and then logout', () => {
    cy.visit('/');
    cy.get('#login-email').type('test@test.com');
    cy.get('#login-password').type('password');
    cy.get('button#login').click();
    cy.url().should('include', '/dashboard');

    cy.contains('LOGOUT').click();
    cy.url().should('eq', 'http://localhost:8081/#/');
  });

  it('Cannot access /dashboard without token', () => {
    cy.visit('/dashboard');
    cy.contains('Please Login or Register').should('be.visible');
  });
});
