"use strict";

// selecting element
const firstName = document.getElementById("first");
const lastName = document.getElementById("last");
const email = document.getElementById("email");
const contact = document.getElementById("mobile");
const gender = document.getElementById("gender").value;
const registerBtn = document.querySelector(".registerbtn");
const err = document.querySelector(".error");

//validate posted data:

const dataValidation = (e) => {
  e.preventDefault();
  clearError();

  const first = firstName.value.trim();
  const last = lastName.value.trim();
  const mail = email.value.trim();
  const number = contact.value.trim();

  if (first.length < 2) {
    showError();
    return;
  }

  if (last.length < 2) {
    showError();
    return;
  }

  if (!mail.match(/^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$/)) {
    showError();
    return;
  }

  if (number.length < 10) {
    showError();
    return;
  }

  const data = {
    firstName: first,
    lastName: last,
    email: mail,
    contact: number,
    gender: gender,
  };

  fetch("http://localhost:5000/", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((result) => console.log(result))
    .catch((error) => console.log(error.message));
};

//error message:
const showError = () => {}; //stil accodring to html

//clear error message:
const clearError = () => {}; //still display none

// event
registerBtn.addEventListener("click", dataValidation);

// new register
