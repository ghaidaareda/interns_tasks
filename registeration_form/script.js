"use strict";

// selecting element
const registerBtn = document.querySelector(".registerbtn");

// Error elements
const firstError = document.getElementById("firstError");
const lastError = document.getElementById("lastError");
const emailError = document.getElementById("emailError");
const contactError = document.getElementById("contactError");

// Validate posted data
const dataValidation = (e) => {
  e.preventDefault();
  clearError(firstError, lastError, emailError, contactError);

  const firstName = document.getElementById("first").value.trim();
  const lastName = document.getElementById("last").value.trim();
  const email = document.getElementById("email").value.trim();
  const contact = document.getElementById("mobile").value.trim();
  const gender = document.getElementById("gender").value;

  if (firstName === "" || firstName.length < 3) {
    showError(firstError, "Please enter a valid First name");
    return;
  }

  if (lastName === "" || lastName.length < 3) {
    showError(lastError, "Please enter a valid Last name");
    return;
  }

  if (!email.match(/^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$/)) {
    showError(emailError, "Please enter a valid Email");
    return;
  }

  if (contact.length < 10 || !contact.match(/^\d+$/)) {
    showError(contactError, "Please enter a valid Mobile Number");
    return;
  }

  const data = {
    firstName: firstName,
    lastName: lastName,
    email: email,
    contact: contact,
    gender: gender,
  };
  console.log(data);

  cleardata();
};

// Show error message
const showError = (element, message) => {
  element.style.display = "block";
  element.innerText = message;
};

// Clear error messages
const clearError = (...params) => {
  for (const ele of params) {
    ele.style.display = "none";
  }
};

// clear data again:
const cleardata = () => {
  document.getElementById("first").value = "";
  document.getElementById("last").value = "";
  document.getElementById("email").value = "";
  document.getElementById("mobile").value = "";
  document.getElementById("gender").value = "";
};

// Event
registerBtn.addEventListener("click", dataValidation);

// new register
