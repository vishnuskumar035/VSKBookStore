function incrementQuantity(button) {
	let input = button.parentElement.querySelector('.cart-item-quantity')
	let currentValue = parseInt(input.value)
	input.value = currentValue + 1
	updateCartSummary()
}

function decrementQuantity(button) {
	let input = button.parentElement.querySelector('.cart-item-quantity')
	let currentValue = parseInt(input.value)
	if (currentValue > 1) {
		input.value = currentValue - 1
		updateCartSummary()
	}
}

function removeItem(button) {
	button.closest('.cart-item').remove()
	updateCartSummary()
}

function updateCartSummary() {
	// Logic to update cart summary goes here, such as recalculating total price
}
