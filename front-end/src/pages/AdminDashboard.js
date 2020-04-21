import React, { Component } from 'react'
import ProgramList from '../components/ProgramList'

export default class AdminDashboard extends Component {

    constructor() {
        super();
        this.state = {
            programs: [],
        };
    }

    componentDidMount() {
        let initialPrograms = [];
        /* Fetch the data from the database */
        fetch('https://my-json-server.typicode.com/MasonTDaniel/capstonedummydata/db')
            /* Response and promises */
            .then(response => {
                console.log(response);
                return response.json();
            })
            /* Examine the data and then map it to our initialPrograms array */
            .then(data => {
                console.log(data)
                initialPrograms = data.allPrograms.map((program) => {
                    return program
                });
                console.log(initialPrograms);
                /* Set our new state with the programs array filled with the programs from the array found in the data */
                this.setState({
                    programs: initialPrograms
                });
            });
    }
    render() {
        return (
            <div>
                <ProgramList programs={this.state.programs} />
            </div>
        )
    }
}
