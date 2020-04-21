import React, { Component } from 'react'
import { Table, Button, Modal, ModalHeader, ModalBody, ModalFooter, FormGroup, Label, Input } from 'reactstrap'
import axios from 'axios'
import ProgramList from '../components/ProgramList'

class AdminDashboard extends Component {

    constructor() {
        super();
        this.state = {
            programs: [],
            newProgramData: {
                country: '',
                term: '',
                name: '',
                language: '',
                cost: ''
            },
            newProgramModal: false
        };

    }

    componentDidMount() {
        /* Fetch the data from the database */
        axios.get('https://my-json-server.typicode.com/MasonTDaniel/capstonedummydata/allPrograms')
            /* Response and promises */
            .then(response => {
                this.setState({
                    programs: response.data
                });
            }, (error) => {
                console.log(error);
            });
        /* Examine the data and then map it to our initialPrograms array */

    }

    toggleNewProgramModal() {
        this.setState({
            newProgramModal: !this.state.newProgramModal
        });
    }

    addProgram() {
        axios.post('https://my-json-server.typicode.com/MasonTDaniel/capstonedummydata/allPrograms', this.state.newProgramData)
            .then(response => {
                let { programs } = this.state;


                programs.push(response.data);
                console.log(programs);
                this.setState({
                    programs, newProgramModal: false, newProgramData: {
                        country: '',
                        term: '',
                        name: '',
                        language: '',
                        cost: ''
                    }
                });
            });
    }

    render() {
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
                <Button color="primary" onClick={this.toggleNewProgramModal.bind(this)}>Add Program</Button>
                <Modal isOpen={this.state.newProgramModal} toggle={this.toggleNewProgramModal.bind(this)}>
                    <ModalHeader toggle={this.toggleNewProgramModal.bind(this)}>Add a new program</ModalHeader>
                    <ModalBody>
                        <FormGroup>
                            <Label for="Country">Country</Label>
                            <Input id="country" placeholder='e.g. " Spain"' value={this.state.newProgramData.country} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.country = e.target.value;
                                this.setState({ newProgramData });
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Term">Term</Label>
                            <Input id="term" placeholder='e.g. " Fall"' value={this.state.newProgramData.term} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.term = e.target.value;
                                this.setState({ newProgramData });
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Name">Program Name</Label>
                            <Input id="name" placeholder='e.g. "Universidad de Vigo"' value={this.state.newProgramData.name} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.name = e.target.value;
                                this.setState({ newProgramData });
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Language">Language</Label>
                            <Input id="language" placeholder='e.g. "English"' value={this.state.newProgramData.language} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.language = e.target.value;
                                this.setState({ newProgramData });
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Cost">Cost</Label>
                            <Input id="cost" placeholder='e.g. "20,000"' value={this.state.newProgramData.cost} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.cost = e.target.value;
                                this.setState({ newProgramData });
                            }} />
                        </FormGroup>
                    </ModalBody>
                    <ModalFooter>
                        <Button color="primary" onClick={this.addProgram.bind(this)}>Add Program</Button>{' '}
                        <Button color="secondary" onClick={this.toggleNewProgramModal.bind(this)}>Cancel</Button>
                    </ModalFooter>
                </Modal>
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
