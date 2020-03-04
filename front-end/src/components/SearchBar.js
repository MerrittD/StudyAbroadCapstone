import React, { Component } from 'react'

/* Dropdown filters */
class SearchBar extends Component {
    /* Constructor to initialize props passed down */
    constructor() {
        super();
    }

    render() {
        let programs = this.props.state.programs;
        let allProgramTerms = programs.map((program) =>
            <option key={program.name}>{program.term}</option>
        );
        let allProgramCountries = programs.map((program) =>
            <option key={program.name}>{program.country}</option>
        );
        let allProgramAreasOfStudy = programs.map((program) =>
            <option key={program.name}>{program.areaOfStudy}</option>
        );
        let allProgramLanguages = programs.map((program) =>
            <option key={program.name}>{program.language}</option>
        );
        return (
            <div>
                <select>
                    {allProgramTerms}
                </select>
                <select>
                    {allProgramCountries}
                </select>
                <select>
                    {allProgramAreasOfStudy}
                </select>
                <select>
                    {allProgramLanguages}
                </select>
                <a href="/ResultPage"> Search</a>
            </div>
        )
    }
}

export default SearchBar;
