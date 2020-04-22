import React, { Component } from 'react'
import { Table, Button, Modal, ModalHeader, ModalBody, ModalFooter, FormGroup, Label, Input } from 'reactstrap'
import axios from 'axios'

/* **Protected Route, Admin Only** 
    Displays all programs in the database, allowing the admin to add, edit, and delete programs
*/
class AdminDashboard extends Component {

    /* Set the initial state:
        @programs: holds data for each program :: for displaying the list of programs
        @newProgramData: holds the data for the program that the user wants to add :: for sending HTTP post requests and updating the DOM
        @editProgramData: (similar to newProgramData) holds the data for the program that is being updated :: for sending HTTP put requests 
                            and updating DOM
        @newProgramModal: toggles the Add a Program window :: for knowing when the window should be opened and closed
        @editProgramModal: toggles the Edit a Program window :: for knowing when the window should be opened and closed
    */
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
    /* Run after initial render */
    componentDidMount() {
        this.refreshPrograms();

    }

    /* Toggles Add a Program window */
    toggleNewProgramModal() {
        this.setState({
            newProgramModal: !this.state.newProgramModal
        });
    }

    /* Toggles Edit a Program window */
    toggleEditProgramModal() {
        this.setState({
            editProgramModal: !this.state.editProgramModal
        });
    }

    /* Perform a post request to add a new program to the database */
    addProgram() {
        // Access api route and pass along newProgramData, which holds user input from the Add a Program window
        axios.post('https://my-json-server.typicode.com/MasonTDaniel/capstonedummydata/allPrograms', this.state.newProgramData)
            .then(response => {
                //Add the new program to the existing programs
                let { programs } = this.state;
                programs.push(response.data);
                // Toggle (close) the Add a Program window, clear the current-program-added var for future use
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

    /* Open the Edit a Program window with fields prefilled with data corresponding to the program being edited */
    editProgram(id, country, term, name, language, cost) {
        this.setState({
            editProgramData: { id, country, term, name, language, cost },
            editProgramModal: !this.state.editProgramModal
        });
    }

    /* Perform a put request to edit an existing program in the database when the user clicks Update
        Keep in mind that at this point, editProgramData was called and the user is assumed to have entered the updated info.
        Now, we must transfer that new information to the database
    */
    updateProgram() {
        // Extract the users input for updated info
        let { country, term, name, language, cost } = this.state.editProgramData;
        // Alter the database by passing that info through an http request
        axios.put('https://my-json-server.typicode.com/MasonTDaniel/capstonedummydata/allPrograms' + '/' + this.state.editProgramData.id, {
            country, term, name, language, cost
        })
            .then(response => {
                // Re-call the database to show updated program list in DOM
                this.refreshPrograms();
                // Toggle (close) Edit a Program window, clear the current-program-edited var for future use
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

    // Delete a program from the database, re-call the database to show updated program list
    deleteProgram(id) {
        axios.delete('https://my-json-server.typicode.com/MasonTDaniel/capstonedummydata/allPrograms' + '/' + id)
            .then(response => {
                this.refreshPrograms();
            })
    }

    refreshPrograms() {
        /* Fetch the data from the database */
        axios.get('https://my-json-server.typicode.com/MasonTDaniel/capstonedummydata/allPrograms')
            /* Store the response (an array of all programs) into programs */
            .then(response => {
                this.setState({
                    programs: response.data
                });
            }, (error) => {
                console.log(error);
            });
    }

    render() {
        // Make a table of programs and store it
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
                        <Button color="danger" size="sm" onClick={this.deleteProgram.bind(this, program.id)} >Delete</Button>
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
