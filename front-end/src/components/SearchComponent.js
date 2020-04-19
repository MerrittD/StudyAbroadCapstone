import React, { Component } from 'react'
import SearchBar from '../components/SearchBar'
import SearchResults from '../components/SearchResults'

/* This is the parent component for the search feature. Its children include SearchBar and SearchResults */

/* Take in program data from database into an array, and pass down data to SearchBar via props to populate dropdowns */
class SearchComponent extends Component {

    /* Sets the programs array to empty initially */
    constructor(props) {
        super(props);
        this.state = {
            programs: [],
            programTerm: '',
            programCountry: '',
            programAreaOfStudy: '',
            programLanguage: '',
            isLoading: false
        };
    }
    /* Function that lets us fetch from the database
        Data of all programs passed into an array of object called programs*/
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

    handleInputChange = event => {
        const { name, value } = event.target;
        this.setState({
            [name]: value
        });
    };

    handleFormSubmit = event => {
        event.preventDefault();
        console.log('Form Submitted');
    };

    /* What we actually see on the webpage—SearchBar */
    render() {
        const { programTerm, programCountry, programAreaOfStudy, programLanguage, programs } = this.state;

        let filtered = [...programs];
        console.log(programTerm)
        if (programTerm) {
            filtered = filtered.filter(program => program.programTerm.toLowerCase().indexOf(programTerm.toLowerCase()) !== -1);
        }

        if (programCountry) {
            filtered = filtered.filter(program => program.programCountry.toLowerCase().indexOf(programCountry.toLowerCase()) !== -1);
        }

        if (programAreaOfStudy) {
            filtered = filtered.filter(program => program.programAreaOfStudy.toString().indexOf(programAreaOfStudy.toString()) !== -1);
        }

        if (programLanguage) {
            filtered = filtered.filter(program => program.programLanguage.toLowerCase().indexOf(programLanguage.toLowerCase()) !== -1);
        }
        return (
            <div>
                <div>
                    <SearchBar
                        state={this.state}
                        handleInputChange={this.handleInputChange}
                        handleFormSubmit={(event) => {
                            event.preventDefault()
                            this.handleFormSubmit(event);
                        }} />
                </div>
                <div>
                    {filtered.map(program => <SearchResults program={program} key={program.id} />)}
                </div>
            </div>
        )
    }
}

export default SearchComponent;