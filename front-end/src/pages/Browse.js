import React, { Component } from 'react'
import NavBar from '../components/NavBar'
import SearchBar from '../components/SearchBar'

/* Take in data from database and pass down data to SearchBar via props to populate dropdowns */
class Browse extends Component {

    /* Sets the programs array to empty initially */
    constructor() {
        super();
        this.state = {
            programs: [],
        };
    }
    /* Function that lets us fetch from the database
        Data passed into an array of object called programs*/
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
                <NavBar />
                <SearchBar state={this.state} />
            </div>
        )
    }
}

export default Browse;