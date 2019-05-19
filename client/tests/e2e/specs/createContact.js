describe('Create contact', () => {
  it('Logged in user can create contact then delete contact', () => {
    cy.login(); // Example of custom Cypress command (see /support/commands.js)
    cy.contains('Add New Contact').click();

    cy.get('#contact-first-name').type('Cypress1');
    cy.get('#contact-last-name').type('last1');
    cy.get('#contact-phone').type('3031234567');
    cy.get('#contact-email').type('cypress@test.com');
    cy.get('#contact-street').type('5975 Greenwood Plaza Blvd');
    cy.get('#contact-city').type('Greenwood Village');
    cy.get('#contact-state').type('CO');

    // Zipcode lookup
    cy.contains('Lookup Zipcode').click();
    cy.wait(500);
    cy.contains('Zip code found').should('be', 'visible');

    // Submit
    cy.contains('Submit').click();
    cy.contains('Contact created successfully!').should('be', 'visible');
    cy.contains('Close').click();

    // Delete contact
    cy.contains('Cypress1 last1').should('be.visible');
    cy.get('.delete-icon').last().click();
    cy.contains('Cypress1 last1').should('not.be.visible');

    cy.logout(); // Another custom command
  });
});
