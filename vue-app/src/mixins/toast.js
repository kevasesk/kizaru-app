import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

export default{
    methods: {
        toast(text, type='info', duration=2000, close=false){
			var color = null;
			switch (type) {
				case 'success': //'linear-gradient(to right, #c8003a, #ff5732 50%)'//
					color = '#56ab2f' // green
					break
				case 'warning':
					color = '#f5af19' // yellow
					break
				case 'error':
					color = '#DA4453' // red
					break
				case 'info':
					color = '#1c92d2' // blue
					break
			}
			Toastify({text: text, duration: duration, close: close, backgroundColor: color}).showToast();
		}
    },
}