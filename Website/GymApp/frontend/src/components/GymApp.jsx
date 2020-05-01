import React, { Component } from 'react';
import {connect} from 'react-redux';

import {exercises, auth} from "../actions";



class GymApp extends Component {

    componentDidMount() {
        this.props.fetchExercises();
    }

    state = {
        text: "",
        updateExerciseId: null,
    }

    resetForm = () => {
        this.setState({text: "", updateExerciseId: null});
    }

    selectForEdit = (id) => {
        let exercise = this.props.exercises[id];
        this.setState({text: exercise.text, updateExerciseId: id});
    }

    submitExercise = (e) => {
        e.preventDefault();
        if (this.state.updateExerciseId === null) {
            this.props.addExercise(this.state.text).then(this.resetForm)
        } else {
            this.props.updateExercise(this.state.updateExerciseId, this.state.text).then(this.resetForm);
        }
    }

    render() {
        return (
            <div>
                <h2>Welcome to AI Sports!</h2>
                <hr />
                <div style={{textAlign: "right"}}>
                    {this.props.user.username} (<a onClick={this.props.logout}>logout</a>)
                </div>

                <h3>Add new exercise</h3>
                <form onSubmit={this.submitExercise}>
                    <input
                        value={this.state.text}
                        placeholder="Enter exercise here..."
                        onChange={(e) => this.setState({text: e.target.value})}
                        required />
                    <button onClick={this.resetForm}>Reset</button>
                    <input type="submit" value="Save Exercise" />
                </form>

                <h3>Exercises</h3>
                <table>
                    <tbody>
                        {this.props.exercises.map((exercise, id) => (
                            <tr key={`exercise_${exercise.id}`}>
                                <td>{exercise.text}</td>
                                <td><button onClick={() => this.selectForEdit(id)}>edit</button></td>
                                <td><button onClick={() => this.props.deleteExercise(id)}>delete</button></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        )
    }
}


const mapStateToProps = state => {
    return {
        exercises: state.exercises,
        user: state.auth.user,
    }
}

const mapDispatchToProps = dispatch => {
    return {
        fetchExercises: () => {
            dispatch(exercises.fetchExercises());
        },
        addExercise: (text) => {
            return dispatch(exercises.addExercise(text));
        },
        updateExercise: (id, text) => {
            return dispatch(exercises.updateExercise(id, text));
        },
        deleteExercise: (id) => {
            dispatch(exercises.deleteExercise(id));
        },
        logout: () => dispatch(auth.logout()),
    }
}


export default connect(mapStateToProps, mapDispatchToProps)(GymApp);
