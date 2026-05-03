// TODO(bader):
// [ ] - register form, on click should trigger also the picture upload form
// [ ] - on click, username is obtained from first form, and then alongside the
// actual picture, sent to the user_add_picture endpoint


const userRegisterButton = document.getElementById("user_register_button");
userRegisterButton.addEventListener("click", e=>
    {
        e.preventDefault();
        alert("button clicked!");
    }
)
