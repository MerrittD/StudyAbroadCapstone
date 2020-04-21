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
            editProgramData: {
                id: '',
                country: '',
                term: '',
                name: '',
                language: '',
                cost: ''
            },
            newProgramModal: false,
            editProgramModal: false
        };

    }

    componentDidMount() {
        this.refreshPrograms();

    }

    toggleNewProgramModal() {
        this.setState({
            newProgramModal: !this.state.newProgramModal
        });
    }

    toggleEditProgramModal() {
        this.setState({
            editProgramModal: !this.state.editProgramModal
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

    updateProgram() {
        let { country, term, name, language, cost } = this.state.editProgramData;
        axios.put('https://my-json-server.typicode.com/MasonTDaniel/capstonedummydata/allPrograms' + this.state.editProgramData.id, {
            country, term, name, language, cost
        })
            .then(response => {
                this.refreshPrograms();

                this.setState({
                    editProgramModal: !this.state.editProgramModal, editProgramData: {
                        id: '',
                        country: '',
                        term: '',
                        name: '',
                        language: '',
                        cost: ''
                    }
                });
            })
    }

    refreshPrograms() {
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
    }

    editProgram(id, country, term, name, language, cost) {
        this.setState({
            editProgramData: { id, country, term, name, language, cost },
            editProgramModal: !this.state.editProgramModal
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
                        <Button color="success" size="sm" className="mr-2 mb-1" onClick={this.editProgram.bind(this, program.id, program.country, program.term, program.name, program.language, program.cost)}>Edit</Button>
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

                <Modal isOpen={this.state.editProgramModal} toggle={this.toggleEditProgramModal.bind(this)}>
                    <ModalHeader toggle={this.toggleEditProgramModal.bind(this)}>Edit a program</ModalHeader>
                    <ModalBody>
                        <FormGroup>
                            <Label for="Country">Country</Label>
                            <Input id="country" placeholder='e.g. " Spain"' value={this.state.editProgramData.country} onChange={(e) => {
                                let { editProgramData } = this.state;
                                editProgramData.country = e.target.value;
                                this.setState({ editProgramData });
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Term">Term</Label>
                            <Input id="term" placeholder='e.g. " Fall"' value={this.state.editProgramData.term} onChange={(e) => {
                                let { editProgramData } = this.state;
                                editProgramData.term = e.target.value;
                                this.setState({ editProgramData });
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Name">Program Name</Label>
                            <Input id="name" placeholder='e.g. "Universidad de Vigo"' value={this.state.editProgramData.name} onChange={(e) => {
                                let { editProgramData } = this.state;
                                editProgramData.name = e.target.value;
                                this.setState({ editProgramData });
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Language">Language</Label>
                            <Input id="language" placeholder='e.g. "English"' value={this.state.editProgramData.language} onChange={(e) => {
                                let { editProgramData } = this.state;
                                editProgramData.language = e.target.value;
                                this.setState({ editProgramData });
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Cost">Cost</Label>
                            <Input id="cost" placeholder='e.g. "20,000"' value={this.state.editProgramData.cost} onChange={(e) => {
                                let { editProgramData } = this.state;
                                editProgramData.cost = e.target.value;
                                this.setState({ editProgramData });
                            }} />
                        </FormGroup>
                    </ModalBody>
                    <ModalFooter>
                        <Button color="primary" onClick={this.updateProgram.bind(this)}>Update</Button>{' '}
                        <Button color="secondary" onClick={this.toggleEditProgramModal.bind(this)}>Cancel</Button>
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
