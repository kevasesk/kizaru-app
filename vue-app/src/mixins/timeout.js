export default{
    methods: {
        timeout(ms){
			return new Promise(resolve => setTimeout(resolve, ms));
		}
    },
}