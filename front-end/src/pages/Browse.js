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
        fetch('https://my-json-server.typicode.com/MasonTDaniel/capstonedatajson/db')
            .then(response => {
                return response.json();
            }).then(data => {
                console.log(data)
                initialPrograms = data.results.map((program) => {
                    return program
                });
                console.log(initialPrograms);
                this.setState({
                    programs: initialPrograms,
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