function showAlert() {
	var username = document.getElementById('username').value
	var email = document.getElementById('email').value
	var password = document.getElementById('password').value
	var confirmPassword = document.getElementById('confirmPassword').value

	if (!username || !email || !password || !confirmPassword) {
		alert('Please fill out the required field!!')
	} else {
		alert('Registration successful. Please login.')
	}
}
