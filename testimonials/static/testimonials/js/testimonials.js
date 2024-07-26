// Edit
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_message");
const commentForm = document.getElementById("commentForms");
const submitButton = document.getElementById("submitButton");

for(let button of editButtons){
    button.addEventListener('click', (e) => {
        let testimonialId = e.target.getAttribute("data-testimonial_id");
        let testimonialContent = document.getElementById(`testimonial${testimonialId}`).innerText;
        commentText.value = testimonialContent;
        submitButton.innerText = "Update";
        // action attribute to know which testimonial to update
        commentForm.setAttribute("action", `edit_testimonial/${testimonialId}`);
    });
}