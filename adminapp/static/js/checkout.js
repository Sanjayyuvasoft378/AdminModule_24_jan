const stripe = Stripe('pk_test_51LzfBbSAZLmnjHWef08IIM3sK2vlbQxgiRpZnCB3KX3hjgizyDoGjgewp6YW9FRWRIIwlvjrG5Dd39KElDEWuqDg00JliEVqEd');
const options = {
    clientSecret: '{{CLIENT_SECRET}}',
    // Fully customizable with appearance API.
    appearance: {/*...*/},
  };
  
  // Set up Stripe.js and Elements to use in checkout form, passing the client secret obtained in step 3
  const elements = stripe.elements(options);
  
  // Create and mount the Payment Element
  const paymentElement = elements.create('payment');
  paymentElement.mount('#payment-element');