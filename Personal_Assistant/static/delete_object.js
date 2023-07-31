function deleteObject(deleteurl, csrftoken) {
    if (confirm("Are you sure you want to delete this object?")) {
        // Perform deletion by making a POST request
        fetch(deleteurl, {
            method: "POST",
            headers: { "X-CSRFToken": csrftoken },
        })
        .then(response => {
            // Check if deletion was successful (status code 204)
            if (response.status === 204) {
                // Refresh the page to update the object list
                location.reload();
            } else {
                alert("Failed to delete the object.");
            }
        })
        .catch(error => {
            console.error("Error occurred while deleting the object:", error);
            alert("An error occurred while deleting the object.");
        });
    }
}
