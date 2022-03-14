import {createStore} from 'vuex'

const store = createStore({
    state: {
        isLoggedIn: false,
        username: '',
        worksheets: []
    },
    mutations: {
        addWorksheet (state, worksheet) {
            state.worksheets.push(worksheet);
        },
     }
})

export default store;