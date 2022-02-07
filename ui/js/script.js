WindowWidth = 720
WindowHeight = 420

// Запрещаем изменять размер программы
window.onresize = function (){ // || window.outerWidth > WindowWidth || window.outerHeight > WindowHeight
	if (window.outerWidth < WindowWidth || window.outerHeight < WindowHeight){
		window.resizeTo(WindowWidth, WindowHeight);
	}
}

// Блокируем нажатия на клавиши (F5, Ctrl + W, Ctrl + F, etc)
document.onkeydown = function(event) {
	if (window.event) {
		// event.preventDefault()
	}
}
