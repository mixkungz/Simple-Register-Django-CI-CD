describe('Landing Page', () => {
  it('shold be able to submit form with email', () => {
    const user = cy
    const appUrl = 'http://localhost:8000'
    user.visit(appUrl)
    user.get('h1')
        .contains('Doge wow wow Doge')
    user.get('input[name="email"]')
        .type('wow@doge.wow')
    user.get('button[type="submit"]')
        .click()
    
    const admin = cy
    admin.visit(`${appUrl}/admin`)
    admin.get('input[name="username"]')
         .type('doge')
         .get('input[name="password"]')
         .type('wow')
         .get('input[type="submit"]')
         .click()
    admin.get('.model-customer > th > a')
         .click()
    admin.get('.field-email > a')
         .should('contain', 'wow@doge.wow')
  })
})
