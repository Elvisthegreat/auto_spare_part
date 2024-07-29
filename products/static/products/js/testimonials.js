// Edit section
const editButtons = document.querySelectorAll(".btn-edit");
const commentText = document.getElementById("id_message");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

editButtons.forEach(button => {
    button.addEventListener('click', (e) => {
        const productId = e.target.getAttribute("data-product_id");
        const testimonialId = e.target.getAttribute("data-testimonial_id");
        const testimonialContent = document.getElementById(`testimonial${testimonialId}`).innerText;
        commentText.value = testimonialContent;
        submitButton.innerText = "Update";
        // Set the action attribute to know which testimonial to update
        commentForm.setAttribute("action", `products/${productId}/edit_testimonial/${testimonialId}`);
    });
});


// Delete section
const deleteConfirm = document.getElementById('deleteConfirm');
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.querySelectorAll('.btn-delete');

deleteButtons.forEach(button => {
    button.addEventListener('click', (e) => {
        const productId = e.target.getAttribute("data-product_id");
        const testimonialId = e.target.getAttribute("data-testimonial_id");
        deleteConfirm.href = `products/${productId}/delete_testimonial/${testimonialId}/`;
        deleteModal.show();
    });
});
