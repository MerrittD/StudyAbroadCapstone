import React, { Component } from 'react'
import SearchResults from './SearchResults'

/* Dropdown filters */
class SearchBar extends Component {
    /* Constructor to initialize props passed down */
    constructor() {
        super();
    }

    /* Takes out all duplicates of the array passed in */
    getUnique(arr) {

        return arr.filter((e, i) => arr.indexOf(e) >= i)
    }


    render() {
        /* Take in the passed down program array and store it for easy access*/
        let programs = this.props.state.programs;

        /* The following code blocks labeled 1, 2, 3, and 4 each create an array (4 total)
            These arrays hold all available program terms, countries, areas of study, and languages respectively, with no duplicates
            e.g. code block 1. will create an array such as [Spring, Summer, Fall] */


        /* 1. Fill an array with all possible terms (by mapping through every program) */
        let allProgramTerms = programs.map((program) =>
            program.term
        );
        /* Remove all duplicate terms */
        allProgramTerms = this.getUnique(allProgramTerms)
        /* Sort the terms into alphabetical order */
        allProgramTerms.sort()
        /* Make it into an array of options so that we can insert them into our dropdown (below) */
        allProgramTerms = allProgramTerms.map((programTermValue, i) =>
            <option key={i}>{programTermValue}</option>
        );

        /* 2. Repeat for countries */
        let allProgramCountries = programs.map((program) =>
            program.country
        );
        allProgramCountries = this.getUnique(allProgramCountries)
        allProgramCountries.sort()
        allProgramCountries = allProgramCountries.map((programCountryValue, i) =>
            <option key={i}>{programCountryValue}</option>
        );

        /* 3. Repeat for areas of study */
        let allProgramAreasOfStudy = programs.map((program) =>
            program.areaOfStudy
        );
        allProgramAreasOfStudy = this.getUnique(allProgramAreasOfStudy)
        allProgramAreasOfStudy.sort()
        allProgramAreasOfStudy = allProgramAreasOfStudy.map((programAreaOfStudyValue, i) =>
            <option key={i}>{programAreaOfStudyValue}</option>
        );

        /* 4. Repeat for languages */
        let allProgramLanguages = programs.map((program) =>
            program.language
        );
        allProgramLanguages = this.getUnique(allProgramLanguages)
        allProgramLanguages.sort()
        allProgramLanguages = allProgramLanguages.map((programLanguageValue, i) =>
            <option key={i}>{programLanguageValue}</option>
        );

        /* Display 4 dropdowns (populated with terms, countries, areas of study, and languages respectively) and a Search button */
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
                <a> <button onClick={this.searchBy}>Search
                    </button></a>
                <SearchResults userArray={userArray} />
            </div >
        )
    }
}

export default SearchBar;
