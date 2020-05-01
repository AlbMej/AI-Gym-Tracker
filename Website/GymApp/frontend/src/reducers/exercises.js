const initialState = [];


export default function exercises(state=initialState, action) {
    let exerciseList = state.slice();

    switch (action.type) {

        case 'FETCH_EXERCISES':
            return [...state, ...action.exercises];

        case 'ADD_EXERCISE':
            return [...state, action.exercise];

        case 'UPDATE_EXERCISE':
            let exerciseToUpdate = exerciseList[action.index]
            exerciseToUpdate.text = action.exercise.text;
            exerciseList.splice(action.index, 1, exerciseToUpdate);
            return exerciseList;

        case 'DELETE_EXERCISE':
            exerciseList.splice(action.index, 1);
            return exerciseList;

        default:
            return state;
    }
}