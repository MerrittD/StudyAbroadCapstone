import React, { Component } from 'react'
import { Table, Button } from 'reactstrap'
import axios from 'axios'
import ProgramList from '../components/ProgramList'

class AdminDashboard extends Component {

    constructor() {
        super();
        this.state = {
            programs: []
        };

    }

    componentWillMount() {
        /* Fetch the data from the database */
        axios.get('https://my-json-server.typicode.com/MasonTDaniel/capstonedummydata/allPrograms')
            /* Response and promises */
            .then(response => {
                console.log(response.data);
                this.setState({
                    programs: response.data
                });
            }, (error) => {
                console.log(error);
            });
        /* Examine the data and then map it to our initialPrograms array */

    }
    render() {
        console.log(this.state)
        let programs = this.state.programs.map((program) => {
            return (
                <tr key={program.id}>
                    <td>{program.id}</td>
                    <td>{program.country}</td>
                    <td>{program.term}</td>
                    <td>{program.name}</td>
                    <td>{program.language}</td>
                    <td>{program.Cost}</td>
                    <td>
                        <Button color="success" size="sm" className="mr-2 mb-1">Edit</Button>
                        <Button color="danger" size="sm">Delete</Button>
                    </td>
                </tr>
            )

        });
        return (

            <div>
                <Table>
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>Country</th>
                            <th>Term</th>
                            <th>Name</th>
                            <th>Language</th>
                            <th>Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        {programs}
                    </tbody>
                </Table>
            </div>
        )
    }
}

export default AdminDashboard;
