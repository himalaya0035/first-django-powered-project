console.log(user)
var email_field = document.getElementById('id_email');
email_field.placeholder = "Email..";
console.log(email_field)
if (user!='AnonymousUser'){
    email_field.value=user_email;
}