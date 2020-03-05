import React, { Component } from 'react'

/* Dropdown filters */
class SearchBar extends Component {
    /* Constructor to initialize props passed down */
    constructor() {
        super();
    }

    getUnique(arr) {

        return arr.filter((e, i) => arr.indexOf(e) >= i)
    }


    render() {
        /* Pass down array prop holding all programs */
        let programs = this.props.state.programs;
        /* Fill an array with all possible terms (by mapping through every program) */
        let allProgramTerms = programs.map((program) =>
            program.term
        );
        /* Remove all duplicate terms */
        allProgramTerms = this.getUnique(allProgramTerms)
        /* Sort the terms into alphabetical order */
        allProgramTerms.sort()
        /* Make it into an array of options so that we can insert them into our dropdown (below) */
        allProgramTerms = allProgramTerms.map((program, i) =>
            <option key={i}>{program}</option>
        );

        /* Repeat for countries */
        let allProgramCountries = programs.map((program) =>
            program.country
        );
        allProgramCountries = this.getUnique(allProgramCountries)
        allProgramCountries.sort()
        allProgramCountries = allProgramCountries.map((program, i) =>
            <option key={i}>{program}</option>
        );

        /* Repeat for areas of study */
        let allProgramAreasOfStudy = programs.map((program) =>
            program.areaOfStudy
        );
        allProgramAreasOfStudy = this.getUnique(allProgramAreasOfStudy)
        allProgramAreasOfStudy.sort()
        allProgramAreasOfStudy = allProgramAreasOfStudy.map((program, i) =>
            <option key={i}>{program}</option>
        );

        /* Repeat for languages */
        let allProgramLanguages = programs.map((program) =>
            program.language
        );
        allProgramLanguages = this.getUnique(allProgramLanguages)
        allProgramLanguages.sort()
        allProgramLanguages = allProgramLanguages.map((program, i) =>
            <option key={i}>{program}</option>
        );

        return (
            <div>
                <select style={{ relative: 'center' }}>
                    <option default value="Any">Any</option>
                    {allProgramTerms}
                </select>
                <select>
                    <option default value="Any">Any</option>
                    {allProgramCountries}
                </select>
                <select>
                    <option default value="Any">Any</option>
                    {allProgramAreasOfStudy}
                </select>
                <select>
                    <option default value="Any">Any</option>
                    {allProgramLanguages}
                </select>
                <a href="/ResultPage"> <button>Search
                    </button></a>
            </div >
        )
    }
}

export default SearchBar;
