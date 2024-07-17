/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

/**
 * Get the stripe public key in the bottom of our checkout.html.
   And client secret from the template using a little jQuery.
   Remember those little script elements contain the values we need as their text.
 */
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Funtionality
// Handle realtime validation errors on card element
card.addEventListener('change', function(event) {
    // And every time it changes we'll check to see if there are any errors.
    var errorDiv = document.getElementById('card-errors');
    // If so, display card errors div we created near the card element on the checkout page.
    if(event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `
        $(errorDiv).html(html);
    }else {
        errorDiv.textContent = '';
    }
})

// Handle form Submit
