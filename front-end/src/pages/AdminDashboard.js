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
        @isDisabled: true when there is still an empty field :: for making sure all fields have input before adding a program
    */
    constructor() {
        super();
        this.state = {
            programs: [],
            newProgramData: {
                country: '',
                term: '',
                name: '',
                areaOfStudy: '',
                language: '',
                cost: '',
                website: ''
            },
            editProgramData: {
                id: '',
                country: '',
                term: '',
                name: '',
                areaOfStudy: '',
                language: '',
                cost: '',
                website: ''
            },
            newProgramModal: false,
            editProgramModal: false,
            isDisabled: true
        };

    }
    /* Run after initial render */
    componentDidMount() {
        /* Fetch the data from the database */
        axios.get('https://studyabroad-test-server.herokuapp.com/db')
            /* Store the response (an array of all programs) into programs */
            .then(response => {
                this.setState({
                    programs: response.data.allPrograms
                });
            }, (error) => {
                console.log(error);
            });
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
        axios.post('https://studyabroad-test-server.herokuapp.com/allPrograms', this.state.newProgramData)
            .then(response => {
                //Add the new program to the existing programs
                let { programs } = this.state;
                programs.push(response.data);

                // Toggle (close) the Add a Program window, clear the current-program-added var for future use
                this.setState({
                    programs, newProgramModal: false, isDisabled: true, newProgramData: {
                        id: '',
                        country: '',
                        term: '',
                        name: '',
                        areaOfStudy: '',
                        language: '',
                        cost: '',
                        website: ''
                    }
                });
            });
    }

    /* Open the Edit a Program window with fields prefilled with data corresponding to the program being edited */
    editProgram(id, country, term, name, areaOfStudy, language, cost, website) {
        this.setState({
            editProgramData: { id, country, term, name, areaOfStudy, language, cost, website },
            editProgramModal: !this.state.editProgramModal
        });
    }

    /* Perform a put request to edit an existing program in the database when the user clicks Update
        Keep in mind that at this point, editProgramData was called and the user is assumed to have entered the updated info.
        Now, we must transfer that new information to the database
    */
    updateProgram() {
        // Extract the users input for updated info
        let { country, term, name, areaOfStudy, language, cost, website } = this.state.editProgramData;
        // Alter the database by passing that info through an http request
        axios.put('https://studyabroad-test-server.herokuapp.com/allPrograms/' + '/' + this.state.editProgramData.id, {
            country, term, name, areaOfStudy, language, cost, website
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
                        areaOfStudy: '',
                        language: '',
                        cost: '',
                        website: ''
                    }
                });
            })
    }

    // Delete a program from the database, re-call the database to show updated program list
    // Program name
    deleteProgram(id) {
        axios.delete('https://studyabroad-test-server.herokuapp.com/allPrograms' + '/' + id)
            .then(response => {
                this.refreshPrograms();
            })
    }

    /* Get current data instance */
    refreshPrograms() {
        /* Fetch the data from the database */
        axios.get('https://studyabroad-test-server.herokuapp.com/db')
            /* Store the response (an array of all programs) into programs */
            .then(response => {
                this.setState({
                    programs: response.data.allPrograms
                });
            }, (error) => {
                console.log(error);
            });
    }

    /* Toggle the Add a Program button
        True: when all fields have input
        False: when one input field is blank*/
    isDisabled = () => {
        let empty = '';
        // Check that all fields have input and enable the button if so
        if (!this.state.newProgramData.country == empty && !this.state.newProgramData.term == empty
            && !this.state.newProgramData.name == empty && !this.state.newProgramData.areaOfStudy == empty
            && !this.state.newProgramData.language == empty && !this.state.newProgramData.cost == empty
            && !this.state.newProgramData.website == empty) {
            this.setState({
                isDisabled: false
            })
        } else {
            this.setState({
                isDisabled: true
            })
        }
    }

    render() {
        // Make a table of programs and store it
        let programs = this.state.programs.map((program) => {
            return (
                // This represents one row in the table i.e. one program
                <tr key={program.id}>
                    <td>{program.id}</td>
                    <td>{program.country}</td>
                    <td>{program.term}</td>
                    <td>{program.name}</td>
                    <td>{program.areaOfStudy}</td>
                    <td>{program.language}</td>
                    <td>{program.cost}</td>
                    <td><a href={"https://" + program.website} target="_blank" rel="noopener noreferrer">{program.website}</a></td>
                    <td style={{ "width": "10rem" }}>
                        <Button style={{ "width": "3.75rem", "marginRight": "0.2rem", "marginLeft": "0.2rem" }}
                            color="success" size="sm"
                            onClick={this.editProgram.bind(this, program.id, program.country, program.term, program.name, program.areaOfStudy, program.language, program.cost, program.website)}>Edit</Button>
                        <Button
                            style={{ "width": "3.75rem", "marginRight": "0.2rem", "marginLeft": "0.2rem" }}
                            color="danger" size="sm"
                            onClick={this.deleteProgram.bind(this, program.id)} >Delete</Button>
                    </td>
                </tr>
            )

        });
        return (
            <div>
                {/* Our 'Add a Program' input form that displays when Add Program is clicked */}
                <Button style={{ "marginBottom": "1rem" }} color="primary" onClick={this.toggleNewProgramModal.bind(this)}>Add Program</Button>
                <Modal isOpen={this.state.newProgramModal} toggle={this.toggleNewProgramModal.bind(this)}>
                    <ModalHeader toggle={this.toggleNewProgramModal.bind(this)}>Add a new program</ModalHeader>
                    <ModalBody>
                        <FormGroup>
                            <Label for="Country">Country</Label>
                            {/* Stores any input for country into this.state.newProgramData.country */}
                            {/* Process repeated for each input field (e.g. term, language, etc.) */}
                            <Input id="country" placeholder='e.g. " Spain"' value={this.state.newProgramData.country} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.country = e.target.value;
                                this.setState({ newProgramData });
                                this.isDisabled();
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Term">Term</Label>
                            <Input id="term" placeholder='e.g. " Fall"' value={this.state.newProgramData.term} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.term = e.target.value;
                                this.setState({ newProgramData });
                                this.isDisabled();
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Name">Program Name</Label>
                            <Input id="name" placeholder='e.g. "Universidad de Vigo"' value={this.state.newProgramData.name} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.name = e.target.value;
                                this.setState({ newProgramData });
                                this.isDisabled();
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="AreaOfStudy">Area of Study</Label>
                            <Input id="areaOfStudy" placeholder='e.g. "Intercultural Studies"' value={this.state.newProgramData.areaOfStudy} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.areaOfStudy = e.target.value;
                                this.setState({ newProgramData });
                                this.isDisabled();
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Language">Language</Label>
                            <Input id="language" placeholder='e.g. "English"' value={this.state.newProgramData.language} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.language = e.target.value;
                                this.setState({ newProgramData });
                                this.isDisabled();
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Cost">Cost</Label>
                            <Input id="cost" placeholder='e.g. "20,000"' value={this.state.newProgramData.cost} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.cost = e.target.value;
                                this.setState({ newProgramData });
                                this.isDisabled();
                            }} />
                        </FormGroup>
                        <FormGroup>
                            <Label for="Website">Website</Label>
                            <Input id="website" placeholder='e.g. "www.southwestern.edu"' value={this.state.newProgramData.website} onChange={(e) => {
                                let { newProgramData } = this.state;
                                newProgramData.website = e.target.value;
                                this.setState({ newProgramData });
                                this.isDisabled();
                            }} />
                        </FormGroup>
                    </ModalBody>
                    <ModalFooter>
                        {/* Whenever Add Program button is clicked, we run addProgram(), and all fields are stored in newProgramData */}
                        <Button disabled={this.state.isDisabled} color="primary" onClick={this.addProgram.bind(this)}>Add Program</Button>{' '}
                        <Button color="secondary" onClick={this.toggleNewProgramModal.bind(this)}>Cancel</Button>
                    </ModalFooter>
                </Modal>
                {/* Our 'Edit a Program' input form that displays when Edit is clicked */}
                <Modal isOpen={this.state.editProgramModal} toggle={this.toggleEditProgramModal.bind(this)}>
                    <ModalHeader toggle={this.toggleEditProgramModal.bind(this)}>Edit a program</ModalHeader>
                    <ModalBody>
                        {/* Input for this program is already stored in this.state.editProgramData, so autofill the form with that data */}
                        {/* Similar to Add a Program, we check for input change on all fields and store in this.state.editProgramData */}
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
                            <Label for="AreaOfStudy">Area of Study</Label>
                            <Input id="areaOfStudy" placeholder='e.g. "Intercultural Studies"' value={this.state.editProgramData.areaOfStudy} onChange={(e) => {
                                let { editProgramData } = this.state;
                                editProgramData.areaOfStudy = e.target.value;
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
                        <FormGroup>
                            <Label for="Website">Website</Label>
                            <Input id="website" placeholder='e.g. "www.southwestern.edu"' value={this.state.editProgramData.website} onChange={(e) => {
                                let { editProgramData } = this.state;
                                editProgramData.website = e.target.value;
                                this.setState({ editProgramData });
                            }} />
                        </FormGroup>
                    </ModalBody>
                    <ModalFooter>
                        {/* updateProgram() is called, with the updated data stored in this.state.editProgramData */}
                        <Button color="primary" onClick={this.updateProgram.bind(this)}>Update</Button>{' '}
                        <Button color="secondary" onClick={this.toggleEditProgramModal.bind(this)}>Cancel</Button>
                    </ModalFooter>
                </Modal>

                {/* Display the data in a table */}
                <Table>
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>Country</th>
                            <th>Term</th>
                            <th>Name</th>
                            <th>Area Of Study</th>
                            <th>Language</th>
                            <th>Cost</th>
                            <th>Website</th>
                            <th></th>
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
